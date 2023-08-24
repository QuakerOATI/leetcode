/*
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
*/

/**
 * @param {string[]} words
 * @param {number} maxWidth
 * @return {string[]}
 */
var fullJustify = function(words, maxWidth) {
    let lines = [];
    let lstart = 0, llen = 0;
    for (let i = 0; i < words.length; ++i) {
        llen += words[i].length;
        if (llen + i - lstart > maxWidth) {
            let extra = maxWidth - llen + words[i].length;
            if (i - lstart === 1)
                lines.push(words[lstart].padEnd(maxWidth, " "));
            else {
                let numS = i - lstart - 1;
                let s = Math.floor(extra/numS);
                for (let j = 0; j < extra % numS; ++j) {
                    words[lstart + j] += " ";
                }
                lines.push(words.slice(lstart, i).join(" ".repeat(s)));
            }
            lstart = i;
            llen = words[i].length;
        }
    }
    lines.push(words.slice(lstart).join(" ").padEnd(maxWidth, " "));
    return lines;
};
