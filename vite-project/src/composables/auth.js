import Cookies from 'js-cookie'

const tokenKey = 'token'

function setCookie(token) {
  Cookies.set(tokenKey, token)
}

function getCookie() {
  return Cookies.get(tokenKey)
}

function removeCookie() {
  Cookies.remove(tokenKey)
}

export {
  setCookie,
  getCookie,
  removeCookie
}