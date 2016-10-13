import unittest
import bslint.constants as const
import bslint
import bslint.utilities.regex_handler as regex_handler


class TestOperatorRegex(unittest.TestCase):

    def testAddEqual(self):
        identifier = "+="
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testSubtractEqual(self):
        identifier = "-="
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testMultiplyEqual(self):
        identifier = "*="
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testDivideEqual(self):
        identifier = "/="
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testAdd(self):
        identifier = "+"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testSubtract(self):
        identifier = "-"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testMultiply(self):
        identifier = "*"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testDivide(self):
        identifier = "/"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testExponent(self):
        identifier = "^"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testLeftShiftAssign(self):
        identifier = "<<="
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testRightShiftAssign(self):
        identifier = ">>="
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testLeftShift(self):
        identifier = "<<"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testRightShift(self):
        identifier = ">>"
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)

    def testDivideInteger(self):
        identifier = "\="
        result = regex_handler.find_match(identifier)
        self.assertEqual(result["match"].group(), identifier)
        self.assertEqual(result["token_type"], const.OPERATOR)