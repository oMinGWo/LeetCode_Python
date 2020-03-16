class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        r = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                r.append(nums1[i])
                i += 1
            else:
                r.append(nums2[j])
                j += 1

        while i < len(nums1):
            r.append(nums1[i])
            i += 1

        while j < len(nums2):
            r.append(nums2[j])
            j += 1

        length = len(nums2) + len(nums1)
        if length % 2 == 1:
            return r[length / 2]
        else:
            return (r[length/2] + r[length/2-1]) / 2.0


if __name__ == '__main__':
    s = Solution()
    print s.findMedianSortedArrays([1, 3], [2, 4])
