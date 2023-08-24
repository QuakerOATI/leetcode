var fourSumCount = function(...arrs) {
    let n = arrs[0].length;
    arrs.forEach(A => {
        A.sort((x, y) => x - y);
        let i = 0;
        while (true) {
            if (i >= A.length)
                break;
            let j = i;
            for (; j < A.length && A[j] === A[i]; ++j);
            A = A.splice(i, j - i, [A[i], j - 1]);
        }
    });
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            let S = arrs[0][i] + arrs[1][j];
            if (S + arrs[2][0] + arrs[3][0] > 0)
                break;
            if (S + arrs[2][n - 1] + arrs[3][n - 1] < 0)
                continue;
            let l = 0, r = n - 1;
            while (l 
    

}
