# s = "You ain't gotta lie to kick it"
# l = s.split(" ")
# l2 = ["C", "A", "P"]
# s2 = ", ".join(l2)

# print(f"This is the split string: {l}")
# print(f"This is the conjoined string: {s2}")
# print(sorted(l2))
# print("This is what a delta looks like: \u0394")


def binary_search_recurse(num, nums, low, high):
    if low >= high:
        return None
    mid = (low + high) // 2
    if nums[mid] == num:
        return mid
    elif nums[mid] < num: # search in the upper half
        return binary_search_recurse(num, nums, mid+1, high)
    else: # search in the lower half
        return binary_search_recurse(num, nums, low, mid+1)

        
def binary_search(num, nums):
    return binary_search_recurse(num, nums, 0, len(nums)-1)