"""
https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    # Time complexity O(nlogn), Space complexity O(1)
    # Sort input list first
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        count = 0
        while l < r:
            if nums[l] + nums[r] == k:
                count += 1
                r -= 1
                l += 1
            if nums[l] + nums[r] < k:
                l += 1
            if nums[l] + nums[r] > k:
                r -= 1
                        
        return count

        # # Hashmap one pass. It is slower than above in test cases.
        # def maxOperations(self, nums: List[int], k: int) -> int:
        #     count = 0
        #     hashmap = {}
        #     for i in nums:
        #         if (k - i in hashmap.keys()) and hashmap[k-i] > 0:
        #             count += 1
        #             hashmap[k-i] -= 1
        #         elif i in hashmap.keys():
        #             hashmap[i] += 1
        #         else:
        #             hashmap[i] = 1
            
        # return count
