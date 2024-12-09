
const Crypto = require('./node_modules_crypto')

// hex -> base64
const str_array = Crypto.enc .Utf8.parse('hello world').toString()
const hex_to_array = Crypto.enc.Hex.parse(str_array).toString(Crypto.enc.Base64)

console.log(hex_to_array )

// 默认 world array is hex
// hex value -> parse

