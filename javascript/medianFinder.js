var MedianFinder = function(debug=false) {
    this.debug = debug;
    this.left =[];
    this.right = [];
    this.median = undefined;
    this.length = 0;
    this.cmpLeft = (x, y) => y - x;
    this.cmpRight = (x, y) => x - y;
};

/** 
 * @param {number} num
 * @return {void}
 */
MedianFinder.prototype.addNum = function(num) {
    this.printState("addNum:begin");
    if (this.length === 0 || this.median === undefined) {
        this.median = num;
    } else if (num <= this.median) {
        heappush(this.left, num, this.cmpLeft);
        if (this.length % 2 === 1) {
            heappush(this.right, Math.floor(this.median), this.cmpRight);
            this.median = (this.left[0] + this.right[0])/2;
        } else {
            this.median = heappop(this.left, this.cmpLeft);
        }
    } else if (num > this.median) {
        heappush(this.right, num, this.cmpRight);
        if (this.length % 2 === 1) {
            heappush(this.left, Math.floor(this.median), this.cmpLeft);
            this.median = (this.right[0] + this.left[0])/2;
        } else {
            this.median = heappop(this.right, this.cmpRight);
        }
    }
    this.length++;
    this.printState("addNum:end");
};

MedianFinder.prototype.printState = function(header, ...msgs) {
    if (this.debug) {
        console.log(`${header}:\n\tleft = [${this.left.join(", ")}]\n\tright = [${this.right.join(", ")}]`);
        console.log(`\tmedian = ${this.median}`);
        console.log(`\tlength = ${this.length}`);
        for (msg of msgs)
            console.log(`\t${msg}`);
    }
};

/**
 * @return {number}
 */
MedianFinder.prototype.findMedian = function() {
    return this.median;    
};

/** 
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */

upheap = function(arr, cmp) {
    if (!arr || !arr.length)
        return;
    let pos = arr.length - 1;
    for (let par=Math.floor((pos-1)/2); cmp(arr[pos], arr[par]) < 0; [pos, par]=[par, Math.floor((par-1)/2)]) {
        [arr[pos], arr[par]] = [arr[par], arr[pos]];
    }
    return pos;
};

const downheap = function(arr, pos, cmp) {
    if (!arr || !arr.length)
        return;
    let cs = [2*pos+1, 2*pos+2].filter(x => arr[x]).sort((x, y) => cmp(arr[x], arr[y]));
    while (cs.length && cmp(arr[cs[0]], arr[pos]) < 0) {
        [arr[cs[0]], arr[pos]] = [arr[pos], arr[cs[0]]];
        pos = cs[0];
        cs = [2*pos+1, 2*pos+2].filter(x => arr[x]).sort((x, y) => cmp(arr[x], arr[y]));
    }
};

const heappush = function(arr, elem, cmp) {
    if (!arr.length)
        return arr.push(elem);
    arr.push(elem);
    let pos = upheap(arr, cmp);
    downheap(arr, pos, cmp);
};

const heappop = function(arr, cmp) {
    if (!arr?.length)
        return;
    if (arr.length === 1)
        return arr.pop();
    [arr[0], arr[arr.length-1]] = [arr[arr.length-1], arr[0]];
    var ret = arr.pop();
    downheap(arr, 0, cmp);
    return ret;
};

const median = (arr) => {
    if (!arr?.length)
        return undefined;
    if (arr.length === 1)
        return arr[0];
    let sorted = [...arr];
    sorted.sort((x, y) => x-y);
    let L = sorted.length;
    if (L % 2 === 0)
        return (sorted[(L/2) - 1] + sorted[L/2])/2;
    else
        return sorted[(L-1)/2];
};

var getTestcase = (size=1000, upper=1000, lower=-1000) => {
    var nums = [...Array(size).keys()].map(x => Math.floor(lower + (upper-lower)*Math.random()));
    return {nums, expected: median(nums)};
}


var testMedianFinder = function(size=1000, upper=1000) {
    var mf = new MedianFinder();
    let {nums, expected} =  getTestcase(size, upper);
    for (let num of nums)
        mf.addNum(num);
    let returned = mf.median;
    console.log(`Expected: median = ${expected}`);
    console.log(`Returned: median = ${returned}`);
    if (expected === returned)
        console.log("PASS");
    else {
        mf.debug = true;
        mf.printState("FAIL");
    }
    return nums;
};

var findCountertests = function(maxTests=1000, size=1000, upper=1000, lower=-1000) {
    MedianFinder.prototype.countertests = MedianFinder.prototype.countertests ?? [];
    for (let i=0; i<maxTests; ++i) {
        let mf = new MedianFinder();
        let {nums, expected} = getTestcase(size, upper);
        for (let num of nums)
            mf.addNum(num);
        if (mf.median !== expected) {
            MedianFinder.prototype.countertests.push({nums, expected});
            mf.debug = true;
            mf.printState(`Countertest found after ${i+1} tests!`, `Expected median to be ${expected}`);
            try {
                testHeapState(mf.left, mf.cmpLeft);
                testHeapState(mf.right, mf.cmpRight);
            } catch (exc) {
                console.error(exc);
            }
        }
    }
}


var testHeapState = function(arr, cmp) {
    if (!arr?.length)
        return;
    for (let i=0; i<arr.length; ++i) {
        [2*i+1, 2*i+2].forEach(x => {
            if (arr[x] && cmp(arr[x], arr[i]) < 0)
                throw new Error(`Heap property violation:\n\tarr[${i}] = ${arr[i]}\n\tarr[${x}] = ${arr[x]}`);
        });
    }
}
