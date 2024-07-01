class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        # construct heap with given nums
        self.minHeap = nums
        self.k = k
        
        # if len(nums) is greater than k, pop the min until we get len(nums) == k
        
        
    def add(self, val: int) -> int:
        # if new val is smaller than or equal to the min (root val), return root val
        if val < self.minHeap[1]:
            return self.minHeap[1]
        
        # else insert new val in the heap
        self.minHeap.append(val)
        i_push = len(self.minHeap) - 1
        
        # percolate up
        while self.minHeap[i_push] < self.minHeap[i_push // 2]:
            self.minHeap[i_push], self.minHeap[i_push // 2] = self.minHeap[i_push // 2], self.minHeap[i_push]
            i_push = i_push // 2
        
        # pop the min just once since k = len(nums) - 1
        self.minHeap[1] = self.minHeap.pop()
        i_pop = 1
        
        # percolate down
        while (2 * i_pop) < len(self.minHeap):
        # if left child exists
            if (
                (2 * i_pop) + 1 < len(self.minHeap) and 
                self.minHeap[2 * i_pop + 1] < self.minHeap[2 * i_pop] and
                self.minHeap[2 * i_pop + 1] < self.minHeap[i_pop]
            ):
            # if right child exists
            # and right child is smaller than left child
            # and right child is smaller than parent -> swap
                self.minHeap[i_pop], self.minHeap[2 * i_pop + 1] = self.minHeap[2 * i_pop + 1], self.minHeap[i_pop]
                i_pop = 2 * i_pop + 1
            elif self.minHeap[2 * i_pop] < self.minHeap[i]:
            # if left child is smalelr than parent -> swap
                self.minHeap[i_pop], self.minHeap[2 * i_pop] = self.minHeap[2 * i_pop], self.minHeap[i_pop]
                i_pop = 2 * i_pop
            else:
            # if parent is the smallest
                break
        
        # return the root val
        return self.minHeap[1]