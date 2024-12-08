
 const CryptoJS = require('./node_modules_crypto')

 const parse_str = CryptoJS.enc.Utf8.parse('你好 世界')
 const sha1 = CryptoJS.SHA1(parse_str).toString()
 const sha2 = CryptoJS.SHA256(parse_str).toString()
 const sha3 = CryptoJS.SHA512(parse_str).toString()
 const sha4 = CryptoJS.SHA384(parse_str).toString()
 const sha5 = CryptoJS.SHA224(parse_str).toString()
 // sha3 还没流行
 console.log(sha1, sha2, sha3, sha4, sha5, '\n ')

 const create_md5 = CryptoJS.algo.MD5.create()
 console.log(create_md5.update('我好 世界').finalize().toString())