
const CryptoJS = require('./node_modules_crypto')

const base64_array = CryptoJS.enc.Utf8.parse('你好 世界')
const base64 = CryptoJS.enc.Base64.stringify(base64_array)
// console.log(base64)

console.log(CryptoJS.enc.Hex.stringify(CryptoJS.enc.Base64.parse(base64)))