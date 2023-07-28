const upToTwenty = [
    null,
    'One',
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'Ten',
    'Eleven',
    'Twelve',
    'Thirteen',
    'Fourteen',
    'Fifteen',
    'Sixteen',
    'Seventeen',
    'Eighteen',
    'Nineteen',
];

const decades = [
    null,
    'Ten',
    'Twenty',
    'Thirty',
    'Forty',
    'Fifty',
    'Sixty',
    'Seventy',
    'Eighty',
    'Ninety'
]

const powersOfTen = [
    null,
    "Thousand",
    "Million",
    "Billion",
    "Trillion"
]

var digitGroups = function*(num) {
    let i=0;
    for (let grp=(num % 1000); num; [grp, i] = [(num % 1000), i+1]) {
        yield [grp, i];
        num = Math.floor(num/1000);
    }
}

// Accepted, and JS-optimal at 35ms
var numberToWords = function(num) {
    if (num === 0)
        return "Zero";
    let grps = [];
    for (let [grp, pow] of digitGroups(num)) {
        if (grp === 0)
            continue;
        let g = [];
        let t = grp % 100;
        let h = (grp - t)/100;
        if (h) {
            g.push(upToTwenty[h]);
            g.push("Hundred");
        }
        if (t >= 20) {
            let o = t % 10;
            g.push(decades[(t-o)/10]);
            if (o > 0) g.push(upToTwenty[o]);
        } else if (t > 0) {
            g.push(upToTwenty[t]);
        }
        if (pow > 0)
            g.push(powersOfTen[pow]);
        grps.push(g);
    }
    return grps.reverse().flat().join(" ");
}
