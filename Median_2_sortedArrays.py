class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # here we cannot use standard search as Comp will reach O(m+n)
        # But as per the constraints of comp O(log(m+n))
        # we use binary search
        A , B = nums1 , nums2
        tot = len(A) + len(B)
        half = tot//2

        if len(B)<len(A):
            A,B=B,A
        l,r = 0 , len(A) - 1
        
        while True :

            i = (l+r)//2 
            j = half -i-2

            Al = A[i] if i >=0 else float ("-infinity") 
            Ar = A[i+1] if (i+1) < len(A) else float ("infinity") 
            Bl = B[j] if j >=0 else float ("-infinity") 
            Br = B[j+1] if (j+1) < len(B) else float ("infinity") 


            # Managing the edge test cases
            
            if Al<=Br and Bl <= Ar:
                if tot % 2:
                    return (min(Ar,Br))
                return (max(Al,Bl) + min(Ar, Br))/2

            elif Al>Br:
                r = i-1

            else :
                l = i+1