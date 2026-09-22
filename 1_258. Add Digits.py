class Solution:
    def addDigits(self, num: int) -> int:
        sum=0
        a=0
        while num>0:
            digit=num%10
            sum+=digit    #38-> 3+8 ->11
            num//=10
        while sum>9:
            a=0
            while sum>0:
                digi=sum%10  
                a+=digi        #11->1+1->2
                sum//=10
            sum=a
        return sum

sol=Solution()
result=sol.addDigits(38)
print(result)  # Output: 
