def max_sum_sub_distinct(nums):
  window_sum=0
  max_sum=0
  left=0
  seen=set()
  for i in range(nums):
    if nums[i] in seen:
      seen.remove(nums[i])
      window_sum-=nums[i]
      left+=1
    seen.add(nums[i])
    window_sum+=nums[i]
    if i-left+1==k:    # when the size of the window is achieved then the sum_value is marked
      max_sum=max(max_sum,window_sum)
      seen.remove(nums[left]) # to remove the leftmost element of window
      window_sum-=nums[left]  # to remove its leftmost element from sum
      left+=1
  return max_sum
