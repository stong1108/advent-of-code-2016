import numpy as np

class Solution(object):

    def __init__(self):
        self.cmds = []
        self.screen_w = 50
        self.screen_h = 6
        self.screen = np.tile('.', (self.screen_h, self.screen_w))

    def read_input(self, filename):
        with open(filename, 'r') as f:
            self.cmds = [ln.replace('x=', '').replace('y=', '').replace('by', '') for ln in f.read().splitlines()]

    def rect(self, width, height):
        self.screen[:height, :width] = '#'

    def rotate_row(self, ind, by):
        shift = self.screen_w - by
        row = self.screen[ind]
        newrow = []
        for i in xrange(self.screen_w):
            newrow.append(row[(i+shift)%self.screen_w])
        self.screen[ind] = np.array(newrow)

    def rotate_col(self, ind, by):
        shift = self.screen_h - by
        col = self.screen[:, ind]
        newcol = []
        for i in xrange(self.screen_h):
            newcol.append(col[(i+shift)%self.screen_h])
        self.screen[:, ind] = np.array(newcol)

    def do_cmd(self, cmd):
        chunks = cmd.split()
        if chunks[0] == 'rect':
            self.rect(*map(int, chunks[1].split('x')))
        elif chunks[1] == 'row':
            self.rotate_row(*map(int, chunks[-2:]))
        elif chunks[1] == 'column':
            self.rotate_col(*map(int, chunks[-2:]))

    def all_cmds(self):
        for cmd in self.cmds:
            self.do_cmd(cmd)
        return len(np.where(self.screen == '#')[0])

if __name__ == '__main__':
    s = Solution()
    s.read_input('day8.txt')
    print s.all_cmds()
