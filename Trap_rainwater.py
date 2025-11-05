class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # Edge case: If no wall is present
        if n == 0:
            return 0
        
        # To store max height of wall from left and right 
        max_l = [0]*n
        max_r = [0]*n

        l_wall, r_wall = 0, 0
        for i in range(n):
            j = -i - 1
            # To record the maximum wall to the left of current position i
            max_l[i] = l_wall
            # Same for right of current position j
            max_r[j] = r_wall

            # Update the running maximums for next iteration
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])

        s = 0
        for k in range(n):
            # Find the limiting wall height at position k
            pot = min(max_l[k], max_r[k])
            # Adding trapped water if the potential height exceeds bar height
            s += max(0, pot - height[k])


        return s
    

'''In this code , I tried to precompute the maximum height of walls to the left and right of each bar.
For each position, the water that can be trapped above it is determined by:
    water_at_i = min(max_left[i], max_right[i]) - height[i]
If this value is positive, it means water can be held at that index.

And i am not going by the 2 pointer approach as i found it quite complicating and conceptually never 
repeating , it has a plus side that it gives a space comp = O(1) constant.

Algorithm Steps:
1. Traverse from left to right to compute `max_l[i]` — the tallest wall to the left of each bar.
2. Traverse from right to left to compute `max_r[i]` — the tallest wall to the right of each bar.
3. For each index, compute the trapped water using the formula above and sum it up.
4. Return the total trapped water.

Time Complexity:  O(n)
Space Complexity: O(n)
'''