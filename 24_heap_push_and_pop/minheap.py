class MinHeap:
    def __init__(self):
        self.minHeap = [0]
        
    def push(self, val: int) -> None:
        self.minHeap.append(val)
        index = len(self.minHeap) - 1
        self.percolate_up(index=index)
        return
        
    def pop(self) -> int:
        if len(self.minHeap) == 1:
            return None
        if len(self.minHeap) == 2:
            return self.minHeap.pop()
        res = self.minHeap[1]
        self.minHeap[1] = self.minHeap.pop()
        self.percolate_down(index=1)
        return res
    
    def top(self) -> int:
        if len(self.minHeap) < 2:
            return None
        return self.minHeap[1]
    
    def heapify(self, nums: list[int]) -> None:
        # if nums is empty make it [0]
        if len(nums) < 1:
            nums.append(0)
        # if nums is not empty, make some changes ex [3, 4, 5] -> [0, 4, 5, 3]
        else:
            nums.append(nums[0])
            nums[0] = 0

        self.minHeap = nums
        
        curr = (len(self.minHeap) - 1) // 2
        
        while curr > 0:
            index = curr
            self.percolate_down(index=index)
            curr -= 1
        return
    
    def percolate_down(self, index) -> None:
        while 2 * index < len(self.minHeap):
            if (
                (2 * index + 1) < len(self.minHeap) and
                self.minHeap[2 * index] > self.minHeap[2 * index + 1] and
                self.minHeap[index] > self.minHeap[2 * index + 1]
            ):
                temp = self.minHeap[index]
                self.minHeap[index] = self.minHeap[2 * index + 1]
                self.minHeap[2 * index + 1] = temp
                index = 2 * index + 1
            elif (self.minHeap[2 * index] < self.minHeap[index]):
                temp = self.minHeap[index]
                self.minHeap[index] = self.minHeap[2 * index]
                self.minHeap[2 * index] = temp
                index = 2 * index
            else:
                break
        return
    
    def percolate_up(self, index) -> None:
        while (
            index > 1 and
            self.minHeap[index // 2] > self.minHeap[index]
        ):
            temp = self.minHeap[index]
            self.minHeap[index] = self.minHeap[index // 2]
            self.minHeap[index // 2] = temp
            index = index // 2
            
def main():
    heap = MinHeap()
    print(heap.top(), heap.minHeap)
    heap.push(2)
    print(heap.top(), heap.minHeap)
    heap.push(3)
    print(heap.top(), heap.minHeap)
    heap.push(1)
    print(heap.top(), heap.minHeap)
    heap.pop()
    print(heap.top(), heap.minHeap)
    heap.pop()
    print(heap.top(), heap.minHeap)
    heap.pop()
    print(heap.top(), heap.minHeap)
    
if __name__ == "__main__":
    main()