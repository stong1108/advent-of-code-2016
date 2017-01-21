import numpy as np
import pprint

class Solution(object):

    def __init__(self):
        self.cmds = []
        self.screen_w = 50
        self.screen_h = 6
        self.screen = np.tile(' ', (self.screen_h, self.screen_w))

    def read_input(self, filename):
        with open(filename, 'r') as f:
            self.cmds = [ln.replace('x=', '').replace('y=', '').replace('by', '') for ln in f.read().splitlines()]

    def rect(self, width, height):
        self.screen[:height, :width] = '#'

    def rotate(self, way, ind, by):
        d_way = {'row': (self.screen_w, '{}, :'), 'column': (self.screen_h, ':, {}')}
        dim, inds = d_way[way]
        inds = inds.format(ind)

        old = eval('self.screen[{}]'.format(inds))
        new = []
        for i in xrange(dim):
            new.append(old[(i + dim - by) % dim])

        exec('self.screen[{}] = np.array(new)'.format(inds))

    def do_cmd(self, cmd):
        chunks = cmd.split()
        if chunks[0] == 'rect':
            self.rect(*map(int, chunks[1].split('x')))
        else:
            self.rotate(*([chunks[1]] + map(int, chunks[2:])))

    def all_cmds(self):
        for cmd in self.cmds:
            self.do_cmd(cmd)

        for row in self.screen:
            print ''.join(row)

        print 'Number of lit pixels: {}'.format(len(np.where(self.screen == '#')[0]))

if __name__ == '__main__':
    s = Solution()
    s.read_input('day8.txt')
    s.all_cmds()
