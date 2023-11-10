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

export function splitDate(dateString) {
  const trimmedString = dateString.split('.')[0]; // 去掉小数点及其后面的部分
  const validValues = trimmedString.split(' '); // 按空格分割字符串，得到有效部分的数组
  return validValues.join(' '); // 将有效部分的数组重新组合成字符串
}