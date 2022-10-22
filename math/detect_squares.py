##https://leetcode.com/problems/detect-squares/

class DetectSquares:

    def __init__(self):
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        count = 0
        x = point[0]
        y = point[1]
        same_x = []
        same_y = []
        for elem in self.points:
            if elem[0] == x and elem[1] != y:
                same_x.append(elem)
            elif elem[0] != x and elem[1] == y:
                same_y.append(elem)
        for a in same_x:
            y = a[1]
            for b in same_y:
                x = b[0]
                for elem in self.points:
                    if elem[0] == x and elem[1] == y:
                        count += 1
        return count