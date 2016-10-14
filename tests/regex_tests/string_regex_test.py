import os
import unittest

import bslint
import bslint.constants as const
import bslint.lexer.regex_handler as regex_handler
from bslint.lexer.lexer import Lexer as Lexer
from bslint.utilities.token import Token as Token


class TestStringRegex(unittest.TestCase):
    TOKENS = 'Tokens'

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)

        cls.string_file = open(os.path.join(this_dir, "../resources/lexing_test_files/basic-string-assignment.txt"), "r+").read()
        cls.multi_line_file = open(os.path.join(this_dir, "../resources/styling_test_files/multiline-assignment.txt"),"r+").read()

    def testString(self):
        test_string = '"test123ID"'
        result = regex_handler.find_match(test_string)
        self.assertEqual(result["match"].group(), test_string)
        self.assertEqual(result["token_lexer_type"], const.STRING)
        self.assertEqual(result["token_parser_type"], const.VALUE)

    def testUnclosedQuotes(self):
        test_string = '"test123ID\n'
        with self.assertRaises(ValueError):
            result = regex_handler.find_match(test_string)
            self.assertEqual(result["match"].group(), test_string)
            self.assertEqual(result["token_lexer_type"], const.STRING)
            self.assertEqual(result["token_parser_type"], const.VALUE)

    def testVariableAssignmentString(self):
        exp_result = [Token('myString', const.ID, const.ID, 1), Token('=', const.OPERATOR, const.EQUALS, 1),
                      Token('words', const.STRING, const.VALUE, 1)]
        result = Lexer().lex(self.string_file)
        self.assertEqual(result[self.TOKENS], exp_result)

    def testDoubleQuoteString(self):
        test_string = '""""'
        exp_result = '""'
        result = regex_handler.find_match(test_string)
        self.assertEqual(result["match"].group(1), exp_result)
        self.assertEqual(result["token_lexer_type"], const.STRING)
        self.assertEqual(result["token_parser_type"], const.VALUE)

    def testMultilineAssignment(self):
        exp_result = [Token('myString', const.ID, const.ID, 1), Token('=', const.OPERATOR, const.EQUALS, 1),
                      Token("words", const.STRING, const.VALUE, 1),
                      Token('test_String', const.ID, const.ID, 2), Token('=', const.OPERATOR, const.EQUALS, 2),
                      Token("this is words", const.STRING, const.VALUE, 2)]
        result = Lexer().lex(self.multi_line_file)
        self.assertEqual(result[self.TOKENS], exp_result)