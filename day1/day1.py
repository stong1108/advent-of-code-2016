class Solution(object):

    def __init__(self):
        self.loc = (0, 0)
        self.commands = None
        self.dir_len = [0, 0, 0, 0] # [north, east, south, west]
        self.curr_dir = 0
        self.seen = set()
        self.seen.add((0, 0)) # in xy coord
        self.start = None

    def read_input(self, filename):
        with open(filename, 'r') as f:
            self.commands = f.read().split(', ')

    def one_command(self, command):
        command_dir = command[:1]
        command_len = int(command[1:])

        if command_dir == 'R':
            self.curr_dir = (self.curr_dir + 1) % 4
        elif command_dir == 'L':
            self.curr_dir = (self.curr_dir - 1) % 4

        if self.start:
            self.dir_len[self.curr_dir] += command_len
        else:
            while command_len != 0:
                command_len -= 1
                self.dir_len[self.curr_dir] += 1
                curr_loc = (self.dir_len[0] - self.dir_len[2], self.dir_len[1] - self.dir_len[3])
                if curr_loc in self.seen:
                    self.start = curr_loc
                else:
                    self.seen.add(curr_loc)

    def follow_commands(self):
        for cmd in self.commands:
            self.one_command(cmd)

        endloc = abs(self.dir_len[0] - self.dir_len[2]) + abs(self.dir_len[1] - self.dir_len[3])
        startloc = abs(self.start[0]) + abs(self.start[1])
        print 'End location: {} blocks away'.format(endloc)
        print 'Start location: {} blocks away'.format(startloc)

if __name__ == "__main__":
    s = Solution()
    s.read_input('day1.txt')
    s.follow_commands()
