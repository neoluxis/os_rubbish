class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Dutch National Flag problem.
        0-red, 1-white, 2-blue.
        One pass, O(n) time, O(1) space.
        """
        red, white, blue = 0, 0, len(nums) - 1
        
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:  # nums[white] == 2
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1