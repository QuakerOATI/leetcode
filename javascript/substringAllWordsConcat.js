/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */

// 100 %ile runtime, 98.4 %ile memory (!)
// Most other solutions used a Map instead of the Counter class I wrote, which probably accounts for the extra overhead they incurred
var findSubstring = function (s, words) {
  var L = words[0].length;
  var ret = [];
  var W = new Counter(words);
  var S = new Counter(words);
  for (let i = 0; i < L; ++i) {
    //console.log(`------------Considering strings at offset i = ${i}-------------`)
    S.clear();
    let start = i;
    for (let j = i; j + L - 1 < s.length; j += L) {
      let w = s.slice(j, j + L);
      //console.log(`Considering substring ${w}...`)
      if (W.has(w)) {
        if (!S.total)
          start = j;
        S.add(w);
        while (S.get(w) > W.get(w)) {
          S.remove(s.slice(start, start + L));
          start += L;
        }
        //console.log(`Word ${w} is in words\n\tWords in pending concatenated substring: [${[...S].join(", ")}]`);
        if (S.total == W.total) {
          //console.log(`Found a new concatenated substring at index ${start}`);
          //console.log(` S = [${[...S].join(", ")}]`)
          ret.push(start);
          S.remove(s.slice(start, start + L));
          start += L;
        }
      }
      else {
        //console.log(`${w} not found in words\n\tClearing S = [${[...S].join(", ")}]`);
        S.clear();
      }
    }
  }
  return ret;
};

var Counter = function (it) {
  this.total = 0;
  this.items = {};
  it.forEach(x => this.add(x));
}

Counter.prototype.add = function (elem) {
  if (this.items.hasOwnProperty(elem))
    this.items[elem]++;
  else
    this.items[elem] = 1;
  this.total++;
}

Counter.prototype.remove = function (key) {
  if (this.items[key] && this.items[key] > 0) {
    this.items[key]--;
    this.total--;
  }
}

Counter.prototype.has = function (key) {
  return this.items.hasOwnProperty(key);
}

Counter.prototype.get = function (key) {
  return this.items[key] ?? 0;
}

Counter.prototype.clear = function () {
  this.items = {};
  this.total = 0;
}
