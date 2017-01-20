class Solution(object):

    def __init__(self):
        self.lines = []
        self.transposed = None
        self.message = ''

    def read_input(self, filename):
        f = open(filename, 'r')
        for ln in f.readlines():
            self.lines.append(list(ln.strip()))
        self.transposed = map(list, zip(*self.lines))

    def _mostcommonletter(self, lst):
        d = dict()
        for char in lst:
            d[char] = d.get(char, 0) + 1
        return d.keys()[d.values().index(max(d.values()))]

    def get_message(self):
        for lst in self.transposed:
            self.message += self._mostcommonletter(lst)
        return self.message

if __name__ == '__main__':
    s = Solution()
    s.read_input('day6.txt')
    print s.get_message()
