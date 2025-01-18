class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        prefix_product=[1]*n
        suffix_product=[1]*n
        product_array=[1]*n

        for i in range(1,len(nums)):
            prefix_product[i]=prefix_product[i-1]*nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            suffix_product[j]=suffix_product[j + 1] * nums[j+1]

        for i in range(len(nums)):
            product_array[i]=prefix_product[i]*suffix_product[i]

        return product_array