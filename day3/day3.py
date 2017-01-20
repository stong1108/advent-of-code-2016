from itertools import chain

class Solution(object):

    def __init__(self):
        self.lines = []

    def read_input(self, filename):
        with open(filename, 'r') as f:
            self.lines = [map(int, ln.strip('\n').split()) for ln in f.readlines()]

    def _is_triangle(self, s1, s2, s3):
        return int(all([s1+s2 > s3, s1+s3 > s2, s2+s3 > s1]))

    def count_vert_triangles(self):
        transposed = map(list, zip(*self.lines))
        chained = list(chain(*transposed))
        sideslist = [chained[i:i+3] for i in xrange(0, len(chained), 3)]
        return sum([self._is_triangle(*sides) for sides in sideslist])

    def count_horiz_triangles(self):
        return sum([self._is_triangle(*sides) for sides in self.lines])

if __name__ == '__main__':
    s = Solution()
    s.read_input('day3.txt')
    print 'Valid triangles by horizontal grouping: {}'.format(s.count_horiz_triangles())
    print 'Valid triangles by vertical grouping: {}'.format(s.count_vert_triangles())
