class Solution(object):

    def __init__(self):
        self.lines = []
        self.transposed = None
        self.most_message = ''
        self.least_message = ''

    def read_input(self, filename):
        with open(filename, 'r') as f:
            for ln in f.readlines():
                self.lines.append(list(ln.strip()))
            self.transposed = map(list, zip(*self.lines))

    def _most_and_least_letter(self, lst):
        d = dict()
        for char in lst:
            d[char] = d.get(char, 0) + 1
        most = d.keys()[d.values().index(max(d.values()))]
        least = d.keys()[d.values().index(min(d.values()))]
        return most, least

    def get_messages(self):
        for lst in self.transposed:
            most, least = self._most_and_least_letter(lst)
            self.most_message += most
            self.least_message += least

if __name__ == '__main__':
    s = Solution()
    s.read_input('day6.txt')
    s.get_messages()
    print 'Message 1: ' + s.most_message
    print 'Message 2: ' + s.least_message
