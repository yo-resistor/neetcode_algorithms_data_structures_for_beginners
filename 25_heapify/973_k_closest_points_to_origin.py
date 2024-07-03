class MinDistanceHeap:
    def __init__(self, points: list[list[int]]):
        if len(points) == 0:
        # if there is no points
            self.heap = [[0, 0]]
        else:
        # if there is at least one point
            points.append(points[0])
            points[0] = [0, 0]
            self.heap = points
        self.heapify(self.heap)
    
    def dist(self, point: list[int]) -> int:
        # point should be [int, int]
        # return euclidean distance between the point and origin
        return point[0] * point[0] + point[1] * point[1]
        
    def heapify(self, array: list[list[int]]) -> None:
        # percolate down starting with index without any children
        curr = (len(array) - 1) // 2
        while curr > 0:
            index = curr
            self.percolate_down(index=index)
            curr -= 1
        return
        
    def pop_heap(self) -> list[int]:
        if len(self.heap) == 1:
        # if there is NOTHING in heap
            return None
        if len(self.heap) == 2:
        # if there is only ONE in heap
            return self.heap.pop()
        # general case: there are more than one element in heap
        # pop the point with minimum distance
        # replace the minimum point with the last point
        # percolate down from the top
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.percolate_down(index=1)
        return res
        
    def percolate_down(self, index: int) -> None:
        while 2 * index < len(self.heap):
        # if there exists left child
            if (
                2 * index + 1 < len(self.heap) and
                self.dist(self.heap[2 * index + 1]) < self.dist(self.heap[2 * index]) and
                self.dist(self.heap[2 * index + 1]) < self.dist(self.heap[index])
            ):
            # if there exists right child
            # if right child's distance is smaller than left child
            # if right child's distance is smaller than parent
            # then swap the right child and parent points
                temp = self.heap[index]
                self.heap[index] = self.heap[2 * index + 1]
                self.heap[2 * index + 1] = temp
                index = 2 * index + 1
            elif (self.dist(self.heap[2 * index]) < self.dist(self.heap[index])):
            # if left child's distance is smaller than parent
            # then swap the left child and parent points
                temp = self.heap[index]
                self.heap[index] = self.heap[2 * index]
                self.heap[2 * index] = temp
                index = 2 * index
            else:
                break
        return
        
    def percolate_up(self, index: int) -> None:
        while (
            index > 1 and
            self.dist(self.heap[index]) < self.dist(self.heap[index // 2])
        ):
            temp = self.heap[index]
            self.heap[index] = self.heap[index // 2]
            self.heap[index // 2] = temp
            index = index // 2
        # if parent's distance is greater, swap the index and parent points
        return

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # corner case: if there are no points
        if len(points) == 0:
            return None
        # corner case: if k is greater than the number of points 
        if k > len(points):
            return None
        # general case
        results = []
        heap_points = MinDistanceHeap(points=points)
        print(heap_points.heap)
        for _ in range(k):
            results.append(heap_points.pop_heap())
        return results
        
def main():
    sol = Solution()
    print(sol.kClosest(points=[[3,3],[5,-1],[-2,4]], k=2))
    print(sol.kClosest(points=[[1,3],[-2,2]], k=1))
    
if __name__ == "__main__":
    main()