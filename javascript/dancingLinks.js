/* Implementation of Knuth's Dancing Links solution to the covering problem */

var CircularListNodeFactory = function (...circularRefNames) {
  return function (obj) {
    if (!obj) obj = {};
    circularRefNames.forEach(n => {
      if (!obj.hasOwnProperty(n) || !obj[n])
        obj[n] = obj;
    });
    return obj;
  }
}

class ConstraintMatrix {

  constructor(randomizationProbability = 0.3) {
    // Used for nondeterministically choosing rows
    this.RANDOMIZATION_PROBABILITY = randomizationProbability;
    this._solution = [];
    this._rows = [];
    this._columns = null;
  }

  static ListNode = CircularListNodeFactory("left", "right", "up", "down", "header");
  static Possibility = (id, [...constraints]) => { return { id, constraints, name: toString(id) } };

  static _removeColumn(node) {
    if (node?.left) node.left.right = node.right;
    if (node?.right) node.right.left = node.left;
  }

  static _removeRow(node) {
    if (node?.up) node.up.down = node.down;
    if (node?.down) node.down.up = node.up;
  }

  static _restoreColumn(node) {
    if (node?.left) node.left.right = node;
    if (node?.right) node.right.left = node;
  }

  static _restoreRow(node) {
    if (node?.up) node.up.down = node;
    if (node?.down) node.down.up = node;
  }

  addConstraints(...ids) {
    let node;
    let right = this._columns;
    for (let name of ids.map(toString).sort()) {
      for (; right && right.name < name; right = right?.right) { }
      this._restoreColumn(node = ConstraintMatrix.ListNode({
        name,
        right,
        left: right?.left,
        count: 0
      }));
      this._columns = this._columns && this._columns.name <= node.name ? this._columns : node;
      right = node;
    }
  }

  addPossibility(data, [...colIds]) {
    let idx = this._rows.push(data) - 1;
    let colHeader = this._columns;
    let tail;
    let node;
    for (let colName of colIds.map(toString).sort()) {
      for (; colHeader.name < colName; colHeader = colHeader.right) {
        if (colHeader.name !== colName) {
          colHeader = ConstraintMatrix.ListNode({
            left: colHeader?.left,
            right: colHeader?.right,
            name: colName,
            count: 0
          });
          this._restoreRow(colHeader);
        }
        node = ConstraintMatrix.ListNode({
          left: tail,
          right: tail?.right,
          header: colHeader,
          rowIdx: idx,
          up: header.up,
          down: header
        });
        this._restoreRow(node);
        this._restoreColumn(node);
        header.count++;
      }
    }
  }

  *_getElemRowIterator(node) {
    yield node;
    for (let curr = node.right; curr !== node; curr = curr.right)
      yield curr;
  }

  *_getElemColumnIterator(node) {
    yield node;
    for (let curr = node.down; curr !== node; curr = curr.down)
      yield curr;
  }

  _getRandomColElem(col) {
    for (let curr = col.head; Math.random() > this.RANDOMIZATION_PROBABILITY || curr === col.head; curr = curr.down) { }
    return curr
  }

  _getNextColumn() {
    let min = this._columns;
    for (let header of this._getElemRowIterator(this._columns)) {
      min = min && min.count < header.count ? min : header;
    }
    return min;
  }

  _backtrack() {
    let node = this._solution.pop();
    for (let colNode of this._getElemColumnIterator(node)) {
      this._restoreRow(colNode);
      for (let rowNode of this._getElemRowIterator(colNode)) {
        this._restoreColumn(rowNode);
      }
    }
  }

  solve() {
    // Solution to the exact cover problem represented by the Boolean constraint matrix using Knuth's "Dancing Links" algorithm
    while (true) {
      let col = this._getNextColumn();
      if (col.up === col) {
        // Empty column
        if (col.right === col) {
          console.log("Great success!  Dancing Links has yielded a solution to all your problems");
          return this._solution.map(n => this._rows[n.rowIdx]);
        } else {
          this._backtrack();
        }
      } else {
        let elem = this._getRandomColElem(col);
        this._solution.push(elem);
        for (let rowNode of this._getElemRowIterator(elem)) {
          for (let colNode of this._getElemColumnIterator(rowNode)) {
            this._removeRow(colNode);
          }
          this._removeColumn(rowNode);
        }
      }
    }
  }
}

