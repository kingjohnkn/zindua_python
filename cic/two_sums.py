nums_list = [2, 7, 11, 15]
target_num = 9


def two_sums(nums, target):
    for i in nums:
        for j in nums:
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


print(two_sums(nums_list, target_num))

# given an array of integers nums and integer target
# return indices of the two numbers such that they add up to target
#
