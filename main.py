import unittest
class CRC32():
    def __init__(self):
        self._table = []
        for i in range(256):
            tmp = i
            for j in range(8):
                tmp = (tmp>>1) ^ 0xedb88320 if (tmp & 1) else (tmp >> 1)
            self._table.append(tmp)
    def get_crc(self, in_str):
        item = 0xffffffff
        for c in in_str:
            item = (self._table[(item ^ ord(c))& 0xff]) ^ (item>>8)
        return hex(item ^ 0xffffffff)

class TestCRC32(unittest.TestCase):
    def setUp(self):
        self.crc32 = CRC32()

    def test_crc(self):
        f = open('crc32.txt', 'r')
        text = f.read()
        expected_crc = '0xcbf43926'
        actual_crc = self.crc32.get_crc(text)
        self.assertEqual(actual_crc, expected_crc)
        f.close()
if __name__ == '__main__':
     unittest.main()