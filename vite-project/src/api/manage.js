import { service } from "../axios";

const login = (username, password) => {
  return service.post('/user/login', null, {
    params: {
      username,
      password
    }
  })
};

const register = (username, password, email) => {
  return service.post("/user/login", {
    username,
    password,
    email
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

export { 
  login, 
  register,
  changePassword,
  getHistory,
  getCurrentInfo
};