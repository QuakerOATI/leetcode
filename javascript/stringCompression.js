var compressPure = function(chars) {
    let [L, z, ret] = chars.reduce(([last, ct, ret], ch) => {
        if (ch===last) {
            return [last, ++ct, ret];
        } else {
            if (last) {
                ret.push(last)
                ct.toString().split("").forEach(c => ret.push(c));
            }
            return [ch, 1, ret];
        }
    }, [null, 0, []]);
    ret.push(L);
    z.toString().split("").forEach(c => ret.push(c));
    return ret;
}

var compress = function(chars) {
    let ct;
    let x;
    let i=-1;
    while (++i<chars.length) {
        x = chars[i];
        ct = 0;
        for (; i+ct<chars.length && chars[i+ct]===x; ++ct) {}
//        console.log(`Count: ${x} --> ${ct}`);
        if (ct > 1) {
            let ctChars = ct.toString().split("");
            ctChars.forEach((c, j) => {chars[i+j+1] = c;});
//            console.log(`       pre-splice: ${chars}`);
            chars.splice(i + ctChars.length + 1, ct - 1 - ctChars.length);
            i += ctChars.length;
        }
//        console.log(`   ${chars}`);
    }
    return chars.length;
}
