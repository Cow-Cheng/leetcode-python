from typing import List


# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for i in accounts:
            total = sum(i)
            if total > maximum:
                maximum = total
        return maximum


if __name__ == '__main__':
    print(Solution().maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]]))
    print(Solution().maximumWealth(accounts=[[1, 5], [7, 3], [3, 5]]))
