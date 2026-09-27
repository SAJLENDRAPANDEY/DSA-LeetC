class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        hashmap={}
        for a  in nums1:
            for b in nums2:
                total=a+b
                hashmap[total]=hashmap.get(total,0)+1

        ans=0
        for c in  nums3:
            for d in nums4:
                total=c+d
                remaining=-total

                if remaining in hashmap:
                    ans+=hashmap[remaining]
        return ans