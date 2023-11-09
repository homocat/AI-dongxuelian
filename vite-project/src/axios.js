import axios from 'axios'

export const service = axios.create({
  baseURL: "/api",
})
