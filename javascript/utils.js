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
    let ret = this.val.toString();
    let loop = false;
    let numNodes = 0;
    while (curr && !loop && numNodes < LinkedList.MAX_PRINTED_ELEMS) {
      curr = curr?.next;
      if (!curr)
        break;
      if (seen.has(curr)) {
        loop = true;
      } else {
        seen.add(curr);
        ret += ` -> ${curr?.val}`;
      }
      numNodes += 1;
    }
    if (loop) {
      ret += ` -> ( ${curr?.val}`;
      for (let n = curr?.next; !n || n !== curr; n = n?.next) {
        ret += ` -> ${n?.val}`;
      }
      ret += " )*";
    }
    if (numNodes >= LinkedList.MAX_PRINTED_ELEMS) {
      ret += "..."
    }
    return ret
  }
}

class SortedArray {
    constructor(arr) {
        this.array = [...arr].sort((x, y) => x-y);
    }
    insert(elem) {
        let idx = this.getIndex(elem);
        this.array = [...this.array.slice(0, idx), elem, ...this.array.slice(idx)];
    }
    remove(elem) {
        let idx = this.getIndex(elem);
        if (this.array[idx] == elem) {
            this.array = [...this.array.slice(0, idx), ...this.array.slice(idx+1)];
        }
    }
    getIndex(elem) {
        if (this.length == 0) {
            return 0;
        } else if (this.length == 1) {
            return elem > this.array[1] ? 2 : (elem > this.array[0] ? 1 : 0);
        } else if (elem <= this.array[0]) {
            return 0;
        } else if (elem >= this.array.at(-1)) {
            return elem===this.array.at(-1) ? this.length-1 : this.length;
        }
        let [l, m, r] = [0, Math.floor(this.length/2), this.length-1];
        while (r-l > 1) {
            if (elem < this.array[m]) {
                r = m;
            } else if (elem > this.array[m]) {
                l = m;
            } else {
                while ((m > 0) && elem===this.array[--m]) {}
                return m+1;
            }
            m = Math.floor((l+r)/2);
        }
        if (this.array[l]<elem && elem<this.array[r]) {
            return l+1;
        } else if (elem<=this.array[l]) {
            while ((l > 0) && elem == this.array[--l]) {}
            return l+1;
        } else if (elem>=this.array[r]) {
            while ((r < this.length) && elem == this.array[++r]) {}
            return elem===this.array[r-1] ? r-1 : r;
        }
        console.log(`Error while finding index for ${elem}.  l = ${l}, r = ${r}, m = ${m}`);
    }
    pop() { return this.array.pop(); }
    peek() { return this.array.at(-1); }
    get length() { return this.array.length; }
}

return { range, randInt, randArr, ListNode, LinkedList, SortedArray };

