from bisect import bisect_left
import sys

#!/usr/bin/env python3
# GitHub Copilot
# file: findLongestSeuence.py
# Usage:
#   python findLongestSeuence.py "string"
#   python findLongestSeuence.py "string1" "string2"


def longest_increasing_subsequence(s: str) -> str:
    if not s:
        return ""
    n = len(s)
    tails = []        # stores indices of ends of LIS of length i+1
    tail_chars = []   # corresponding characters for binary search
    prev = [-1] * n   # previous index in LIS for each position

    for i, ch in enumerate(s):
        pos = bisect_left(tail_chars, ch)
        pred = tails[pos - 1] if pos > 0 else -1
        prev[i] = pred
        if pos == len(tails):
            tails.append(i)
            tail_chars.append(ch)
        else:
            tails[pos] = i
            tail_chars[pos] = ch

    # reconstruct
    idx = tails[-1]
    seq = []
    while idx != -1:
        seq.append(s[idx])
        idx = prev[idx]
    return ''.join(reversed(seq))

def longest_palindromic_subsequence(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2 if j > i else 1
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    i, j = 0, n - 1
    left = []
    right = []
    while i <= j:
        if s[i] == s[j]:
            left.append(s[i])
            if i != j:
                right.append(s[j])
            i += 1
            j -= 1
        elif dp[i + 1][j] >= dp[i][j - 1]:
            i += 1
        else:
            j -= 1
    return ''.join(left) + ''.join(reversed(right))

def longest_common_subsequence(a: str, b: str) -> str:
    m, n = len(a), len(b)
    if m == 0 or n == 0:
        return ""
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if a[i] == b[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    i = j = 0
    res = []
    while i < m and j < n:
        if a[i] == b[j]:
            res.append(a[i])
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1
    return ''.join(res)

def main(argv):
    if len(argv) < 2:
        print("Provide one or two input strings as arguments.")
        print("Example: python findLongestSeuence.py 'character' 'char'")
        return
    s1 = argv[1]
    s2 = argv[2] if len(argv) > 2 else None

    print("Input 1:", s1)
    print("Longest Increasing Subsequence:", longest_increasing_subsequence(s1))
    print("Longest Palindromic Subsequence:", longest_palindromic_subsequence(s1))
    if s2 is not None:
        print("Input 2:", s2)
        print("Longest Common Subsequence:", longest_common_subsequence(s1, s2))

if __name__ == "__main__":
    main(sys.argv)