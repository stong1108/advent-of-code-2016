class Solution2(object):

    def __init__(self):
        self.keypad = ['  1  ', ' 234 ', '56789', ' ABC ', '  D  ']
        self.coord = [2, 0] # [row, col], start at 5
        self.moves = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
        self.code = ''

    def read_input(self, filename):
        with open(filename, 'r') as f:
            self.lines = f.readlines()

    def get_one_num(self, line):
        for char in line.strip('\n'):
            move = self.moves[char]
            result = [sum(_) for _ in zip(self.coord, move)]
            if any([num not in range(0, 5) for num in result]):
                continue
            elif self.keypad[result[0]][result[1]] == ' ':
                continue
            else:
                self.coord = result
        self.code += self.keypad[self.coord[0]][self.coord[1]]

    def get_code(self):
        for line in self.lines:
            self.get_one_num(line)
        print self.code

if __name__ == "__main__":
    s2 = Solution2()
    s2.read_input('day2.txt')
    s2.get_code()
