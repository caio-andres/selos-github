def binary_search(nums, h):
  lo = 0
  hi = len(nums)
  steps = 0
  
  while lo < hi:
    steps += 1
    mid = int((lo + hi) / 2)
    if h > mid:
      lo = mid + 1
    elif h < mid:
      lo = mid - 1  