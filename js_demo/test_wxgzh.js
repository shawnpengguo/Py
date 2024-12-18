var j;

function y(t, i) {
    var r = (t & 65535) + (i & 65535)
        , f = (t >> 16) + (i >> 16) + (r >> 16);
    return f << 16 | r & 65535
}

function D(t, i) {
    return t << i | t >>> 32 - i
}

function R(t, i, r, f, C, T) {
    return y(D(y(y(i, t), y(f, T)), C), r)
}

function k(t, i, r, f, C, T, z) {
    return R(i & r | ~i & f, t, i, C, T, z)
}

function m(t, i, r, f, C, T, z) {
    return R(i & f | r & ~f, t, i, C, T, z)
}

function p(t, i, r, f, C, T, z) {
    return R(i ^ r ^ f, t, i, C, T, z)
}

function v(t, i, r, f, C, T, z) {
    return R(r ^ (i | ~f), t, i, C, T, z)
}

function o(t, i) {
    t[i >> 5] |= 128 << i % 32;
    t[(i + 64 >>> 9 << 4) + 14] = i;
    var r, f, C, T, z, s = 1732584193, c = -271733879, g = -1732584194, n = 271733878;
    for (r = 0; r < t.length; r += 16) {
        f = s;
        C = c;
        T = g;
        z = n;
        s = k(s, c, g, n, t[r], 7, -680876936);
        n = k(n, s, c, g, t[r + 1], 12, -389564586);
        g = k(g, n, s, c, t[r + 2], 17, 606105819);
        c = k(c, g, n, s, t[r + 3], 22, -1044525330);
        s = k(s, c, g, n, t[r + 4], 7, -176418897);
        n = k(n, s, c, g, t[r + 5], 12, 1200080426);
        g = k(g, n, s, c, t[r + 6], 17, -1473231341);
        c = k(c, g, n, s, t[r + 7], 22, -45705983);
        s = k(s, c, g, n, t[r + 8], 7, 1770035416);
        n = k(n, s, c, g, t[r + 9], 12, -1958414417);
        g = k(g, n, s, c, t[r + 10], 17, -42063);
        c = k(c, g, n, s, t[r + 11], 22, -1990404162);
        s = k(s, c, g, n, t[r + 12], 7, 1804603682);
        n = k(n, s, c, g, t[r + 13], 12, -40341101);
        g = k(g, n, s, c, t[r + 14], 17, -1502002290);
        c = k(c, g, n, s, t[r + 15], 22, 1236535329);
        s = m(s, c, g, n, t[r + 1], 5, -165796510);
        n = m(n, s, c, g, t[r + 6], 9, -1069501632);
        g = m(g, n, s, c, t[r + 11], 14, 643717713);
        c = m(c, g, n, s, t[r], 20, -373897302);
        s = m(s, c, g, n, t[r + 5], 5, -701558691);
        n = m(n, s, c, g, t[r + 10], 9, 38016083);
        g = m(g, n, s, c, t[r + 15], 14, -660478335);
        c = m(c, g, n, s, t[r + 4], 20, -405537848);
        s = m(s, c, g, n, t[r + 9], 5, 568446438);
        n = m(n, s, c, g, t[r + 14], 9, -1019803690);
        g = m(g, n, s, c, t[r + 3], 14, -187363961);
        c = m(c, g, n, s, t[r + 8], 20, 1163531501);
        s = m(s, c, g, n, t[r + 13], 5, -1444681467);
        n = m(n, s, c, g, t[r + 2], 9, -51403784);
        g = m(g, n, s, c, t[r + 7], 14, 1735328473);
        c = m(c, g, n, s, t[r + 12], 20, -1926607734);
        s = p(s, c, g, n, t[r + 5], 4, -378558);
        n = p(n, s, c, g, t[r + 8], 11, -2022574463);
        g = p(g, n, s, c, t[r + 11], 16, 1839030562);
        c = p(c, g, n, s, t[r + 14], 23, -35309556);
        s = p(s, c, g, n, t[r + 1], 4, -1530992060);
        n = p(n, s, c, g, t[r + 4], 11, 1272893353);
        g = p(g, n, s, c, t[r + 7], 16, -155497632);
        c = p(c, g, n, s, t[r + 10], 23, -1094730640);
        s = p(s, c, g, n, t[r + 13], 4, 681279174);
        n = p(n, s, c, g, t[r], 11, -358537222);
        g = p(g, n, s, c, t[r + 3], 16, -722521979);
        c = p(c, g, n, s, t[r + 6], 23, 76029189);
        s = p(s, c, g, n, t[r + 9], 4, -640364487);
        n = p(n, s, c, g, t[r + 12], 11, -421815835);
        g = p(g, n, s, c, t[r + 15], 16, 530742520);
        c = p(c, g, n, s, t[r + 2], 23, -995338651);
        s = v(s, c, g, n, t[r], 6, -198630844);
        n = v(n, s, c, g, t[r + 7], 10, 1126891415);
        g = v(g, n, s, c, t[r + 14], 15, -1416354905);
        c = v(c, g, n, s, t[r + 5], 21, -57434055);
        s = v(s, c, g, n, t[r + 12], 6, 1700485571);
        n = v(n, s, c, g, t[r + 3], 10, -1894986606);
        g = v(g, n, s, c, t[r + 10], 15, -1051523);
        c = v(c, g, n, s, t[r + 1], 21, -2054922799);
        s = v(s, c, g, n, t[r + 8], 6, 1873313359);
        n = v(n, s, c, g, t[r + 15], 10, -30611744);
        g = v(g, n, s, c, t[r + 6], 15, -1560198380);
        c = v(c, g, n, s, t[r + 13], 21, 1309151649);
        s = v(s, c, g, n, t[r + 4], 6, -145523070);
        n = v(n, s, c, g, t[r + 11], 10, -1120210379);
        g = v(g, n, s, c, t[r + 2], 15, 718787259);
        c = v(c, g, n, s, t[r + 9], 21, -343485551);
        s = y(s, f);
        c = y(c, C);
        g = y(g, T);
        n = y(n, z)
    }
    return [s, c, g, n]
}

function u(t) {
    var i, r = "";
    for (i = 0; i < t.length * 32; i += 8) {
        r += String.fromCharCode(t[i >> 5] >>> i % 32 & 255)
    }
    return r
}

function b(t) {
    var i, r = [];
    r[(t.length >> 2) - 1] = void 0;
    for (i = 0; i < r.length; i += 1) {
        r[i] = 0
    }
    for (i = 0; i < t.length * 8; i += 8) {
        r[i >> 5] |= (t.charCodeAt(i / 8) & 255) << i % 32
    }
    return r
}

function O(t) {
    return u(o(b(t), t.length * 8))
}

function h(t, i) {
    var r, f = b(t), C = [], T = [], z;
    C[15] = T[15] = void 0;
    if (f.length > 16) {
        f = o(f, t.length * 8)
    }
    for (r = 0; r < 16; r += 1) {
        C[r] = f[r] ^ 909522486;
        T[r] = f[r] ^ 1549556828
    }
    z = o(C.concat(b(i)), 512 + i.length * 8);
    return u(o(T.concat(z), 512 + 128))
}

function _(t) {
    var i = "0123456789abcdef", r = "", f, C;
    for (C = 0; C < t.length; C += 1) {
        f = t.charCodeAt(C);
        r += i.charAt(f >>> 4 & 15) + i.charAt(f & 15)
    }
    return r
}

function E(t) {
    return unescape(encodeURIComponent(t))
}

function I(t) {
    return O(E(t))
}

function P(t) {
    return _(I(t))
}

function B(t, i) {
    return h(E(t), E(i))
}

function d(t, i) {
    return _(B(t, i))
}

function md5(t, i, r) {
    if (!i) {
        if (!r) {
            return P(t)
        } else {
            return I(t)
        }
    }
    if (!r) {
        return d(i, t)
    } else {
        return B(i, t)
    }
}

console.log(md5('12345678'))