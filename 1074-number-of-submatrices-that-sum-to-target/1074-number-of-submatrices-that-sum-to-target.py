class Solution:
    def numSubmatrixSumTarget(self, A: List[List[int]], target: int) -> int:
        m = len(A)
        n = len(A[0])

        # Compute the cumulative sum for each row
        for row in A:
            for i in range(n - 1):
                row[i + 1] += row[i]

        res = 0  # Initialize the result variable to count submatrices

        # Iterate over all possible pairs of columns
        for i in range(n):
            for j in range(i, n):
                c = collections.defaultdict(int)
                cur =  0
                c[0] = 1  # Initialize the current sum and a counter for cumulative sums

                # Iterate over each row to calculate the submatrix sum
                for k in range(m):
                    cur += A[k][j] - (A[k][i - 1] if i > 0 else 0)
                    res += c[cur - target]  # Count submatrices with the target sum
                    c[cur] += 1  # Update the counter for the current cumulative sum

        return res