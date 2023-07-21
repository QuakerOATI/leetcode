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

  constructor(randomizationProbability = 0.3, maxIterations = Infinity, maxAllowedDepth = Infinity) {
    // Used for nondeterministically choosing rows
    this.RANDOMIZATION_PROBABILITY = randomizationProbability;
    this.solution = [];
    this.rows = [];
    this.columns = null;
    this.maxAllowedDepth = maxAllowedDepth;
    this.maxIterations = maxIterations;
    this.maxDepth = -1;
    this.numIterations = -1;
  }

  static ListNode = CircularListNodeFactory("left", "right", "up", "down", "header");

  _removeCol(node) {
    if (node?.left) node.left.right = node?.right;
    if (node?.right) node.right.left = node?.left;
  }

  _removeRow(node) {
    if (node?.up) node.up.down = node?.down;
    if (node?.down) node.down.up = node?.up;
  }

  _restoreCol(node) {
    if (node?.left) node.left.right = node;
    if (node?.right) node.right.left = node;
  }

  _restoreRow(node) {
    if (node?.up) node.up.down = node;
    if (node?.down) node.down.up = node;
  }

  insertCol(name, searchStart = this.columns) {
    let col;
    if (!searchStart) {
      col = ConstraintMatrix.ListNode({
        name,
        count: 0
      });
    } else {
      let header = searchStart;
      for (
        ;
        header.name < name && header.right.name > header.name;
        header = header.right
      ) { }
      if (header.name === name) { return header; }
      while (header.name > name && header.left.name < header.name) { header = header.left; }
      col = ConstraintMatrix.ListNode({
        name,
        left: header,
        right: header.right,
        count: 0
      });
    }
    if (!this.columns || col.name < this.columns.name) { this.columns = col; }
    col.left.right = col;
    col.right.left = col;
    return col;
  }

  addPossibility(data, colIds) {
    let idx = this.rows.push(data) - 1;
    let searchStart = this.columns;
    let prev;
    let header;
    let node;
    for (let id of colIds.sort()) {
      header = this.insertCol(id, searchStart);
      node = ConstraintMatrix.ListNode({
        left: prev,
        right: prev?.right,
        up: header.up,
        down: header,
        rowIdx: idx,
        header: header
      });
      // console.log(node);
      node.left.right = node;
      node.right.left = node;
      node.up.down = node;
      node.down.up = node;
      prev = node;
      header.count++;
    }
  }

  *iterateRow(node) {
    if (node) yield node;
    for (let curr = node?.right; curr && curr !== node; curr = curr?.right)
      yield curr;
  }

  *iterateCol(node) {
    node = node.header;
    for (let curr = node?.down; curr && curr.down !== node; curr = curr?.down)
      yield curr;
  }

  getRandomColElem(col) {
    let curr;
    for (curr = col.header; Math.random() > this.RANDOMIZATION_PROBABILITY || curr === col.header; curr = curr.down) { }
    return curr
  }

  getNextCol() {
    let min = this.columns;
    for (let header of this.iterateRow(this.columns)) {
      min = min && min.count < header.count ? min : header;
    }
    return min;
  }

  backtrack() {
    let elem = this.solution.pop();
    let node;
    let colNode;
    let rowNode;
    for (colNode of this.iterateRow(elem)) {
      colNode.header.left.right = colNode.header;
      colNode.header.right.left = colNode.header;
      if (!this.columns || this.columns.name > colNode.header.name)
        this.columns = colNode.header;
      for (rowNode of this.iterateCol(colNode)) {
        for (node of this.iterateRow(rowNode)) {
          node.up.down = node;
          node.down.up = node;
          node.header.count++;
        }
      }
    }
  }

  eliminateRow(elem) {
    this.solution.push(elem);
    let node;
    let colNode;
    let rowNode;
    for (colNode of this.iterateRow(elem)) {
      for (rowNode of this.iterateCol(colNode)) {
        for (node of this.iterateRow(rowNode)) {
          if (node !== rowNode) {
            node.up.down = node.down;
            node.down.up = node.up;
            node.header.count--;
          }
        }
      }
      if (colNode.header === colNode.header.right) {
        return true;
      }
      colNode.header.left.right = colNode.header.right;
      colNode.header.right.left = colNode.header.left;
      if (this.columns === colNode.header)
        this.columns = colNode.header.right;
    }
    return false;
  }

  solve() {
    // Solution to the exact cover problem represented by the Boolean constraint matrix using Knuth's "Dancing Links" algorithm
    this.maxDepth = this.depth;
    this.numIterations = 0;
    while (true) {
      if (this.maxIterations && ++this.numIterations > this.maxIterations) {
        console.log(`Exceeded max number of iterations ${this.maxIterations}`)
        break;
      }
      if (this.depth > this.maxDepth) {
        this.maxDepth = this.depth;
        console.log(`Reached depth ${this.depth} after ${this.numIterations} iterations`);
      }
      if (this.maxAllowedDepth && this.maxDepth >= this.maxAllowedDepth) {
        console.log(`Max depth ${this.maxAllowedDepth} exceeded`);
        break;
      }
      let col = this.getNextCol();
      this.currentCol = col;
      if (col.up === col) {
        this.backtrack();
      } else {
        if (this.eliminateRow(this.getRandomColElem(col))) {
          console.log("Solution found!  Booyah!");
          return this.solution.map(n => this.rows[n.rowIdx]);
        }
      }
    }
  }

  reset() {
    while (this.solution.length) this.backtrack();
  }

  *headers() {
    yield this.columns;
    for (let header = this.columns.right; header !== this.columns; header = header.right) {
      yield header;
    }
  }

  getColByName(name) {
    for (let col of this.headers()) {
      if (col.name === name)
        return col;
    }
    console.log(`Sorry, no column with name ${name} was found`);
  }

  getRowData(row) {
    return this.rows[row?.rowIdx];
  }

  getColSize(col) {
    let cnt = 0;
    for (let elem of this.iterateCol(col)) {
      cnt++;
    }
    return cnt;
  }

  getRowSize(row) {
    let cnt = 0;
    for (let elem of this.iterateRow(row)) {
      cnt++;
    }
    return cnt;
  }

  get numCols() {
    if (!this.columns) return 0;
    let numCols = 1;
    for (let header = this.columns; header.right !== this.columns; header = header.right)
      numCols++;
    return numCols;
  }

  get depth() {
    return this.solution.length;
  }
}

