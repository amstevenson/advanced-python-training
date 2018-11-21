import unittest
from python_training.examples.ch9UnitTesting import myClasses


class TestPoint(unittest.TestCase):

    def testMoveBy2(self):
        test_point = myClasses.Point(6, 4)
        test_point.move_by(2, 2)
        self.assertEqual(test_point.where_am_i(), "8, 6")

    def testMoveBy3(self):
        test_point3d = myClasses.Point3d(1, 2, 3)
        test_point3d.move_by(1, 1)
        self.assertEqual(test_point3d.where_am_i(), "2, 3, 3")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestPoint('testMoveBy2'))
    suite.addTest(TestPoint('testMoveBy3'))
    return suite

if __name__ == '__main__':
    mySuite = suite()
    unittest.TextTestResult(verbosity=0).run(mySuite)
