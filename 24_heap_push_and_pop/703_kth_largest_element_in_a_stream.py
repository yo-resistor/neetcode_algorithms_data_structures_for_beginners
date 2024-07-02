class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        # construct heap with given nums
        self.minHeap = nums
        self.k = k
        self.heapify(self.minHeap)
        
        # if len(nums) is greater than k, pop the min until we get len(nums) == k
        while len(self.minHeap) > (self.k + 1):
            self.pop()
    
    def heapify(self, array: list[int]) -> None:
        # if the array is empty make it [0]
        if len(array) < 1:
            array.append(0)
        # if the array is not empty, make some changes ex [3, 4, 5] -> [0, 4, 5, 3]
        else:
            print("the array is not empty -----")
            array.append(array[0])
            array[0] = 0
        
        curr = (len(array) - 1) // 2
        
        while curr > 0:
            index = curr
            self.percolate_down(index=index)
            curr -= 1
        return
    
    def pop(self) -> None:
        if len(self.minHeap) == 1:
            return
        if len(self.minHeap) == 2:
            return
        self.minHeap[1] = self.minHeap.pop()
        self.percolate_down(index=1)
        return
        
    def add(self, val: int) -> int:
        self.minHeap.append(val)
        index = len(self.minHeap) - 1
        self.percolate_up(index=index)
        if len(self.minHeap) - 1 > self.k:
            self.pop()
        
        return self.minHeap[1]
    
    def percolate_down(self, index: int) -> None:
        while 2 * index < len(self.minHeap):
            if (
                2 * index + 1 < len(self.minHeap) and
                self.minHeap[2 * index + 1] < self.minHeap[2 * index] and
                self.minHeap[2 * index + 1] < self.minHeap[index]
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
        
        
    def percolate_up(self, index: int) -> None:
        while (
            index > 1 and
            self.minHeap[index // 2] > self.minHeap[index]
        ):
            temp = self.minHeap[index]
            self.minHeap[index] = self.minHeap[index // 2]
            self.minHeap[index // 2] = temp
            index = index // 2
        return
    
def main():
    obj = KthLargest(k=2, nums=[0])
    print(obj.minHeap)
    print("----done with initialization----")
    print(obj.add(-1), obj.minHeap)
    print(obj.add(1), obj.minHeap)
    print(obj.add(-2), obj.minHeap)
    print(obj.add(-4), obj.minHeap)
    print(obj.add(3), obj.minHeap)
    
if __name__ == "__main__":
    main()