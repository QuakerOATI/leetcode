/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    for (let i=0; 2*i<=matrix.length-1; ++i) {
        for (let j=0; 2*j<matrix.length-1; ++j) {
            for (let k=0; k<3; ++k) {
                [matrix[i][j], matrix[matrix.length-j-1][i]] = [matrix[matrix.length-j-1][i], matrix[i][j]];
                [i, j] = [matrix.length-j-1, i];
            }
            [i, j] = [matrix.length-j-1, i];
        }
    }
}

// This rotates the elements of the matrix around the (fixed) middle.
// Unfortunately, that's not what the problem asked for.  :/
var rotateRigid = function(matrix) {
    const rotateShell = (mat, i) => {
        if (2*(i+1) >= mat.length)
            return;
        let r = mat.length-i;
        for (let j=i+1; j<r; ++j) {
            [mat[j][i], mat[j-1][i]] = [mat[j-1][i], mat[j][i]];
        }
        for (let j=i+1; j<r; ++j) {
            [mat[r-1][j], mat[r-1][j-1]] = [mat[r-1][j-1], mat[r-1][j]];
        }
        for (let j=r-1; j>i; --j) {
            [mat[j][r-1], mat[j-1][r-1]] = [mat[j-1][r-1], mat[j][r-1]];
        }
        for (let j=r-1; j>i+1; --j) {
            [mat[i][j], mat[i][j-1]] = [mat[i][j-1], mat[i][j]];
        }
    }
    for (let i=0; 2*(i+1) < matrix.length; ++i) {
        rotateShell(matrix, i);
    }
};
