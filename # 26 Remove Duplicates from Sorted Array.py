# In short, without [:], we're creating a new list object, which is against what this problem is asking for:
# "Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory."
# 從頭到尾只會有一個 list 變數

# modifying the input array in-place
nums[:] = sorted(set(nums))

# creating a new list object
nums = sorted(set(nums))
