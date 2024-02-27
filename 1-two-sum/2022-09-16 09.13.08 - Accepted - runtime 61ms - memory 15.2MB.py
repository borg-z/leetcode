# class Solution:
#     def twoSum(self, nums, target: int):
#         d = dict()
#         for i,num in enumerate(nums):
#             if d.get(num):
#                 d[num].append(i)
#             else:
#                 d[num] = [i]
        
#         for i,num in enumerate(nums):
#             needed = target - num
#             found = d.get(needed)
#             if found:
#                 if len(found) > 1:
#                     found.remove(i)
#                 found = found[0]
#                 if found and found != i:
#                     return [i, found]


class Solution:
    def twoSum(self, nums, target: int):
        d = dict()
        for i,num in enumerate(nums):
            d[num] = i
        
        for i,num in enumerate(nums):
            needed = target - num
            if needed in d and d[needed] !=i:
                return [i, d[needed]]

