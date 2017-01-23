import re

class Solution(object):

    def __init__(self):
        self.compressed = ''
        self.decompressed = ''

    def load_input(self, filename):
        with open(filename, 'r') as f:
            self.compressed = f.read().strip()

    def pattern(self, start_ind, length, times):
        substr = self.compressed[start_ind:start_ind + length]
        self.decompressed += substr * times
        new_ind = start_ind + length
        return new_ind

    def decompress(self):
        i = 0
        pattern = re.compile('\([0-9]+x[0-9]+\)')
        while i < len(self.compressed):
            matched = pattern.match(self.compressed, i)
            if not matched:
                self.decompressed += self.compressed[i]
                i += 1
            else:
                nums = map(int, matched.group(0)[1:-1].split('x'))
                start_ind = i + len(matched.group(0))
                i = self.pattern(start_ind, *nums)
        return sum([1 for char in s.decompressed if char != ' '])

if __name__ == '__main__':
    s = Solution()
    s.load_input('day9.txt')
    print 'Decompressed length (no whitespace): {}'.format(s.decompress())
