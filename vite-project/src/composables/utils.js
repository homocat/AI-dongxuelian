import { ElNotification, ElMessageBox } from 'element-plus'

// 普通弹窗
export function toast(message, type, duration = 3000) {
  return ElNotification({
    message,
    type,
    duration
  })
}

// 按钮弹窗
export function showModal(content, type, title = '') {
  return ElMessageBox.confirm(
    content,
    title,
    {
      confirmButtonText: '确认',
      cancelButtonText: '取消',
      type
    }
  )
}