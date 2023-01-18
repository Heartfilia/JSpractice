// ==UserScript==
// @name         网洛者一题
// @namespace    http://spider.wangluozhe.com
// @version      0.1
// @description  try to take over the world!
// @author       LodgeHeartfilia
// @match        http://spider.wangluozhe.com/challenge/1
// @icon         https://www.google.com/s2/favicons?sz=64&domain=wangluozhe.com
// @grant        none
// ==/UserScript==

(function(){
    Function.prototype.constructor_ = Function.prototype.constructor;
    Function.prototype.constructor = function (a) {
        // 如果参数为 debugger，就返回空方法
        if(a == "debugger") {
            console.log("跳过了");
            return function (){};
        }
        // 如果参数不为 debugger，还是返回原方法
        return Function.prototype.constructor_(a);
    };

    // 先保留原定时器
    var setInterval_ = setInterval
    setInterval = function (func, time){
        // 如果时间参数为 0x7d0，就返回空方法
        // 当然也可以不判断，直接返回空，有很多种写法
        if(time == 0x7d0)
        {
            return function () {};
        }
        // 如果时间参数不为 0x7d0，还是返回原方法
        return setInterval_(func, time)
    }}
)();