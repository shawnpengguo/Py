// e9284d45-cf2a-4e46-9367-f122413ca6b0

const CryptoJS = require('../crypto_js/node_modules_crypto')

const pwd = "a12345678".trim()
const desKey = "e9284d45-cf2a-4e46-9367-f122413ca6b0"
const encryptByDES = (pwd, key) => {
    var a = CryptoJS.enc.Utf8.parse(key);
    try {
        var s = CryptoJS.DES.encrypt(String(pwd), a, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        })
    } catch (t) {
        console.log(t)
    }
    return s.toString()
}

console.log(encryptByDES(pwd, desKey))