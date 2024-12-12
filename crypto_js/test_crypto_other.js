const CryptoJS = require('./node_modules_crypto')

// app 常用
// RIPEMD160 HmacRIPEMD160
console.log(CryptoJS.RIPEMD160('hello world').toString())
console.log(CryptoJS.HmacRIPEMD160('hello world', '12345678').toString())
// PBKDF2 keySize 4/8/16 结果 128/256/512
console.log(CryptoJS.PBKDF2('hello world', '12345678', {keySize: 8, iterations: 100}).toString())


// 不太常用
// EvpKDF RC4 RC4Drop  Rabbit RabbitLegacy
console.log(CryptoJS.EvpKDF('hello world', '12345678', {keySize: 8, iterations: 100}).toString())
