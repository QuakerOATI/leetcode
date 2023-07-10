class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        s[0]: look at s[:0], s[:1]
        s[1]: look at s[:2], s[:3]
        s[2]: s[:4], s[:5]
        A[i][j] = expected char at pos j if s[i:j] is to be a palindrome
                == s[i]
        (i+k, j-k) for k in range((j-i)//2)
        center := (i+j)//2
        -----------------------
        B[i][j] = ord(s[j]) - ord(s[i])
        s[0]    |   B[0, 0] == 0
        s[1]    |   B[0, 1] == s[1] - s[0]
                |   B[1, 1] == 0
        s[2]    |   B[1, 2] == s[2] - s[1]
                |   B[0, 2]
        B[1, 2] == s[2] - s[1]
        B[0, 2] == s[2] - s[0] == s[2] - s[1] + s[1] - s[0]
                                == B[0][1] + B[1][2]
        B[2, 2] == 0
        Given:
            B[i, j] for all j >= i, i+j < k
        Compute:
            B[i', j'] for i' >= j', i' + j' == k
        -B[i+1, j] + B[i, j+1] == B[i, j] + B[i+1, j+1]
        B[i, j+r] - B[i+r, j] == B[i, j] + B[j+r, i+r]
        -----------------------
        C[i, j] := sum(s[i:j])
        if isPal(s[i:j]):
            assert C[i, k] == C[i+j-k, j]
        -----------------------
        Testcases:
            (1) s = c*100

        Barely accepted: takes around 8 seconds; best solutions are around 99 ms
        Much better to just scan through all chars linearly, using Python slices to compare substrings with reversed substrings
        """
        if len(s) == 0:
            return ""
        ispal = [[a == b for a in range(len(s))] for b in range(len(s))]
        best, start, end = 1, 0, 0
        for L in range(1, len(s)):
            for i in range(len(s) - L + 1):
                j = i + L - 1
                subproblem = (L <= 2) or ispal[i + 1][j - 1]
                ispal[i][j] = s[i] == s[j] or subproblem
                if ispal[i][j] and L > best:
                    best, start, end = L, i, j
        return s[start : end + 1]


def print_mat(mat):
    mat = list(mat)
    mat.insert(0, ["-" * 7 for _ in range(len(mat[0]))])
    mat.append(["-" * 7 for _ in range(len(mat[0]))])
    for row in mat:
        print(list(map(lambda v: str(v).center(7), row)))


def longestPalindrome(s: str) -> str:
    if len(s) == 0:
        return ""
    ispal = [[a == b for a in range(len(s))] for b in range(len(s))]
    print_mat(ispal)
    best, start = 1, 0
    for L in range(1, len(s) + 1):
        print(f"Length: {L}")
        for i in range(len(s) - L + 1):
            j = i + L - 1
            subproblem = (L <= 2) or ispal[i + 1][j - 1]
            ispal[i][j] = (s[i] == s[j]) and subproblem
            print(f"    ispal{(i, j)} = {ispal[i][j]}")
            if ispal[i][j] and L > best:
                best, start = L, i
                print(f"        --> best, start = {L}, {i}")
    print_mat(ispal)
    print(best, start)
    return s[start : start + best]
