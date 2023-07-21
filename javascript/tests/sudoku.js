var board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]];
//
// var pos = new SudokuBoard(board);
// console.log(pos.toString());
//
// var testLegalMoves = () => {
//   for (m of pos.legalMoves()) {
//     console.log(`Applying move ${m}`);
//     pos.applyMove(...m);
//     console.log(pos.toString());
//     pos.backtrack();
//   }
// }


let chars = "123456789".split("");
var matrix = new ConstraintMatrix();
var numPossibilities = 0;
board.forEach((row, i) => {
  row.forEach((entry, j) => {
    if (entry === ".") {
      let box = i - (i % 3) + Math.floor(j / 3);
      console.log(`Adding possibilities for row = ${i}, col = ${j}, box = ${box}`);
      chars.forEach(char => {
        numPossibilities++;
        matrix.addPossibility({ name: `R${i}C${j}IS${char}`, apply: function (b) { b[i][j] = char; } },
          [`ROW${i}COL${j}`, `R${i}HAS${char}`, `C${j}HAS${char}`, `B${box}HAS${char}`]);
      });
    }
  });
});
