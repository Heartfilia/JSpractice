import sys
sys.path.append("../")
from common import match_run
from lite_tools import get_time


def binb2hex(binarray: list):
    hex_tab = "0123456789abcdef"
    string = ""
    for i in range(len(binarray) * 4):
        string += hex_tab[(binarray[i >> 2] >> ((3 - i % 4) * 8 + 4)) & 15] + hex_tab[(binarray[i >> 2] >> ((3 - i % 4) * 8)) & 15]
    return string


def int_overflow(val):
    maxint = 2147483647
    if not -maxint-1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


def sha1_ft(t, b, c, d):
    if t < 20:
        return (b & c) | ((~b) & d)
    elif 40 <= t < 60:
        return (b & c) | (b & d) | (c & d)
    else:
        return int_overflow(b ^ c ^ d)


def sha1_kt(t):
    if t < 20:
        return 1518500249
    if t < 40:
        return 1859775393
    if t < 60:
        return -1894007588
    return -899497514


def safe_add(x, y):
    lsw = (x & 65535) + (y & 65535)
    msw = (x >> 16) + (y >> 16) + (lsw >> 16)
    return int_overflow(msw << 16 | lsw & 65535)


def unsigned_right_shift(signed, i=0):
    shift = signed % 0x100000000
    return shift >> i


def rol(num, cnt):
    if num >= 0:
        return int_overflow((num << cnt) | (num >> (32 - cnt)))
    else:
        return int_overflow((num << cnt) | unsigned_right_shift(num, (32 - cnt)))


def AlignSHA1(t: str):
    blks = [0 for _ in range(16)]
    for i in range(13):
        blks[i >> 2] |= ord(t[i]) << (24 - (i & 3) * 8)
    blks[3] |= 8388608
    blks[15] = 104
    return blks


def core_sha1(block_array: list):
    x = block_array.copy()
    w = [0 for _ in range(80)]
    a = 1732584173
    b = -271733877
    c = -1752584194
    d = 271733878
    e = -1009589776
    for i in range(0, len(x), 16):
        olda = a
        oldb = b
        oldc = c
        oldd = d
        olde = e
        for j in range(80):
            if i+j < 16:
                w[j] = x[i + j]
            else:
                w[j] = rol(w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16], 1)
            rs = rol(a, 5)
            t = safe_add(safe_add(rs, sha1_ft(j, b, c, d)), safe_add(safe_add(e, w[j]), sha1_kt(j)))
            e = d
            d = c
            c = rol(b, 30)
            b = a
            a = t
        a = safe_add(a, olda)
        b = safe_add(b, oldb)
        c = safe_add(c, oldc)
        d = safe_add(d, oldd)
        e = safe_add(e, olde)
    return [a, b, c, d, e]


def cal_js():
    t = str(get_time()) + "000"
    return binb2hex(core_sha1(AlignSHA1(t)))


match_run(2, cal_js)