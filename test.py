import unittest


class FastTest(unittest.TestCase):
    def setUp(self):
        super(FastTest, self).setUp()

    def test_test(self):
        self.assertEqual(True, True)

    def tearDown(self):
        super(FastTest, self).tearDown()


unittest.main()
