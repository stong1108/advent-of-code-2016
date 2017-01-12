import pprint

class Solution(object):

    def __init__(self):
        self.sectorsum = 0
        self.rooms = []
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.secretmessage = {}

    def read_input(self, filename):
        f = open(filename, 'r')
        self.rooms = [ln.strip('\n') for ln in f.readlines()]

    def split_room_info(self, room):
        checksum = room[-6:-1]
        lasthyphenind = -room[::-1].index('-')
        sectorid = int(room[lasthyphenind:-7])
        letters = room[:lasthyphenind-1]
        return checksum, sectorid, letters

    def is_real_room(self, checksum, sectorid, letters):
        mysum = ''
        d = {}
        for char in letters:
            if char != '-':
                d[char] = d.get(char, 0) + 1
        top_counts = sorted(d.values())[::-1]
        ind = 0
        while ind < 5:
            cnt = top_counts[ind]
            results = sorted([k for k in d.keys() if d[k] == cnt])
            n = sum([1 for _ in top_counts[ind:5] if _ == cnt])
            mysum += ''.join(results[:n])
            ind += n
        if checksum == mysum:
            self.sectorsum += sectorid

    def decipher(self, sectorid, letters):
        n_rotations = sectorid % 26
        rotatedletters = ''
        for char in letters:
            if char == '-':
                rotatedletters += ' '
            else:
                ind = self.alphabet.index(char)
                rotatedind = (ind + n_rotations) % 26
                rotatedletters += self.alphabet[rotatedind]
        self.secretmessage[sectorid] = rotatedletters

    def process_rooms(self):
        for room in self.rooms:
            checksum, sectorid, letters = self.split_room_info(room)
            self.is_real_room(checksum, sectorid, letters)
            self.decipher(sectorid, letters)
        for i, v in enumerate(self.secretmessage.values()):
            if 'northpole' in v:
                return self.secretmessage.keys()[i]

if __name__ == '__main__':
    s = Solution()
    s.read_input('day4.txt')
    northpole_id = s.process_rooms()
    print 'Sum of sector IDs of real rooms: {}'.format(s.sectorsum)
    print 'Sector ID of room for northpole object storage: {}'.format(northpole_id)
    # pprint.pprint(s.secretmessage)
