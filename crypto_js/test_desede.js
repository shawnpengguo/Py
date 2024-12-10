
const CryptoJS = require('./node_modules_crypto')

/**
 * desede 三次加密
 * des加密 前八个密钥
 * des解密 中八个密钥
 * des加密 后八个密钥
 * 尽量保持八个密钥个不一样 不然和 des 加密一样
 * */

const msg = CryptoJS.enc.Utf8.parse('hello world')
const key = CryptoJS.enc.Utf8.parse('123456781234567812345678') // 24
const iv = CryptoJS.enc.Utf8.parse('12345678')

const cfg = {
    iv,
    mode: CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs7
 }

const cihper_text = CryptoJS.TripleDES.encrypt(msg, key, cfg);
console.log(cihper_text.ciphertext.toString())