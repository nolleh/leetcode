def rob(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    M = [0] * len(nums)
    R = [0] * len(nums)
    M[0], M[1], M[2] = 0, nums[1], nums[2]
    R[0], R[1], R[2] = nums[0], nums[1], nums[2] + nums[0]

    for i in range(3, len(nums)):
        M[i] = max(nums[i] + M[i - 2], nums[i] + M[i - 3])
        R[i] = max(nums[i] + R[i - 2], nums[i] + R[i - 3])

    R[-1] = M[-1]

    return max(R[-1], R[-2], R[-3])
