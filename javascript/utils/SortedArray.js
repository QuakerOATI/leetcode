export default class SortedArray {
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

