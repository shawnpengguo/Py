 const CryptoJS = require('./node_modules_crypto')

 const to_utf8 = CryptoJS.enc.Utf8.parse('hello world')
 console.log(to_utf8.toString())
 const to_hex = CryptoJS.enc.Hex.parse('68656c6c6f20776f726c64')
 const res = CryptoJS.MD5(to_hex).toString()
 console.log(CryptoJS.MD5('hello world').toString(CryptoJS.enc.Base64), res )