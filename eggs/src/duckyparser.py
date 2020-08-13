# Modified version of duckyparser.py
#https://github.com/insecurityofthings/jackit/blob/master/jackit/duckyparser.py
class DuckyParser(object):

    hid_map = {
        '':           [0, 0],
        'GUI':        [0, 8],
        'ENTER':      [40, 0]
    }

    blank_entry = {
        "mod": 0,
        "hid": 0,
        "char": '',
        "sleep": 0
    }

    keys = {
    " ": [44, 0],
    "-": [45, 0],
    ".": [55, 0],
    "/": [56, 0],
    "0": [39, 0],
    "1": [30, 0],
    "2": [31, 0],
    "3": [32, 0],
    "4": [33, 0],
    "5": [34, 0],
    "6": [35, 0],
    "7": [36, 0],
    "8": [37, 0],
    "9": [38, 0],
    ":": [51, 2],
    "A": [4, 2],
    "B": [5, 2],
    "C": [6, 2],
    "D": [7, 2],
    "E": [8, 2],
    "F": [9, 2],
    "G": [10, 2],
    "H": [11, 2],
    "I": [12, 2],
    "J": [13, 2],
    "K": [14, 2],
    "L": [15, 2],
    "M": [16, 2],
    "N": [17, 2],
    "O": [18, 2],
    "P": [19, 2],
    "Q": [20, 2],
    "R": [21, 2],
    "S": [22, 2],
    "T": [23, 2],
    "U": [24, 2],
    "V": [25, 2],
    "W": [26, 2],
    "X": [27, 2],
    "Y": [28, 2],
    "Z": [29, 2],
    "a": [4, 0],
    "b": [5, 0],
    "c": [6, 0],
    "d": [7, 0],
    "e": [8, 0],
    "f": [9, 0],
    "g": [10, 0],
    "h": [11, 0],
    "i": [12, 0],
    "j": [13, 0],
    "k": [14, 0],
    "l": [15, 0],
    "m": [16, 0],
    "n": [17, 0],
    "o": [18, 0],
    "p": [19, 0],
    "q": [20, 0],
    "r": [21, 0],
    "s": [22, 0],
    "t": [23, 0],
    "u": [24, 0],
    "v": [25, 0],
    "w": [26, 0],
    "x": [27, 0],
    "y": [28, 0],
    "z": [29, 0],
}

    def __init__(self, attack_script):
        key_mapping = self.keys.copy()
        self.hid_map.update(key_mapping)
        self.script = attack_script.split("\n")

    def char_to_hid(self, char):
        return self.hid_map[char]

    def parse(self):
        entries = []

        for line in self.script:
            if line.startswith("GUI") or line.startswith('WINDOWS'):
                entry = self.blank_entry.copy()
                if line.find(' ') == -1:
                    entry['char'] = ''
                else:
                    entry['char'] = line.split()[1]
                entry['hid'], mod = self.char_to_hid(entry['char'])
                entry['mod'] = 8 | mod
                entries.append(entry)

            elif line.startswith("STRING"):
                for char in " ".join(line.split()[1:]):
                    entry = self.blank_entry.copy()
                    entry['char'] = char
                    entry['hid'], entry['mod'] = self.char_to_hid(char)
                    entries.append(entry)

            elif line.startswith("DELAY"):
                entry = self.blank_entry.copy()
                entry['sleep'] = line.split()[1]
                entries.append(entry)

            elif line.startswith("ENTER"):
                entry = self.blank_entry.copy()
                entry['char'] = "\n"
                entry['hid'], entry['mod'] = self.char_to_hid('ENTER')
                entries.append(entry)

            elif len(line) == 0:
                pass

            else:
                print("CAN'T PROCESS... %s" % line)

        return entries
