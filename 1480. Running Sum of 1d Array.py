from typing import List


# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result_list = []
        length = len(nums) + 1
        for i in range(1, length):
            result_list.append(sum(nums[:i]))
        return result_list


if __name__ == '__main__':
    print(Solution().runningSum(nums=[1, 2, 3, 4]))
    print(Solution().runningSum(nums=[1, 1, 1, 1, 1]))
    print(Solution().runningSum(nums=[3, 1, 2, 10, 1]))
