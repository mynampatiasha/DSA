def max_sum_subarray(nums, k):
    # Manually calculate the sum of the first window
    window_sum = 0
    for i in range(k):
        window_sum += nums[i]
    max_sum = window_sum
    # Slide the window over the rest of the array
    for i in range(k, len(nums)):
        window_sum = window_sum + nums[i] - nums[i - k]  # Slide the window 
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum
