/**
 * 搜索关键词 码表 各种算法的初始化常量 k表 s盒的值
 *
 * xhr断点 + callstack 根据堆栈排查 比较多的stack特别是promise可以跳着看
 *
 * initiator + callstack 控制台帮忙记录发送时的堆栈
 *
 * 事件断点 dom 全局
 *
 * debugger 条件断点
 *
 * js hook
 * */

// 条件断点实例 想在某种条件断下
for (let i = 0; i <100; i++) {
    // console.log(i)
}

/**
 * 下面这种写法 不适应 局部
 * hook 全局变量 方法 global很适合hook
 * */
function test(c) {
    var a = 100
    var b = 200
    return a + b + c
}

var _test = test
test = function (c) {
    console.log(c)
    var tmp = _test(c)
    console.log(tmp)
    return tmp
}

test(100)

// hook suning draw
// const _drawimage = CanvasRenderingContext2D.prototype.drawImage;
// CanvasRenderingContext2D.prototype.drawImage = function CanvasRenderingContext2D(...arg) {
//     console.log(arg);
//     return _drawImage.call(this, ...arg);
// }

/**
 * 复习一下 网页逆向（扣代码，补环境）
 * 简略看一下头也没有可疑的地方 在看网络堆栈有没有栈信息 看一下 type 是不是form类型提交
 * 没有就搜索关键字，尽量代码原封不动扣下来，进行方法的补充或者修改
 * 注意全局事件是不是有
 * 记得后续补充一下 js 的学习或者提升（特别是原型链 异步 很重要！！！，很多方法的 hook 都需要在原型进行改动～）
 * 12/19 今天复习回顾一下
 * */

/**
 * 12/20
 * 偷懒一下 明天在看 嘻嘻～
 * 随便有空在复习一下～
 * */

/**
 * todo
 * 12/21
 * 今天继续偷懒一下
 * 家里有事
 * */










