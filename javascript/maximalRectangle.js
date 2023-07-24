/**
 * @param {character[][]} matrix
 * @return {number}
 */
// This works but it uses too much memory :/
var maximalRectangle = function(matrix) {
  let m = matrix.length;
  let n = matrix[0].length;
  let i;
  let j;
  let k;
  let l;
  var subs = {
    A: 0,
    get: function(i, j, k, l) {return this[`${i},${j},${k},${l}`];},
    put: function(i, j, k, l, val) {
      this[`${i},${j},${k},${l}`] = val;
      if (val && ((k-i+1)*(l-j+1) > this.A))
        this.A = (k-i+1)*(l-j+1);
      return this.A;
    }
  };
  for (i=0; i<m; ++i) {
    for (j=0; j<n; ++j) {
      subs.put(i, j, i, j, matrix[i][j] === "1");
    }
  }
  // A failed attempt to solve the memory problem
  matrix = null;
  for (k=0; k<m; ++k) {
    for (l=0; l<n; ++l) {
      for (j=l+1; j<n; ++j) {
        subs.put(k, l, k, j, subs.get(k, l, k, j-1) && subs.get(k, j, k, j));
      }
      for (i=k+1; i<m; ++i) {
        subs.put(k, l, i, l, subs.get(k, l, i-1, l) && subs.get(i, l, i, l));
      }
    }
  }
  // The next series of nested loops seems to be the most problematic memory-wise.
  let best = subs.A;
  for (k=0; k<m; ++k) {
    for (l=0; l<n; ++l) {
      for (i=k+1; i<m; ++i) {
        for (j=l+1; j<n; ++j) {
          // subs.put(k, l, i, j, subs.get(k, l, i-1, j) && subs.get(i, l, i, j));
          if (subs.get(k, l, i-1, j) && subs.get(i, l, i, j)) {
            best = Math.max(best, (j-l+1)*(i-k+1));
          }
        }
      }
    }
  }
  return best;
};

var reduceMatrix = function(matrix) {
  // Strategy: let matrix[i][j] := length of the longest horizontal "streak" ending at (i, j)
  let i;
  let j;
  for (i=0; i<matrix.length; ++i) {
    for (j=0; j<matrix[0].length; ++j) {
      if (matrix[i][j] === '1') {
        matrix[i][j] = 1 + (matrix[i-1][j] ?? 0);
      } else {
        matrix[i][j] = 0;
      }
    }
  }
  let min;
  for (j=0; j<matrix[0].length; ++j) {
    let len = 0;
    for (i=0; i<matrix.length; ++i) {
      if (!matrix[i][j]) {
        len = 0;
        min = null;
      } else {
        ++len;
        min = Math.min(min ?? matrix[i][j], matrix[i][j]);
      }
    }
  }
}

var recursiveSolution = function(matrix) {
  var bestLeftTerminatingSubrect = function(mat, L) {
    let i;
    let j;
    let k;
    for (i=0; i<mat.length; ++i) {
      for (j=L; j<mat[0].length && mat[i][j] === "1"; ++j) { }
      mat[i][L] = j;
    }
  }
}
