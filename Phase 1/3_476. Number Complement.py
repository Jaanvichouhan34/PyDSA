class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1

        while mask <= num:
            mask <<= 1

        mask -= 1

        return num ^ mask

sol=Solution()
result=sol.findComplement(5)
print(result)  # Output: 2