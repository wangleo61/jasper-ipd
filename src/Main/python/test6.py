def lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    # Create a 2D array to store lengths of longest common subsequence.
    L = [[None]*(n+1) for i in range(m+1)]
    
    # Build the L[m+1][n+1] in bottom up fashion
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    # L[m][n] contains the length of LCS for X[0..n-1] and Y[0..m-1]
    return L[m][n]

# Example usage
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is", lcs(X, Y))