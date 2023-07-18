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
  if (!lists.length) {
    return null;  // null represents empty linked list
  }
  let q = new PQueue(x => x.val);
  let dummy = { next: null };
  let tail = dummy;
  lists.filter(x => x).forEach(l => { q.insert(l); });
  while (q.length) {
    tail.next = q.removeMin();
    tail = tail.next;
    if (tail.next)
      q.insert(tail.next);
  }
  return dummy.next;
}


var randomTestcase = function (numLists = 50, maxSize = 100, maxElem = 1000) {
  let comp = (x, y) => parseInt(x) - parseInt(y);
  arrs = range(1, numLists).map(_ => randArr(randInt(1, maxSize), -maxElem, maxElem).sort(comp));
  ans = arrs.reduce((tot, arr) => tot.concat(arr), []).sort(comp);
  lists = arrs.map(LinkedList.fromArray);
  return { args: lists, sorted: ans };
};

var doTestcase = function (tc) {
  console.time("testcase");
  let ll = mergeKLists(tc.args);
  let curr = ll;
  console.timeEnd("testcase");
  for (let idx = 0; idx < tc.sorted.length; idx++) {
    if (!curr) {
      console.log(`Dude, your linked list ended at index ${idx} out of ${tc.sorted.length - 1}`);
      console.log(ll.toString())
      console.log(tc.sorted)
      return false;
    }
    if (curr.val !== tc.sorted[idx]) {
      console.log(`Oh noes, failed at index ${idx}`);
      console.log(`            curr.val = ${curr.val}`);
      console.log(`    tc.sorted[idx] = ${tc.sorted[idx]}`);
      console.log(ll.toString())
      console.log(tc.sorted)
      return false;
    }
    curr = curr.next;
  }
  return true;
}

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
      if (children.length && this.keyfunc(val) > this.keyfunc(children[0][1])) {
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
