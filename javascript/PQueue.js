class PQueue {
  constructor() {
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
    while (idx > 0 && val < this._items[p]) {
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
        .sort((x, y) => x[1] - y[1]);
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

export { PQueue };
