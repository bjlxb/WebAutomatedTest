import unittest
from util import SelUtil


class MyTest(unittest.TestCase):

    def setUp(self):
        print('开始操作')
    
    def tearDown(self)):
        print('结束操作')

    def test_baidu(self):
        pass

    def test_002(self):
        pass

if __name__ == '__main__':
    unittest.main()