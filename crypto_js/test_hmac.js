
const CryptoJS = require('./node_modules_crypto')

const hmac_key = '01'
const create_hmac = CryptoJS.HmacMD5('hello world', hmac_key)
console.log(create_hmac.toString())

const createHmac = CryptoJS.algo.HMAC.create(CryptoJS.algo.SHA1.create(), '01')
createHmac.update('hello world')
console.log(createHmac.finalize().toString())