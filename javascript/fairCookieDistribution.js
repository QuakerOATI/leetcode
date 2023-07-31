/**
 * @param {number[]} cookies
 * @param {number} k
 * @return {number}
 */
var distributeCookies = function(cookies, k) {
    cookies.sort((x, y) => y - x);
    if (k === 1)
        return cookies.reduce((S, c) => S + c, 0);
    let q = new Heap(Array(k).fill(0), (x, y) => x - y);
    console.log(`Apportioning cookies [${cookies}] among ${k} children`);
    for (c of cookies) {
        console.log(`Heap state:\n\tPre-allotment: [${q.arr}]`);
        q.insert(c + q.removeMin());
        console.log(`\tPost-allotment: [${q.arr}]`);
    }
    return Math.max(...q.arr);
};

// Note: doesn't heapify on construction
function Heap(l, cmp) {
    this.arr = l;
    this.cmp = cmp;
}

Heap.prototype.upheap = function(idx) {
    for (let p=Math.floor((idx-1)/2); p>=0 && this.cmp(this.arr[p], this.arr[idx]) > 0; [idx, p] = [p, Math.floor((p-1)/2)]) {
        [this.arr[p], this.arr[idx]] = [this.arr[idx], this.arr[p]];
    }
    return idx;
}

Heap.prototype.minChild = function(idx) {
    return [2*idx+1, 2*idx+2].filter(x => x<this.arr.length).sort((i, j) => this.cmp(this.arr[i], this.arr[j]))[0];
}

Heap.prototype.downheap = function(idx) {
    for (let c=this.minChild(idx); c && this.cmp(this.arr[c], this.arr[idx]) < 0; [idx, c] = [c, this.minChild(c)]) {
        [this.arr[c], this.arr[idx]] = [this.arr[idx], this.arr[c]];
    }
}

Heap.prototype.insert = function(x) {
    this.arr.push(x);
    let i = this.upheap(this.arr.length-1);
    this.downheap(i);
}

Heap.prototype.removeMin = function() {
    [this.arr[0], this.arr[this.arr.length-1]] = [this.arr[this.arr.length-1], this.arr[0]];
    let ret = this.arr.pop();
    this.downheap(0);
    return ret;
}
