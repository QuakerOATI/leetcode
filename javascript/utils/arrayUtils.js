var range = (l, r) => [...Array(r - l + 1).keys()].map(x => x + l);
var randInt = (l, r) => Math.floor(Math.random() * (r - l) + l);
var randArr = (size, minElem, maxElem) => [...Array(size).keys()].map(_ => randInt(minElem, maxElem));

return { range, randInt, randArr };
