class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        return half * half * x
# Create an instance of the Solution class
sol = Solution()

# Call the function with test inputs (e.g., x=2.0, n=10) and print the result
result = sol.myPow(2.0, 10)
print(result)
