// ==UserScript==
// @name         网洛者第六题
// @namespace    http://spider.wangluozhe.com/challenge/6
// @version      0.1
// @description  try to take over the world!
// @author       Lodge
// @match        http://spider.wangluozhe.com/challenge/6
// @icon         https://www.google.com/s2/favicons?sz=64&domain=wangluozhe.com
// @grant        none
// ==/UserScript==

(function () {
    'use strict';
    var org = window.XMLHttpRequest.prototype.setRequestHeader;
    window.XMLHttpRequest.prototype.setRequestHeader = function (key, value) {
        if (key == 'hexin-v') {
            debugger;
        }
        return org.apply(this, arguments);
    };
})();