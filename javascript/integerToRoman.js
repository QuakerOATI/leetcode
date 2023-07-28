/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    let ans = [];
    while (num) {
        let next = Math.max(...Object.keys(numerals).filter(n => n <= num));
        if (num/next >= 4) {
            s += numerals
        } else {
            s += numerals[next];
    
};

const numerals = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}
