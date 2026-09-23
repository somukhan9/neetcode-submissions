class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)
        # print(max_heap)
        while len(max_heap) > 1:
            s1 = heapq.heappop(max_heap)
            s2 = heapq.heappop(max_heap)

            if s2 > s1:
                heapq.heappush(max_heap, s1 - s2)

        max_heap.append(0)

        return abs(max_heap[0])