/*
Alice and Bob take turns playing a game, with Alice starting first.

You are given a string num of even length consisting of digits and '?' characters. On each turn, a player will do the following if there is still at least one '?' in num:

Choose an index i where num[i] == '?'.
Replace num[i] with any digit between '0' and '9'.
The game ends when there are no more '?' characters in num.

For Bob to win, the sum of the digits in the first half of num must be equal to the sum of the digits in the second half. For Alice to win, the sums must not be equal.

For example, if the game ended with num = "243801", then Bob wins because 2+4+3 = 8+0+1. If the game ended with num = "243803", then Alice wins because 2+4+3 != 8+0+3.
Assuming Alice and Bob play optimally, return true if Alice will win and false if Bob will win.

1 ?     1pw unconditionally
2 ?     1pw if score with abs > 9 is accessible
3 ?     1pw unconditionally


*/

/**
 * @param {string} num
 * @return {boolean}
 */
var sumGame = function(num) {
    // 100 %ile runtime
    // 100 %ile memory
    // (insufficient data)
    let s = State.fromPos(num, true);
    return closedSolution(s);
};

var closedSolution = function(s) {
    if ((s.numLeft + s.numRight) % 2 === 1)
        return true;
    else if (s.numLeft === s.numRight)
        return s.score !== 0;
    else if (s.numLeft === 0)
        return s.score !== 9*s.numRight / 2;
    else if (s.numRight === 0)
        return s.score !== -9*s.numLeft/2;
    else if (s.numLeft > s.numRight) {
        s.numLeft -= s.numRight;
        s.numRight = 0;
        return closedSolution(s);
    } else if (s.numLeft < s.numRight) {
        s.numRight -= s.numLeft;
        s.numLeft = 0;
        return closedSolution(s);
    }
};

function State(score, numLeft, numRight, firstPlayersMove) {
    this.numLeft = numLeft;
    this.numRight = numRight;
    this.score = score;
    this.firstPlayersMove = firstPlayersMove;
};

State.fromPos = function(pos, firstPlayersMove) {
    let left = pos.slice(0, pos.length/2);
    let right = pos.slice(pos.length/2)
    var sum = (arr) => arr.map(x => parseInt(x)).reduce((s, x) => isNaN(x) ? s : (s + x), 0);
    return new State(sum(Array.from(left)) - sum(Array.from(right)),
        left.match(/\?/g)?.length ?? 0, right.match(/\?/g)?.length ?? 0, firstPlayersMove);
};

var isFirstPlayerWin = function(state) {
    console.log(`Testing state ${JSON.stringify({score: state.score, numLeft: state.numLeft, numRight: state.numRight, firstPlayersMove: state.firstPlayersMove})}`);
    if (state.numLeft + state.numRight === 0)
        return state.score !== 0;
    if (!State.prototype.memo.hasOwnProperty(state.toString())) {
        State.prototype.memo[state.toString()] = state.firstPlayersMove
            ? Array.from(state.accessible()).some(s => isFirstPlayerWin(s))
            : Array.from(state.accessible()).every(s => isFirstPlayerWin(s));
    }
    return State.prototype.memo[state.toString()];
}

State.prototype.memo = {};

State.prototype.toString = function() {
    return String([this.score, this.numLeft, this.numRight, this.firstPlayersMove]);
};

State.prototype.accessible = function*() {
    if (this.numLeft > 0) {
        yield* [...Array(10).keys()].map(
            n => new State(this.score + n, this.numLeft - 1, this.numRight, !this.firstPlayersMove));
    }
    if (this.numRight > 0) {
        yield* [...Array(10).keys()].map(
            n => new State(this.score - n, this.numLeft, this.numRight - 1, !this.firstPlayersMove));
    }
};
