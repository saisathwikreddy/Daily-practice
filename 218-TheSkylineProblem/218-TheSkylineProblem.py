# Last updated: 6/26/2025, 2:34:52 PM
from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Step 1: Create events
        events = []
        for left, right, height in buildings:
            events.append((left, -height))   # start of a building
            events.append((right, height))   # end of a building

        # Step 2: Sort events by x, then by height
        events.sort()
        
        # Step 3: Process events with max heap
        result = []
        heap = [0]  # Initial ground height
        height_map = defaultdict(int)
        height_map[0] = 1  # ground is always valid
        prev_max = 0

        for x, h in events:
            if h < 0:
                heappush(heap, h)
                height_map[-h] += 1
            else:
                height_map[h] -= 1

            # Clean the heap's top if invalid
            while heap and height_map[-heap[0]] == 0:
                heappop(heap)

            # Safely check current max
            current_max = -heap[0] if heap else 0
            if current_max != prev_max:
                result.append([x, current_max])
                prev_max = current_max

        return result
