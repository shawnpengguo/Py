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


/**
 * 主要记录 charles window 的安装设置（如果 window proxy 不能代理 直接用系统自带的代理开启）
 * 浏览器 network 的一些缺陷（如不同tab只能开启一个network进行监听请求）
 * 监听python发出的请求，通过配置 proxy 进行， verify 设为false 取消证书可信
 * 配置 proxifier 配合 charles 。
 * */