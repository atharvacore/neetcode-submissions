class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        sorted_nums = sorted(nums)
        result = []

        for i in range(len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            target = -sorted_nums[i]
            j = i + 1
            k = len(sorted_nums) - 1
            while j < k:
                total = sorted_nums[j] + sorted_nums[k]
                if total == target:
                    result.append([
                        sorted_nums[i],
                        sorted_nums[j],
                        sorted_nums[k]
                    ])
                    j += 1
                    k -= 1
                    while j < k and sorted_nums[j] == sorted_nums[j - 1]:
                        j += 1
                    while j < k and sorted_nums[k] == sorted_nums[k + 1]:
                        k -= 1
                elif total < target:
                    j += 1
                else:
                    k -= 1
        return result
