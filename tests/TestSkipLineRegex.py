import unittest
import src
import resources.Constants as const


class TestSkipLine(unittest.TestCase):
    def setUp(self):
        self.lexer = src.Lexer()

    def testSkipLineSingleSpace(self):
        identifier = "' BSLINT_skip_line\n"
        exp_result = 'skip_line'
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEquals(result.group('command'), exp_result)
        self.assertEquals(regex_type, const.BSLINT_COMMAND)

    def testSkipLineNoSpaces(self):
        identifier = "'BSLINT_skip_line\n"
        exp_result = 'skip_line'
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEquals(result.group('command'), exp_result)
        self.assertEquals(regex_type, const.BSLINT_COMMAND)

    # Should be interpreted as a string
    def testSkipLineText(self):
        identifier = "' BSLINT_skip_line\n"
        exp_result = 'skip_line'
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEquals(result.group('command'), exp_result)
        self.assertEquals(regex_type, const.BSLINT_COMMAND)

    def testSkipLineFiveSpaces(self):
        identifier = "'     BSLINT_skip_line\n"
        exp_result = 'skip_line'
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEquals(result.group('command'), exp_result)
        self.assertEquals(regex_type, const.BSLINT_COMMAND)

    def testSkipLineWithText(self):
        identifier = "' randomText BSLINT_skip_line \n"
        result, regex = self.lexer.regex_handler(identifier)
        self.assertEquals(regex, None)

    def testSkipFile(self):
        identifier = "'BSLINT_skip_file\n"
        exp_result = 'skip_file'
        result, regex_type = self.lexer.regex_handler(identifier)
        self.assertEquals(result.group('command'), exp_result)
        self.assertEquals(regex_type, const.BSLINT_COMMAND)

