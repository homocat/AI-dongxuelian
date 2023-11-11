import { defineStore } from 'pinia'
import router from '../router/index'

import { login, getHistory, getCurrentInfo, register, getAvatar } from '../api/manage'
import { setCookie, removeCookie, getCookie } from '../composables/auth'
import { toast } from '../composables/utils'
import { service } from '../axios'

export const useUserStore = defineStore('user', {
  state: () => ({
    // 用户信息
    userInfo: {
      username: 'defualt',
      id: 0,
    },
    avatar: null,
    // 历史记录
    history: { sdf: 123 }
  }),
  actions: {
    // 登录
    async loginAction(username, password) {
      const res = await login(username, password)
        .then(res => {
          // 存储token
          setCookie(res.data)
          this.userInfo = {
            username,
            id: getCookie(),
          }

          // 登录成功的弹窗
          toast('登录成功', 'success')
          // 跳转到首页
          router.push('/spark')
        })
      return res
    },
    getUserInfo() {
      const id = getCookie()
      this.userInfo.id = id
      getCurrentInfo(id).then(res => {
        this.userInfo.username = res.data.username
      })
    },
    // 用户头像
    async setAvatar() {
      const id = getCookie()
      try {
        const response = await service.get(`/user/avatar/${id}`, {
          params: {
            id
          },
          responseType: 'blob' // 设置响应类型为blob，以便正确处理图片数据
        });

        const blob = new Blob([response.data]);
        this.avatar = URL.createObjectURL(blob);
      } catch (error) {
        toast(error)
        this.avatar = `https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSF84M_riULl7nDa5SN48iC5dQc7sMr8iUjuu2MSIEmHQ&s`
      }
    },
    // 获取历史记录
    async getHistoryAction() {
      const id = getCookie()
      const res = await getHistory(id)
        .then(res => {
          this.history = res
          return res
        })
      return res
    },
    // 退出登录
    logoutAction() {
      removeCookie()
      // 成功退出登录
      toast('成功退出登录', 'success')
      // 跳转到登录页面
      router.push('/login')
      // 重置当前用户信息为空对象
      this.userInfo.username = ''
      this.userInfo.id = 0
    },
    registerAction(username, password, email) {
      register(username, password, email).then(res => {
        // 存储token
        setCookie(res.data)
        this.userInfo = {
          username,
          id: getCookie(),
        }

        // 登录成功的弹窗
        toast('登录成功', 'success')
        // 跳转到首页
        router.push('/spark')
      }).catch(err => {
        toast('用户已存在', 'warning')
      })
    }
  }
})