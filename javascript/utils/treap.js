class Treap {
    constructor(cmp, val, priority) {
        this.cmp = cmp;
        this.val = val;
        this.priority = priority;
    }
    static split(T, val) {
        if (T == null)
            return [null, null];
        if (T.val <= val) {
            if (T.right == null)
                return [T, null];
            [t1, t2] = Treap.split(T.right, val);
            T.right = t1;
            return [T, t2];
        } else {
            if (T.left == null)
                return [null, T];
            [t1, t2] = Treap.split(T.left, val);
            T.left = t2;
            return [t1, T];
        }
    }
    static merge(T1, T2) {
        if (T1 == null) return T2;
        if (T2 == null) return T1;
        if (T1.val > T2.val)
            return Treap.merge(T2, T1);
        T1.right = Treap.merge(T1.right, T2);
        return T1;
    }
    static find_max_bounded_priority(T, p) {
    }
    static from(...vals) {
    }
    insert(val, priority) {
    }
    find(val) {
    }
    remove(val) {
        let node = this.find(val);
        :
    }
    union(T) {
    }
}
