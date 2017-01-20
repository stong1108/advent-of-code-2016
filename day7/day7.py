class Solution(object):

    def __init__(self):
        self.lines = []
        self.count_TLS = 0
        self.count_SSL = 0

    def read_input(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()

    def _is_ABBA(self, string):
        if len(set(string)) == 2:
            sub = string[:2]
            return string == sub + sub[::-1]
        return False

    def _is_ABA(self, string):
        return len(set(string)) == 2 and string[0] == string[-1]

    def _split_chunks(self, line):
        chunks = line.replace('[', ' ', len(line)).replace(']', ' ', len(line)).split()
        outsides, insides = [], []
        for i, chunk in enumerate(chunks):
            if i % 2 == 0:
                outsides.append(chunk)
            else:
                insides.append(chunk)
        return outsides, insides

    def _get_aba_set(self, lst, outside):
        s = set()
        for chunk in lst:
            for i in xrange(len(chunk)-2):
                string = chunk[i:i+3]
                if self._is_ABA(string):
                    if outside:
                        s.add(string)
                    else:
                        s.add(string[1]+string[0]+string[1])
        return s

    def _check_abba(self, chunk, outside):
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

    def check_line(self, line):
        outsides, insides = self._split_chunks(line)

        outside_check = any([self._check_abba(chunk, True) for chunk in outsides])
        inside_check = all([self._check_abba(chunk, False) for chunk in insides])
        self.count_TLS += int(outside_check and inside_check)

        outside_set = self._get_aba_set(outsides, True)
        inside_set = self._get_aba_set(insides, False)
        self.count_SSL += int(len(outside_set.intersection(inside_set)) != 0)

    def count_ips(self):
        for line in self.lines:
            self.check_line(line)

if __name__ == '__main__':
    s = Solution()
    s.read_input('day7.txt')
    s.count_ips()
    print '# of IPs that support TLS: {}'.format(s.count_TLS)
    print '# of IPs that support SSL: {}'.format(s.count_SSL)
