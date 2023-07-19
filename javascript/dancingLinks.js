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

class SparseBooleanMatrix {
  static RANDOMIZATION_PROBABILITY = 0.3;
  // static MatrixElem(left = null, right = null, up = null, down = null, header=null) {
  //   ret = { left, right, up, down, header };
  //   if (!ret.left) ret.left = ret;
  //   if (!ret.right) ret.right = ret;
  //   if (!ret.up) ret.up = ret;
  //   if (!ret.down) ret.down = ret;
  //   return ret;
  // }
  static ListNode = CircularListNodeFactory("left", "right", "up", "down", "header");
  static removeColumn(node) {
    node.left.right = node.right;
    node.right.left = node.left;
  }
  static removeRow(node) {
    node.up.down = node.down;
    node.down.up = node.up;
  }
  static restoreColumn(node) {
    node.left.right = node;
    node.right.left = node;
  }
  static restoreRow(node) {
    node.up.down = node;
    node.down.up = node;
  }
  addColumnHeader(colName) {
    let header = SparseBooleanMatrix.ListNode({
      left: this.columns?.left,
      right: this.columns,
      name: colName,
      count: 0
    });
    this.columns = this.columns ?? header;
    this.columns.left.right = header;
    this.columns.left = header;
  }
  addElem(rowName, colName) {
    let elem = SparseBooleanMatrix.ListNode({
      left: this.rowsByName[rowName]?.left,
      right: this.rowsByName[rowName],
      header: this.rowsByName[rowName]?.left?.header ?? this.columns
    });
    while (elem.header.name < colName) {
      elem.header = elem.header.right;
    }
    this.rowsByName[rowName] = this.rowsByName[rowName] ?? elem;
    elem.up = elem.header.up;
    elem.down = elem.header;
    this.restoreRow(elem);
  }
  constructor(colNames, rowData) {
    colNames.sort();
    this.rowDataByName = {};
    for (let colName of colNames)
      this.addColumnHeader(colName);
    for (let [rowName, ...cols] of rowData) {
      cols.sort();                    // so that we iterate in the same order as before
      for (let colName of cols) {
        this.addElem(rowName, colName);
      }
    }
    // Stack for removed rowData to enable backtracking
    this.solution = [];
  }

  *getRowIterator(node) {
    yield node;
    for (let curr = node.right; curr !== node; curr = curr.right)
      yield curr;
  }

  *getColumnIterator(node) {
    yield node;
    for (let curr = node.down; curr !== node; curr = curr.down)
      yield curr;
  }

  getRandomColElem(col) {
    for (let curr = col.head; Math.random() > SparseBooleanMatrix.RANDOMIZATION_PROBABILITY; curr = curr.down) { }
    return curr
  }

  backtrack() {
    let node = this.solution.pop();
    for (let colNode of this.getColumnIterator(node)) {
      this.restoreRow(colNode);
      for (let rowNode of this.getRowIterator(colNode)) {
        this.restoreColumn(rowNode);
      }
    }
  }

  dancingLinks() {
    while (true) {
      let col = this.getNextColumn();
      if (col.up === col) {
        // Empty column
        if (col.right === col) {
          console.log("Great success!  Dancing Links has yielded a solution to all your problems");
          return;
        } else {
          this.backtrack();
        }
      } else {
        let elem = this.getRandomColElem(col);
        this.solution.push(elem);
        for (let rowNode of this.getRowIterator(elem)) {
          for (let colNode of this.getColumnIterator(rowNode)) {
            this.removeRow(colNode);
          }
          this.removeColumn(rowNode);
        }
      }
    }
  }
}
