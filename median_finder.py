# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        is_even = ((len(nums1) + len(nums2))%2) == 0
        
        i = 0
        j = len(nums2)-1
        while nums1[i] < nums2[i]:
            if i+1 < len(nums1) and nums1[i+1] < nums2[j]:
                i += 1
            elif j-1 >= 0 and nums2[j-1] > nums1[i]:
                j -= 1
            else:
                if is_even:
                    return nums
     
    
class Surfer:
    
    def __init__(self, list1, list2, direction):
        self.direction = direction
        if direction == 1:
            self.idx_list = [0, 0]
        elif direction == -1:
            self.idx_list = [len(list1)-1, len(list2)-1]
        else:
            raise ValueError
        self.activetrack = 0 if list1[idx_list[0]]