


function AlignSHA1(str) {
    var nblk = ((str.length + 8) >> 6) + 1;
    var blks = new Array(nblk * 16);
    for (var i = 0; i < nblk * 16; i++) {
        blks[i] = 0;
    }
    for (i = 0; i < str.length; i++) {
        blks[i >> 2] |= str.charCodeAt(i) << (24 - (i & 3) * 8);
    }
    blks[i >> 2] |= 0x80 << (24 - (i & 3) * 8);
    blks[nblk * 16 - 1] = str.length * 8;
    return blks;
}


