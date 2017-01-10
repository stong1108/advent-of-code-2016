class KeypadCode(object):

    def __init__(self):
        self.curr_num = 5
        self.curr_row = 1
        self.lines = None
        self.code = ''
        self.moves = {'U': -3, 'D': 3, 'L': -1, 'R': 1}

    def read_input(self, filename):
        f = open(filename, 'r')
        self.lines = f.readlines()

    def get_one_num(self, line):
        for char in line.strip('\n'):
            move = self.moves[char]
            result = self.curr_num + move
            result_row = (result - 1) / 3
            if result not in range(1, 10):
                continue
            elif abs(move) == 1 and self.curr_row != result_row:
                continue
            else:
                self.curr_num = result
                self.curr_row = result_row
        self.code += str(self.curr_num)

    def get_code(self):
        for line in self.lines:
            self.get_one_num(line)
        print self.code

if __name__ == "__main__":
    KC = KeypadCode()
    KC.read_input('day2.txt')
    KC.get_code()
