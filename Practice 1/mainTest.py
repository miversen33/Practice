import unittest
import practice1 as practice

testMatrix = [['F', 'A', 'C', 'I'],
              ['O', 'B', 'Q', 'P'],
              ['A', 'N', 'O', 'B'],
              ['M', 'A', 'S', 'S']]
test1 = 'FOAM'
test2 = 'MASS'
test3 = 'FACE'

class Test(unittest.TestCase):

    def test(self):
        print('Testing Practice')
        self.assertEqual(practice.parse(testMatrix, test1), True)
        print('Test 1 Successful')
        self.assertEqual(practice.parse(testMatrix, test2), True)
        print('Test 2 Successful')
        self.assertEqual(practice.parse(testMatrix, test3), False)
        print('Test 3 Successful')

if __name__ == '__main__':
    unittest.main()
