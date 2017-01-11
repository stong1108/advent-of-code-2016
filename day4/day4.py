class Solution(object):

    def __init__(self):
        self.sectorsum = 0
        self.rooms = []

    def read_input(self, filename):
        f = open(filename, 'r')
        self.rooms = [ln.strip('\n') for ln in f.readlines()]

    def _split_room_info(self, room):
        checksum = room[-6:-1]
        lasthyphenind = -room[::-1].index('-')
        sectorid = int(room[lasthyphenind:-7])
        letters = room[:lasthyphenind-1].replace('-', '', len(room))
        return checksum, sectorid, letters

    def is_real_room(self, room):
        checksum, sectorid, letters = self._split_room_info(room)
        mysum = ''
        d = {}
        for char in letters:
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

    def check_all_rooms(self):
        for room in self.rooms:
            self.is_real_room(room)
        print self.sectorsum

if __name__ == '__main__':
    s = Solution()
    s.read_input('day4.txt')
    s.check_all_rooms()
