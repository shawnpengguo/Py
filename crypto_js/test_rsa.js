const CryptoJS = require('./node_modules_crypto')

/**
 * 非对称加密算法 rsa sm2
 * 加密解密使用不同密钥
 * pkcs1 开头 begin rsa private key
 * pkcs8 开头 begin private key
 * 密钥形式 base63 pem hex编码
 *
 * 性能极差 加密安全
 * 填充细节
 * Nopadding 明文最大字节数为密钥字节数  明文与密钥等长 填充字节0 密文不变
 * PkCS1padding 明文最大字节数为密钥字节数 - 11 / 明文与密钥等长 / 每次填充不一样 加密后密文会变
 *
 *
 * js数字签名算法
 * sm2
 * */