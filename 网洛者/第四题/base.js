const CryptoJS = require("crypto-js");


function aes(word) {
    let date = Date.parse(new Date())
    let key_tmp = date * 1234;  // 1244
    let iv_tmp = date * 4311;  // 4321
    const key = CryptoJS.enc.Utf8.parse(key_tmp);
    var iv = CryptoJS.enc.Utf8.parse(iv_tmp);
    let srcs = CryptoJS.enc.Utf8.parse(word);
    let encrypted = CryptoJS.AES.encrypt(srcs, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return encrypted.ciphertext.toString().toUpperCase();
}


// console.log(aes("1568489765000"))