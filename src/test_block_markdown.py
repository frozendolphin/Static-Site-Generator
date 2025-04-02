import unittest

from block_markdown import (
    markdown_to_blocks, 
    BlockType,
    block_to_block_type
)

class MarkdownToBlockTest(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_single_block(self):
        """Test with a single block of markdown"""
        markdown = "This is a single paragraph"
        result = markdown_to_blocks(markdown)
        expected = ["This is a single paragraph"]
        self.assertEqual(result, expected)

    def test_multiple_blocks(self):
        """Test with multiple blocks separated by double newlines"""
        markdown = "First paragraph\n\nSecond paragraph\n\nThird paragraph"
        result = markdown_to_blocks(markdown)
        expected = ["First paragraph", "Second paragraph", "Third paragraph"]
        self.assertEqual(result, expected)

    def test_empty_string(self):
        """Test with empty string"""
        markdown = ""
        result = markdown_to_blocks(markdown)
        expected = []
        self.assertEqual(result, expected)

    def test_single_newlines(self):
        """Test with single newlines (should be treated as one block)"""
        markdown = "Line one\nLine two\nLine three"
        result = markdown_to_blocks(markdown)
        expected = ["Line one\nLine two\nLine three"]
        self.assertEqual(result, expected)

    def test_extra_newlines(self):
        """Test with multiple consecutive newlines"""
        markdown = "First block\n\n\n\nSecond block\n\n\nThird block"
        result = markdown_to_blocks(markdown)
        expected = ["First block", "Second block", "Third block"]
        self.assertEqual(result, expected)

    def test_leading_trailing_newlines(self):
        """Test with leading and trailing newlines"""
        markdown = "\n\nFirst block\n\nSecond block\n\n"
        result = markdown_to_blocks(markdown)
        expected = ["First block", "Second block"]
        self.assertEqual(result, expected)

    def test_whitespace_blocks(self):
        """Test with blocks containing only whitespace"""
        markdown = "Real block\n\n  \n\nAnother block"
        result = markdown_to_blocks(markdown)
        expected = ["Real block", "Another block"]
        self.assertEqual(result, expected)

    def test_mixed_content(self):
        """Test with mixed markdown content"""
        markdown = "# Heading\nText here\n\n* List item 1\n* List item 2\n\nParagraph"
        result = markdown_to_blocks(markdown)
        expected = [
            "# Heading\nText here",
            "* List item 1\n* List item 2",
            "Paragraph"
        ]
        self.assertEqual(result, expected)

    def test_trailing_whitespace(self):
        """Test with trailing whitespace in blocks"""
        markdown = "First block  \n\nSecond block\t\n\nThird block"
        result = markdown_to_blocks(markdown)
        expected = ["First block", "Second block", "Third block"]
        self.assertEqual(result, expected)

    def test_single_line_with_newlines(self):
        """Test with single line containing embedded newlines"""
        markdown = "One\ntwo\nthree\n\nFour"
        result = markdown_to_blocks(markdown)
        expected = ["One\ntwo\nthree", "Four"]
        self.assertEqual(result, expected)
        
class TestBlockToBlockType(unittest.TestCase):
    
    def test_heading_single_hash(self):
        """Test heading with single #"""
        block = "# Heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_heading_multiple_hash(self):
        """Test heading with multiple #"""
        block = "#### Heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_code_block(self):
        """Test code block starting with triple backticks"""
        block = "```python\nprint('hello')\n```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)

    def test_quote_block(self):
        """Test quote block starting with >"""
        block = "> This is a quote"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_unordered_list(self):
        """Test unordered list starting with -"""
        block = "- Item 1"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        """Test ordered list starting with 1."""
        block = "1. First item"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_paragraph(self):
        """Test regular paragraph"""
        block = "This is a normal paragraph"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_heading_no_space(self):
        """Test heading without space after # (still counts as heading)"""
        block = "#Heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_multi_line_quote(self):
        """Test multi-line quote block"""
        block = "> Line 1\n> Line 2"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_multi_line_unordered_list(self):
        """Test multi-line unordered list"""
        block = "- Item 1\n- Item 2"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_multi_line_ordered_list(self):
        """Test multi-line ordered list"""
        block = "1. Item 1\n2. Item 2"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_paragraph_with_special_chars(self):
        """Test paragraph starting with other special characters"""
        block = "*not a list* because no space"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_empty_block(self):
        """Test empty block (should be paragraph)"""
        block = ""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_code_block_with_language(self):
        """Test code block with language specification"""
        block = "```python\ncode here\n```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)