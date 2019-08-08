import unittest

from practice3 import MyHashMap

class Test(unittest.TestCase):

    def test(self):
        print('Testing Practice')

        hashMap = MyHashMap()
        hashMap.put(1, 1)
        hashMap.put(2, 2)
        self.assertEqual(hashMap.get(1), 1)
        print('Test 1 Successful')

        self.assertEqual(hashMap.get(3), -1)
        print('Test 2 Successful')
        hashMap.put(2, 1)
        hashMap.remove(2)
        self.assertEqual(hashMap.get(2), -1)
        print('Test 3 Successful')

if __name__ == '__main__':
    unittest.main()
