import hashlib

class Solution(object):

    def __init__(self, door_id):
        self.door_id = door_id
        self.password1 = ''
        self.password2 = ['_']*8

    def decrypt1(self):
        ind = 0
        while len(self.password1) != 8:
            hashed = hashlib.md5(self.door_id + str(ind)).hexdigest()
            if hashed.startswith('00000'):
                self.password1 += hashed[5]
            ind += 1
        return self.password1

    def decrypt2(self):
        ind = 0
        print '_'*8
        while '_' in self.password2:
            hashed = hashlib.md5(self.door_id + str(ind)).hexdigest()
            if hashed.startswith('00000') and hashed[5].isdigit():
                loc = int(hashed[5])
                char = hashed[6]
                if loc < 8 and self.password2[loc] == '_':
                    self.password2[loc] = char
                    print ''.join(self.password2) # visualize
            ind += 1
        return ''.join(self.password2)

if __name__ == '__main__':
    with open('day5.txt', 'r') as f:
        door_id = f.read().strip()
    s = Solution(door_id)
    print 'Password 1: ' + s.decrypt1()
    print 'Password 2: ' + s.decrypt2()
