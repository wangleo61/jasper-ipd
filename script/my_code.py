from typing import List

class Solution:
    def check_prime(self, x: int) -> bool:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    def primeSubOperation(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if i == 0:
                bound = nums[0]
            else:
                bound = nums[i] - nums[i - 1]
            if bound <= 0:
                return False
            largest_prime = 0
            for j in range(bound - 1, 1, -1):
                if self.check_prime(j):
                    largest_prime = j
                    break
            nums[i] = nums[i] - largest_prime
            if i > 0 and nums[i] <= nums[i - 1]:
                return False
        return True

    def sort_nums(self, nums: List[int]) -> List[int]:
        """
        Sorts the input list in ascending order and returns the sorted list.
        """
        return sorted(nums)

if __name__ == "__main__":
    sol = Solution()
    nums1 = [5, 8, 13]
    nums2 = [4, 4, 4]
    print("Test 1:", sol.primeSubOperation(nums1.copy()))  # Should print True or False
    print("Test 2:", sol.primeSubOperation(nums2.copy()))  # Should print False
    print("Sorted:", sol.sort_nums([3, 1, 2]))
    print("Sorted:", sol.sort_nums([3, 1, 2]))
    print("Sorted:", sol.sort_nums([3, 1, 2]))
