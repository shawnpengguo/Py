const CryptoJS = require('./node_modules_crypto')

/**
 * 只传入 key cryptojs 会自动生成 iv key mode
 * */

const formatObj = {
    // toString 加密前调用
    stringify: function (data) {
        const cipher_data = data
        let diy = {
            res: cipher_data.ciphertext.toString(),
            iv: cipher_data.iv.toString(),
            salt: cipher_data.salt.toString(),
            desc: "xiix"
        }
        return JSON.stringify(diy)
    },

    // 解密前调用
    parse: function (data) {
        let res = JSON.parse(data)
        return {
            res: CryptoJS.lib.CipherParams.create({ciphertext: CryptoJS.enc.Hex.parse(res.res)}),
            iv: CryptoJS.enc.Hex.parse(res.iv),
            salt: CryptoJS.enc.Hex.parse(res.salt),
        }
    },
}

const cfg = {
    format: formatObj,
}

// const text = CryptoJS.enc.Utf8.parse('hello') // 明文会自动采用 utf8 解析
const cipher_text = CryptoJS.AES.encrypt('hello ', '12345678912345678', cfg) // 这个密钥并不是加密的密钥 还是根据这个自动生成一个 key iv salt ,只用于解密得

const hack_cipher_text = CryptoJS.AES.decrypt(cipher_text, '12345678912345678', cfg)
console.log(cipher_text.toString(), hack_cipher_text.toString(CryptoJS.enc.Utf8))
// console.log(cipher_text.key.toString())
// 可以保存下面两个 解密需要用到
// console.log(cipher_text.iv.toString())
// console.log(cipher_text.salt.toString())
