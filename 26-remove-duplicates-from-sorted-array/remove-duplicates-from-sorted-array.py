class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0: 
            return 0
        else:
            i=0
            cnt=1
            for j in range(1,len(nums)):
                if nums[i]!=nums[j]:
                    nums[i+1],nums[j]=nums[j],nums[i+1]
                    i+=1
                    cnt+=1
        return cnt
        