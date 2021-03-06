class Solution(object):
    def addNegabinary(self, arr1, arr2):
        result = []
        carry = 0
        while arr1 or arr2 or carry:
            if arr1:
                carry += arr1.pop()
            if arr2:
                carry += arr2.pop()
            result.append(carry & 1)
            carry = -(carry >> 1)
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        result.reverse()
        return result
val=Solution()
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(*val.addNegabinary(arr1,arr2))
