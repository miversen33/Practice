import unittest
import practice2 as practice

test1Input  = "the sky is blue"
test2Input  = "  hello  world! "
test3Input  = "a good example"
test1Output = "blue is sky the"
test2Output = "world! hello"
test3Output = "example good a"

class Test(unittest.TestCase):

    def test(self):
        print('Testing Practice')
        self.assertEqual(practice.sort(test1Input), test1Output)
        print('Test 1 Successful')
        self.assertEqual(practice.sort(test2Input), test2Output)
        print('Test 2 Successful')
        self.assertEqual(practice.sort(test3Input), test3Output)
        print('Test 3 Successful')

if __name__ == '__main__':
    unittest.main()
