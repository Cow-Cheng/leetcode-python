import copy
from typing import List


# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result_list = copy.deepcopy(nums)
        length = len(result_list)
        for i in range(length):
            result_list[i] = nums[nums[i]]
        return result_list


if __name__ == '__main__':
    print(Solution().buildArray(nums=[0, 2, 1, 5, 3, 4]))
    print(Solution().buildArray(nums=[5, 0, 1, 2, 3, 4]))
