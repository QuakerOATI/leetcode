import { ConstraintMatrix } from "./dancingLinks";
/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */

var solveSudokuDancingLinks = function (board) {
  let chars = "123456789".split("");
  matrix = ConstraintMatrix();
  board.forEach((row, i) => {
    row.forEach((entry, j) => {
      if (entry === ".") {
        let box = i - (i % 3) + Math.floor(j / 3);
        chars.forEach(char => {
          matrix.addPossibility({ apply: function (b) { b[i][j] = char; } },
            [`ROW${i}COL${j}`, `R${i}HAS${char}`, `C${j}HAS${char}`, `B${box}HAS${char}`]);
        });
      }
    });
  });
  for (possibility of matrix.solution()) {
    possibility.apply(board);
  }
}

class SudokuBoard {
  static CHARS = "123456789".split("");
  constructor(board) {
    this._position = board;
    this._moves = [];
    this.maxDepth = 0;
    this.numPositionsConsidered = 0;
    this.closestApproach = this.numBlanks;
  }
  get serialized() {
    return this._position.map(r => r.join("")).join("");
  }
  get depth() {
    return this._moves.length;
  }
  get rows() {
    return this._position;
  }
  get columns() {
    return this._position.map((_, i) => this._position.map(r => r[i]));
  }
  get cells() {
    return [0, 3, 6].map(i => [0, 3, 6].map(j =>
      this._position.map(r => r.slice(i, i + 3)).slice(j, j + 3).flat()
    ))
  }
  get numBlanks() {
    return this._position.flat().filter(c => c === ".").length;
  }
  get isSolved() {
    return this.numBlanks === 0 && this.isValidPosition();
  }
  reset() {
    while (this.depth > 0)
      this.backtrack();
    this.numPositionsConsidered = 0;
    this.closestApproach = this.numBlanks;
  }
  isValidPosition() {
    return SudokuBoard.CHARS.every(c =>
      this.rows.every(row => row.indexOf(c) === row.lastIndexOf(c))
      && this.columns.every(col => col.indexOf(c) === col.lastIndexOf(c))
      && this.cells.every(cell => cell.indexOf(c) === cell.lastIndexOf(c))
    );

  }
  applyMove(i, j, c) {
    if (i === null || j === null)
      return;
    this._moves.push([i, j, this._position[i][j]]);
    this._position[i][j] = c;
  }
  backtrack() {
    let [i, j, c] = this._moves.pop();
    this._position[i][j] = c;
  }
  *legalMoves() {
    for (let i = 0; i < 9; i++) {
      for (let j = 0; j < 9; j++) {
        if (this._position[i][j] === ".") {
          for (let c of SudokuBoard.CHARS) {
            if (
              !this._position[i].includes(c) &&
              !this._position.some(r => r[j] === c) &&
              !this.getCell(i, j).includes(c)
            )
              yield [i, j, c];
          }
        }
      }
    }
  }
  toString() {
    return this._position.map(r => r.join("  ")).join("\n\n");
  }
  getCell(i, j) {
    let [m, n] = [Math.floor(i / 3), Math.floor(j / 3)];
    return this._position.slice(3 * m, 3 * m + 3).map(r => r.slice(3 * n, 3 * n + 3)).flat();
  }
  solve() {
    let numInitialBlanks = this.numBlanks;
    let moves = [[0, [null, null], this.serialized, numInitialBlanks]];
    let maxDepth = 0;
    while (moves.length) {
      this.numPositionsConsidered++;
      let [depth, move, state, blanks] = moves.pop();
      if (this.depth < depth) {
        console.log("Houston, we have a problem");
        break;
      }
      while (this.depth > depth)
        this.backtrack();
      if (state !== this.serialized || this.numBlanks !== blanks) {
        console.log("MISMATCHED STATE:");
        console.log(`   depth = ${this.moves.length}`);
        console.log(`   numBlanks = ${this.numBlanks}`);
        console.log(`   numPrevBlanks = ${blanks}`);
        break;
      }
      if (this.depth > maxDepth)
        maxDepth = this.depth;
      if (maxDepth > numInitialBlanks) {
        console.log(`Max theoretical depth exceeded`);
        break;
      }
      this.applyMove(...move);
      this.closestApproach = Math.min(this.closestApproach, this.numBlanks);
      if (this.numBlanks === 0)
        break;
      for (let move of this.legalMoves())
        moves.push([this.depth, move, this.serialized, this.numBlanks]);
    }
    if (this.isSolved)
      console.log("Success!");
    else
      console.log("DFS solution failed :/");
    console.log(this.toString());
  }
}

var solveSudokuDFS = function (board) {
  let gameBoard = new SudokuBoard(board);
  let s = gameBoard.serialized;
  let moves = [[0, [null, null]]];
  while (moves.length) {
    let [depth, move] = moves.pop();
    if (gameBoard.depth < depth) {
      console.log("Houston, we have a problem");
      break;
    }
    while (gameBoard.depth > depth)
      gameBoard.backtrack();
    if (depth === 0 && gameBoard.serialized !== s) {
      console.log("MISMATCH at depth 0");
      break;
    }
    gameBoard.applyMove(...move);
    if (gameBoard.numBlanks === 0)
      break;
    for (let move of gameBoard.legalMoves())
      moves.push([gameBoard.depth, move]);
  }
  if (gameBoard.isSolved)
    console.log("Success!");
  else
    console.log("DFS solution failed :/");
  console.log(gameBoard.toString());
};

