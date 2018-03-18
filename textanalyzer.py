import unittest
import os

def analyze_text(filename):
    with open(filename,mode = "r", encoding= "utf-8") as f:
        lines = 0
        chars = 0
        for line in f:
            lines += 1
            chars += len(line)
        return (lines,chars)

class TextAnalysisTexts(unittest.TestCase):
    """Tests for Analyze Text Function. """

    def setUp(self):
        """Fixture to create a file for each test case"""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, "w") as f:
            f.write('This is the first line \n'
                'this is the second line\n'
                'and the third line is here\n'
                'this is the last line in the test file with a loooooooooooong word')

    def tearDown(self):
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """ Basic test. Does the function run?? """
        analyze_text(self.filename)

    def test_line_count(self):
        self.assertEqual(analyze_text(self.filename)[0],4)

    def test_char_count(self):
        self.assertEqual(analyze_text(self.filename)[1],141)

if __name__ == "__main__":
    unittest.main()