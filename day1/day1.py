class BlockCounter(object):

    def __init__(self):
        self.loc = (0, 0)
        self.commands = None
        self.dir_len = [0, 0, 0, 0] # [north, east, south, west]
        self.curr_dir = 0

    def read_input(self, filename):
        f = open(filename, 'r')
        self.commands = f.read().split(', ')

    def one_command(self, command):
        command_dir = command[:1]
        command_len = int(command[1:])
        if command_dir == 'R':
            self.curr_dir = (self.curr_dir + 1) % 4
        elif command_dir == 'L':
            self.curr_dir = (self.curr_dir - 1) % 4
        self.dir_len[self.curr_dir] += command_len

    def follow_commands(self):
        for cmd in self.commands:
            self.one_command(cmd)
        print abs(self.dir_len[0] - self.dir_len[2]) + abs(self.dir_len[1] - self.dir_len[3])

if __name__ == "__main__":
    bc = BlockCounter()
    bc.read_input('day1.txt')
    bc.follow_commands()
