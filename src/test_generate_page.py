import unittest

from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):

    # Test 1: Simple H1 header in a single block
    def test_simple_h1(self):
        markdown = "# Simple Title"
        self.assertEqual(extract_title(markdown), "Simple Title")

    # Test 2: Multiple blocks, H1 in the first block
    def test_multiple_blocks_first_h1(self):
        markdown = "# First Title\n\nSome text\n\n# Second Title"
        self.assertEqual(extract_title(markdown), "First Title")

    # Test 3: H1 in a later block
    def test_later_h1(self):
        markdown = "Some introductory text\n\n# Actual Title\n\nMore text"
        self.assertEqual(extract_title(markdown), "Actual Title")

    # Test 4: No H1 header present
    def test_no_h1(self):
        markdown = "Just paragraphs.\n\nAnother paragraph."
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "no h1")

    # Test 5: Empty markdown
    def test_empty(self):
        markdown = ""
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "no h1")

    # Test 6: Markdown with only spaces
    def test_only_spaces(self):
        markdown = "   \n\n   "
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "no h1")

    # Test 7: H1 header followed by text in the same block
    def test_header_with_text(self):
        markdown = "# Title followed by text\nThis is still part of the block."
        self.assertEqual(extract_title(markdown), "Title followed by text This is still part of the block.")

    # Test 8: H1 header with extra spaces
    def test_extra_spaces(self):
        markdown = "#   Title with spaces  "
        self.assertEqual(extract_title(markdown), "Title with spaces")

    # Test 9: H2 header (##)
    def test_h2(self):
        markdown = "## Subtitle"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "no h1")

    # Test 10: H1 after H2
    def test_h1_after_h2(self):
        markdown = "## Subtitle\n\n# Main Title"
        self.assertEqual(extract_title(markdown), "Main Title")

    # Test 11: Header without space after "#"
    def test_no_space_after_hash(self):
        markdown = "#NoSpace"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "no h1")

    # Test 12: H1 header with trailing "#"
    def test_trailing_hash(self):
        markdown = "# Title #"
        self.assertEqual(extract_title(markdown), "Title #")

    # Test 13: H1 not on the first line of a block
    def test_h1_not_first_line(self):
        markdown = "First line\n# Title"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "no h1")

if __name__ == '__main__':
    unittest.main()