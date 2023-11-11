import { createRouter, createWebHashHistory } from "vue-router";

import { useUserStore } from "../store/userStore";

import { getCookie } from "../composables/auth";
import { toast } from "../composables/utils";

const routes = [
  {
    path: "/",
    component: () => import("../view/Home.vue"),
    children: [
      {
        path: '/',
        redirect: "/spark"
      },
      {
        path: '/blog',
        component: () => import("../view/Blog/Blog.vue")
      },
      {
        path: "/health",
        component: () => import("../view/Health.vue")
      },
      {
        path: "/about",
        component: () => import("../view/About.vue")
      },
      {
        path: "/spark",
        component: () => import("../view/Spark.vue")
      }
    ]
  },
  {
    path: "/login",
    component: () => import("../view/Login.vue")
  },

  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    component: () => import("../view/404.vue")
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

// 全屏前置导航守卫
router.beforeEach((to, from) => {
  // 获取token
  const token = getCookie()
  // 如果用户没有登录, 让用户强制跳转到登录页面
  if (!token && to.path !== '/login') {
    toast('请先登录', 'warning')
    return '/login'
  }
  // 如果用户已经登录, 限制用户重复登录
  if (token && to.path === '/login') {
    toast('请勿重复登录', 'error')
    return from.path ? from.path : '/'
  }

  // 如果用户已经登录, 就获取用户信息
  const userStore = useUserStore()
  if (token) {
    userStore.getHistoryAction()
    userStore.getUserInfo()
    userStore.setAvatar()
  }
})

export default router;