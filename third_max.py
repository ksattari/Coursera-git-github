
class Solution:
    #@staticmethod
    def thirdMax(self,nums: list[int]) -> int:
        threeMax = [float('-inf')]*3
        if len(nums) < 3:
            return max(nums)
        else:
            for x in nums:
                if x > threeMax[0]:
                    threeMax = [x,threeMax[0],threeMax[1]]
                elif x > threeMax[1]:
                    threeMax = [threeMax[0],x,threeMax[1]]
                elif x > threeMax[2]:
                        threeMax = [threeMax[0],threeMax[1],x]
        if threeMax[2] > float('-inf'):
            return threeMax[2]
        else:
            return threeMax[0]

s = Solution()
print(s.thirdMax([1,2,3,4,5,6,7]))
