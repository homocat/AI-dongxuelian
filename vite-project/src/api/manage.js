import { service } from "../axios";
import { toast } from "../composables/utils";

const login = (username, password) => {
  return service.post('/user/login', null, {
    params: {
      username,
      password
    }
  }).catch(() => {
    toast('账号错误', 'error')
  })
};

const register = (username, password, email) => {
  if (username === '') {
    toast('用户名不能为空', 'error')
    return
  }
  return service.post("/user/register", {
    diabled: false,
    username,
    password,
    email,
  })
}

const changePassword = (old_pass, new_pass, current_user) => {
  return service.put("/user/me/password", {
    password: old_pass,
    new_password: new_pass,
    id: current_user
  })
}

async function getHistory(current_user) {
  return service.post("/ai/history", null, {
    params: {
      id: current_user
    }
  })
}

async function getCurrentInfo(current_user) {
  return service.post("/user/userinfo", null, {
    params: {
      id: current_user
    }
  })
}

async function getAvatar(current_user) {
  try {
    const response = await service.get(`/user/avatar/${current_user}`, {
      params: {
        id: current_user
      },
      responseType: 'blob' // 设置响应类型为blob，以便正确处理图片数据
    });

    const blob = new Blob([response.data]);
    this.avatarUrl = URL.createObjectURL(blob);
  } catch (error) {
    return `https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSF84M_riULl7nDa5SN48iC5dQc7sMr8iUjuu2MSIEmHQ&s`
  }
}


export {
  login,
  register,
  changePassword,
  getHistory,
  getCurrentInfo,
  getAvatar
};