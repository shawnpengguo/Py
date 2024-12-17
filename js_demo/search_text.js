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













