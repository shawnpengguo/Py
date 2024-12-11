const CryptoJS = require('./node_modules_crypto')

// aes 128 192 256
// 密钥不同 128 192 256
// 加密轮数 10 12 14
// 分组向量都是 128

const formatObj = {
    // toString 加密前调用
    stringify: function (data) {
        let diy = {
            res: data.ciphertext.toString(),
            desc: "xiix"
        }
        return JSON.stringify(diy)
    },

    // 解密前调用
    parse: function (data) {
        let res = JSON.parse(data)
        return CryptoJS.lib.CipherParams.create({ciphertext: CryptoJS.enc.Hex.parse(res.res)})
    },
}

const text = CryptoJS.enc.Utf8.parse('hello world')
const key = CryptoJS.enc.Utf8.parse('1234567812345678')
const iv = CryptoJS.enc.Utf8.parse('1234567812345678')
const cfg = {
    iv,
    mode: CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs7,
    // format: CryptoJS.format.Hex // 指定输入格式 就不用 cihpertext  了
    format: formatObj // 指定输入格式 就不用 cihpertext  了
}

const cihper_text = CryptoJS.AES.encrypt(text, key, cfg)
const hack_text = CryptoJS.AES.decrypt(cihper_text, key, cfg)

console.log(cihper_text.toString(), hack_text.toString(CryptoJS.enc.Utf8))
/**
 * 注意事项
 * ecb 多段明文一样 ecb 解析是一样的 cbc不是
 * 对称加密算法一定要比明文长，否则不考虑对称加密算法
 * */