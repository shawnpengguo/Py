const CryptoJS = require('./node_modules_crypto')

// cfg { iv, mode, padding, format }

// 00110001 00110010 00110011 00110100 00110101 00110110 00110111 00111000 12345678
// 00110000 00110011 00110010 00110101 00110100 00110111 00110110 00111001 03254769
// 上面两个加密出来是一样的

const msg = CryptoJS.enc.Utf8.parse('hello world')
const key = CryptoJS.enc.Utf8.parse('03254769') // 64bit 实际使用 54bit （最低位没用到，每个bit最后一位）
const iv = CryptoJS.enc.Utf8.parse('12345678') // 跟分组走

const cfg = {
    iv, // ecb 不需要 iv
    mode: CryptoJS.mode.CBC,
    // mode: CryptoJS.mode.ECB,
    // padding: CryptoJS.pad.Pkcs7
    // 默认 pkcs7
}

const res = CryptoJS.DES.encrypt(msg, key, cfg)
const hack_res = CryptoJS.DES.decrypt(res, key, cfg)
console.log(res.toString(), res.ciphertext.toString())
console.log('hack: ', CryptoJS.enc.Utf8.stringify(hack_res ))
