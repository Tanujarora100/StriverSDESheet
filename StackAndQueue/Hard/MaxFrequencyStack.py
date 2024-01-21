from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.count_map = defaultdict(int)
        self.freq_map = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = self.count_map[val] + 1
        self.count_map[val] = freq

        self.max_freq = max(self.max_freq, freq)

        self.freq_map[freq].append(val)

    def pop(self) -> int:
        if self.max_freq == 0:
            return -1

        val = self.freq_map[self.max_freq].pop()
        self.count_map[val] -= 1

        if not self.freq_map[self.max_freq]:
            self.max_freq -= 1

        return val


