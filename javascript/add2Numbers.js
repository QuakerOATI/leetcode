/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

// 93.96 %ile runtime, 19.44 %ile memory
var addTwoNumbers = function(l1, l2) {
    var propagateCarry = function(node, carry) {
        if (!carry) return;
        node.val += 1;
        for (carry=node.val >= 10; carry; carry=node.val>=10) {
            node.val %= 10;
            node.next = node.next ?? new ListNode(0, null);
            node = node.next;
            node.val += 1;
        }
    }
            
    let carry = false;
    let dummy = new ListNode(null, l2);
    let prev;

    for (prev=dummy; l1 && l2; [l1, l2, prev] = [l1?.next, l2?.next, l2]) {
        l2.val += l1.val + (carry ? 1 : 0);
        carry = l2.val >= 10;
        l2.val %= 10;
    }

    if (!l1 && !l2 && carry && prev.next !== dummy.next) {
        prev.next = new ListNode(1, null);
    } else if (!l1) {
        propagateCarry(l2, carry);
    } else if (!l2) {
        prev.next = l1;
        propagateCarry(l1, carry);
    }

    return dummy.next;
};

var addTwoNumsTest = function(num1, num2, notifySuccess=true, notifyFail=true) {
    let log = (msg, pred) => { if (pred) console.log(msg); }
    let expect = num1 + num2;
    [n1, n2] = [num1, num2].map(listFromNum);
    let [s1, s2] = [n1, n2].map(x => x.toString()).sort((x, y) => x.length - y.length);
    let ret = addTwoNumbers(n1, n2);
    let success = expect === numFromList(ret);
    if ((!success && notifyFail) || (success && notifySuccess)) {
        log(`Adding ${num1} and ${num2} as linked lists:\n`, );
        log(`      ${s1}\n   +  ${s2}`);
        log("   ---" + ret.toString().replaceAll(/./g, '-'));
        log(`      ${ret.toString()} --> ${numFromList(ret)}\n`);
        log(`${expect === numFromList(ret) ? "PASS" : "FAIL"}: ${num1} + ${num2} = ${expect}`);
    }
    return success;
}

var findCountertest = function(min, max, numTests) {
    ListNode.prototype.countertests = ListNode.prototype.countertests ?? [];
    let i;
    for (i=0; i<numTests; ++i) {
        let [a, b] = [0, 0].map(x => Math.floor((max-min)*Math.random()) + min);
        success = addTwoNumsTest(a, b, notifySuccess=false, notifyFail=true);
        if (!success) {
            console.log(`Found countertest after ${i+1} rounds`);
            ListNode.prototype.countertests.push([a, b]);
        }
    }
    console.log(`Finished running ${i} tests`);
}

var numFromList = function(node) {
    let num = 0;
    for (let mult=1; node; node=node.next) {
        num += mult*node.val;
        mult *= 10;
    }
    return num;
}

var listFromNum = function(num) {
    let head = new ListNode(num % 10, null);
    for (var [curr, next] = [head, Math.floor(num/10)]; next; [curr.val, next] = [curr.val + (next % 10), Math.floor(next/10)]) {
        curr.next = new ListNode(0, null);
        curr = curr.next;
    }
    curr = null;
    return head;
}

ListNode.prototype.toString = function() {
    let ret = [];
    let node = this;
    while (node) {
        ret.push(node.val);
        node = node.next;
    }
    return `[${ret.join(", ")}]`;
}

var printList = function(node) {

}

function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}
