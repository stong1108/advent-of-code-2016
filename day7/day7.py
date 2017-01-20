class Solution(object):

    def __init__(self):
        self.lines = []
        self.count = 0

    def read_input(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()

    def _is_ABBA(self, string):
        if len(set(string)) == 2:
            sub = string[:2]
            return string == sub + sub[::-1]
        return False

    def check_line(self, line):
        chunks = line.replace('[', ' ', len(line)).replace(']', ' ', len(line)).split()
        outsides, insides = [], []
        for i, chunk in enumerate(chunks):
            if i % 2 == 0:
                outsides.append(chunk)
            else:
                insides.append(chunk)
        outside_check = any([self._check_chunk(chunk, True) for chunk in outsides])
        inside_check = all([self._check_chunk(chunk, False) for chunk in insides])
        self.count += int(outside_check and inside_check)

    def _check_chunk(self, chunk, outside):
        abba = False
        for i in xrange(len(chunk)-3):
            string = chunk[i:i+4]
            result = self._is_ABBA(string)
            if outside and result:
                return True
            elif not outside:
                abba = abba or result
        if outside:
            return False
        return not abba

    def count_ips(self):
        for line in self.lines:
            self.check_line(line)
        print self.count

if __name__ == '__main__':
    s = Solution()
    s.read_input('day7.txt')
    s.count_ips()
