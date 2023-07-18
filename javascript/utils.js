var range = (l, r) => [...Array(r - l + 1).keys()].map(x => x + l);
var randInt = (l, r) => Math.floor(Math.random() * (r - l) + l);
var randArr = (size, minElem, maxElem) => [...Array(size).keys()].map(_ => randInt(minElem, maxElem));
var ListNode = (val, next) => { return { val: val, next: next }; };

class LinkedList {
  static MAX_PRINTED_ELEMS = 50;
  static fromArray(arr) {
    return arr.reduceRight((head, val) => new LinkedList(val, head), null);
  }
  static getRandom(N, minElem, maxElem) {
    return LinkedList.fromArray(randArr(N, minElem, maxElem));
  }
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
  toString() {
    let seen = new Set();
    let curr = this;
    let ret = "";
    let loop = false;
    let numNodes = 0;
    while (curr && !loop && numNodes < this.MAX_PRINTED_ELEMS) {
      curr = curr?.next;
      if (seen.has(curr)) {
        loop = true;
      } else {
        seen.add(curr);
        ret += ` -> ${curr.val}`;
      }
      numNodes += 1;
    }
    if (loop) {
      ret += ` -> ( ${curr.val}`;
      for (let n = curr.next; n !== curr; n = n.next) {
        ret += ` -> ${n.val}`;
      }
      ret += " )*";
    }
    if (numNodes >= MAX_PRINTED_ELEMS) {
      ret += "..."
    }
    return ret
  }
}

export { range, randInt, randArr, ListNode, LinkedList };
