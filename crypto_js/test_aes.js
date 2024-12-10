
const CryptoJS = require('./node_modules_crypto')

// aes 128 192 256
// 密钥不同 128 192 256
// 加密轮数 10 12 14
// 分组向量都是 128

const text = CryptoJS.enc.Utf8.parse('hello world')
const key = CryptoJS.enc.Utf8.parse('1234567812345678')
const iv = CryptoJS.enc.Utf8.parse('1234567812345678')
const cfg = {
    iv,
    mode: CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs7
}

const cihper_text = CryptoJS.AES.encrypt(text, key, cfg)
const hack_text = CryptoJS.AES.decrypt(cihper_text, key, cfg)
console.log(cihper_text.ciphertext.toString(), hack_text.toString(CryptoJS.enc.Utf8))
