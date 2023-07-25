var countAndSay = function(n) {
    let counted = 0;
    let c = counter();
    c.history.push(1);
    for (let i=1; i<n; ++i) {
        c.flushHistory().forEach(n => c.push(n));
    }
    return c.flushHistory().join("");
};

var counter = function() {
    return {
        history: [],
        currentNum: null,
        currentCt: 0,
        push: function(x) {
            this.currentNum = this.currentNum ?? x;
            if (x===this.currentNum) {
                this.currentCt++;
            } else {
                this.archive();
                this.currentNum = x;
                this.currentCt = 1;
            }
        },
        archive: function() {
            if (this.currentNum)
                this.history.push(this.currentCt, this.currentNum);
            this.currentNum = null;
            this.currentCt = 0;
        },
        flushHistory: function() {
            this.archive();
            h = this.history;
            this.history = [];
            return h;
        },
        length: function() {
            return this.history.length + (this.currentNum ? 2 : 0);
        }
    };
};

