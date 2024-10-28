class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[len(text1)][len(text2)]

def main():
    sol = Solution()

    print(sol.longestCommonSubsequence(text1 = "abcde", text2 = "ace"))
    print(sol.longestCommonSubsequence(text1 = "abc", text2 = "abc"))
    print(sol.longestCommonSubsequence(text1 = "abc", text2 = "def"))
    
if __name__ == "__main__":
    main()