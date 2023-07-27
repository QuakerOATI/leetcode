/**
 * @param {number[][]} grid
 * @return {number}
 */
var countPyramids = function(grid) {
    // This appears to work, but is still TLE'd.
    var pyramids = [];
    var reversePyramids = [];
    for (let i=0; i<grid.length; ++i) {
        for (let j=0; j<grid[i].length; ++j) {
            grid[i][j] = {
                0: grid[i][j],
                1: grid[i][j],
                [-1]: grid[i][j]
            }
            if (grid[i][j][0]) {
                pyramids.push([i, j]);
                reversePyramids.unshift([i, j]);
            }
        }
    }
    let total = 0;
    for (let h=1; h<grid.length; ++h) {
        let [p, r] = [pyramids.length, reversePyramids.length];
        for (let x=0; x<p; ++x) {
            let [i, j] = pyramids.pop();
            if (
                grid[i-h] && grid[i-h][j][1] && 
                grid[i][j-h] && grid[i][j-h][0] && 
                grid[i][j+h] && grid[i][j+h][0]
            ) {
                pyramids.unshift([i, j]);
                total++;
            }
        }
        for (let x=0; x<r; ++x) {
            let [i, j] = reversePyramids.pop();
            if (
                grid[i+h] && grid[i+h][j][1] && 
                grid[i][j-h] && grid[i][j-h][0] && 
                grid[i][j+h] && grid[i][j+h][0]
            ) {
                reversePyramids.unshift([i, j]);
                total++;
            }
        }
    }
    return total;
}
            
// Accepted, and apparently one of only three solutions submitted in Javascript.
var countPyramids = function(grid) {
    let total = 0;
    for (let i=0; i<grid.length; ++i) {
        for (let j=0; j<grid[0].length; ++j) {
            if (grid[i][j]) {
                grid[i][j] = {
                    up: 1,
                    down: 1
                };
                let left = grid[i][j-1];
                let leftLeft = grid[i][j-2];
                let upLeft = grid[i-1] && grid[i-1][j-1];
                let upRight = grid[i-1] && grid[i-1][j+1];
                let up = grid[i-1] && grid[i-1][j];

                let hPos = Math.min(left?.up ?? 0, upLeft?.up ?? 0, leftLeft?.up ?? 0);
                let hNeg = Math.min(upLeft?.down ?? 0, up?.down ?? 0, upRight?.down ?? 0);

                grid[i][j].up += hPos;
                grid[i][j].down += hNeg;
                total += hPos + hNeg;
            }
        }
    }
    return total;
}
