import { range, LinkedList, LinkedListNode, randArr, randInt } from './utils.js';

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {
  q = new PQueue(x => x.val);
  while (lists.length) {
    lists.filter(l => l)
    lists.forEach(l => {
      q.insert(l);
      l = l?.next;
    })
  }
};

var randomTestcase = function (numLists = 50, maxSize = 100, maxElem = 1000) {
  arrs = range(1, numLists).map(_ => randArr(randInt(1, maxSize), -maxElem, maxElem).sort());
  ans = arrs.reduce((tot, arr) => tot.concat(arr), []).sort();
  lists = arrs.map(LinkedList.fromArray);
  return { args: lists, sorted: ans };
};

class PQueue {
  static id = (x) => x;
  constructor(keyfunc = PQueue.id) {
    this.keyfunc = keyfunc;
    this._items = [];
  }
  get length() {
    return this._items.length;
  }
  peek() {
    return this._items.length ? this._items[0] : undefined;
  }
  upheap(idx) {
    if (idx <= 0)
      return;
    let p = Math.floor((idx - 1) / 2);
    let val = this._items[idx];
    while (idx > 0 && this.keyfunc(val) < this.keyfunc(this._items[p])) {
      this._items[idx] = this._items[p];
      this._items[idx = p] = val;
      p = Math.floor((idx - 1) / 2);
    }
  }
  downheap(idx) {
    if (idx >= this._items.length || this._items.length < 2)
      return;
    let val = this._items[idx];
    let children;
    while (true) {
      children = [2 * idx + 1, 2 * idx + 2]
        .map(j => j >= this._items.length ? undefined : [j, this._items[j]])
        .filter(x => x !== undefined)
        .sort((x, y) => this.keyfunc(x[1]) - this.keyfunc(y[1]));
      if (children.length && val > children[0][1]) {
        this._items[idx] = children[0][1];
        this._items[idx = children[0][0]] = val;
      } else {
        break;
      }
    }
  }
  insert(item) {
    this._items.push(item);
    this.upheap(this._items.length - 1);
    this.downheap(0);
  }
  removeMin() {
    if (this._items.length === 0) {
      return undefined;
    } else if (this._items.length === 1) {
      return this._items.pop();
    }
    let min = this._items[0];
    this._items[0] = this._items.pop();
    this.downheap(0);
    return min;
  }
  dump() {
    while (this.length) {
      console.log(this.removeMin());
    }
  }
}
