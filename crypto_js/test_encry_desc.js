/**
 * 加密算法：解密/加密可逆算法
 * 对称加密算法：解密/加密 使用相同密钥（密钥随机个数要求，没有长度要求，速度快）
 * 各个算法：
 * rc4: 1 - 256 byte
 * des: 8 byte
 * 3des/desede/tripledes: 24 byte
 * aes: 16 /24 /32 byte aes128/192/256
 * sm4: 16
 *
 * 对称加密分类：
 * 序列加密/流加密：以字节流的方式加密每一个字节 rc4
 * 分组加密：明文分组（多个字节），按组加密 des / 3des/ aes/ sm4
 * */


/**
 * 加密模式：规定不同分组之间如何处理 cfb / ofb / ctr / gcm
 * ecb 模式：hello world ccpp 按组加密合并每组
 * cbc 模式：分组明文 进行 iv 异或 hello ^ 12345 得到的数据进行加密 在和后面的明文异或 如此反复 在进行拼接
 * 填充方式：当一个分组不满足长度数 进行填充在加密 满足一个分组长度在填充一个分组长度
 *  crypto 提供 nopadding pkcs7（pkcs5）
 *  zeropadding iso10126 iso97971 ansix923
 * */
