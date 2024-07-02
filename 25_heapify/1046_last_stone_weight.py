class MaxHeap:
    def __init__(self, nums: list[int]):
        # if there is NOTHING in nums
        if len(nums) == 0:
            self.heap = []
        # if there is ANYTHING in array, makes some changes ex: [3,4,5] -> [0,4,5,3]
        else:
            nums.append(nums[0])
            nums[0] = 0
            self.heap = nums
        self.max_heapify(self.heap)
        
    def max_heapify(self, array: list[int]) -> None:
        # set the pointer that has any children
        curr = (len(array) - 1) // 2
        
        while curr > 0:
            index = curr
            self.percolate_down(index=index)
            curr -= 1
        
        return
    
    def push(self, val: int) -> None:
        self.heap.append(val)
        index = len(self.heap) - 1
        self.percolate_up(index=index)
        return
        
    def pop(self) -> int:
        if len(self.heap) == 1:
        # there is NOTHING in heap
            return None
        if len(self.heap) == 2:
        # there is only one element in heap
            return self.heap.pop()
        
        # general case: if there are more than one element
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.percolate_down(index=1)
        
        return res
        
    def percolate_up(self, index) -> None:
        while (
            index > 1 and
            self.heap[index] > self.heap[index // 2]
        ):
            temp = self.heap[index]
            self.heap[index] = self.heap[index // 2]
            self.heap[index // 2] = temp
            index = index // 2
        
    def percolate_down(self, index) -> None:
        while 2 * index < len(self.heap):
        # if left child exists
            if (
                (2 * index + 1) < len(self.heap) and
                self.heap[2 * index + 1] > self.heap[2 * index] and
                self.heap[2 * index + 1] > self.heap[index]
            ):
            # if right child exists, 
            # if right child is greater than left child,
            # and if right child is greater than parent, swap right child and parent
                temp = self.heap[index]
                self.heap[index] = self.heap[2 * index + 1]
                self.heap[2 * index + 1] = temp
                index = 2 * index + 1
            elif (self.heap[2 * index] > self.heap[index]):
            # if left child is greater than parent         
                temp = self.heap[index]
                self.heap[index] = self.heap[2 * index]
                self.heap[2 * index] = temp
                index = 2 * index
            else:
                break
        return

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = MaxHeap(nums=stones)
        print(heap.heap)
        # if there is no stone in heap
        if len(heap.heap) - 1 < 1:
            return None
        # if there is more than one stone in heap
        while len(heap.heap) - 1 > 1:
            # pop two heaviest stones and smash
            # if they have same weight, do nothing after the popping
            # if there weight difference, add the difference to heap
            weight1 = heap.pop()
            weight2 = heap.pop()
            if weight1 != weight2:
                heap.push(abs(weight1 - weight2))
            
        if len(heap.heap) == 1:
        # if there is no stone remaining after smash
            heap.heap.append(0)
            
        return heap.heap[1]

def main():
    sol = Solution()
    
    print(sol.lastStoneWeight(stones=[2,7,4,1,8,1]))
    print(sol.lastStoneWeight(stones=[1]))
    print(sol.lastStoneWeight(stones=[1, 1]))
    
if __name__ == "__main__":
    main()