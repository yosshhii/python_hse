class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow_pointer = nums[0]
        fast_pointer = nums[nums[0]]

        while slow_pointer != fast_pointer:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[nums[fast_pointer]]

        slow_pointer = 0

        while slow_pointer != fast_pointer:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[fast_pointer]

        return slow_pointer