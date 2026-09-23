class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        self.k = k

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[len(self.arr)-self.k]
        
# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.min_heap = nums
#         self.k = k

#         heapq.heapify(self.min_heap)

#         while len(self.min_heap) > k:
#             heapq.heappop(self.min_heap)        

#     def add(self, val: int) -> int:
        
