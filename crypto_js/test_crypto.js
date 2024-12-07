
const CryptoJS = require('./node_modules_crypto')

// hex
const transform_utf8_bit = CryptoJS.enc.Utf8.parse('hello world')

const hex_demo = CryptoJS.enc.Hex.stringify(transform_utf8_bit)

const text = CryptoJS.enc.Hex.parse(hex_demo).toString(CryptoJS.enc.Utf8)

console.log(hex_demo, text);

// url
const cn_text = CryptoJS.enc.Utf8.parse('你好 世界')
const transform_text = CryptoJS.enc.Hex.stringify(cn_text)
console.log(transform_text)