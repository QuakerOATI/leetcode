/**
 * @param {number[][]} buildings
 * @return {number[][]}
 */
var getSkyline = function (buildings) {
  let q = new PQueue(x => x[0]);
  buildings.forEach(b => { q.insert([b[0], b[2]]); q.insert([b[1], -b[2]]); });
  let counter = {};
  let heights = new PQueue(x => -x);
  let points = [];
  let top = function () {
    while (heights.length && !counter[heights.peek()])
      heights.removeMin();
    return heights.length ? heights.peek() : 0;
  }
  while (q.length) {
    let x = q.peek()[0];
    // console.log(`Handling points with x-coordinate ${x}`);
    let t = top();
    // console.log(`Top at beginning of loop: ${top}`);
    while (q.length && q.peek()[0] === x) {
      // console.log(`  ${q.peek()}`);
      let y = q.removeMin()[1];
      if (y > 0) {
        if (!counter[y]) {
          // console.log(`    New height: ${y} (numHeights = ${heights.length})`);
          counter[y] = 1;
          heights.insert(y);
        } else {
          counter[y]++;
          // console.log(`    Height ${y} occurs with multiplicity ${counter[y]} after incrementing`);
        }
      } else if (y < 0) {
        counter[-y]--;
        // console.log(`    Height ${-y} occurs with multiplicity ${counter[-y]} after decrementing`);
      }
    }
    if (t !== top()) {
      // console.log(`Height discrepancy, adding point ${[x, top()]}`);
      points.push([x, top()]);
    }
  }
  return points;
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
      // console.log(this.removeMin());
    }
  }
}
