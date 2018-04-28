import heapq
import math


# prints k number of lowest distance points from center
def closest(points, k):
    points_dict = {}
    min_heap = []

    for point in points:
        points_dict[math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2))] = point
        heapq.heappush(min_heap, math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2)))

    while k != 0:
        print points_dict.get(min_heap.pop(0))
        k -= 1


points = [(-2, -4), (0, -2), (-1, 0), (3, -5), (-2, -3), (3, 2)]
points2 = [(-1, 1), (2, 2), (0, 1), (0, 0), (8, -6), (5, -2)]

closest(points, 3)
print
closest(points2, 3)
