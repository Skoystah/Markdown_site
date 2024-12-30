import unittest

from markdown_to_blocks import (
    markdown_to_blocks,
    block_to_blocktype,
)
from block import BlockType


class TestMarkDownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
        """
        blocks = markdown_to_blocks(text)
        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item""",
        ]
        self.assertEqual(blocks, expected_blocks)

    def test_block_to_blocktype(self):
        block = "### This is a heading.\nWith multiple lines"
        self.assertEqual(block_to_blocktype(block), BlockType.HEADING.value)

        block = "###This is not a heading.\nWith multiple lines"
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH.value)

        block = "``` This is a code block\n with multiple lines  ```"
        self.assertEqual(block_to_blocktype(block), BlockType.CODE.value)

        block = "` This is a code block\n with multiple lines  `"
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH.value)

        block = "> This is a quote block\n> with multiple lines"
        self.assertEqual(block_to_blocktype(block), BlockType.QUOTE.value)

        block = "> This is a quote block\n with multiple lines"
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH.value)

        block = "* This is an unordered list\n- with muyltiple lines\n* and multiple bullets"
        self.assertEqual(block_to_blocktype(block), BlockType.UNORDERED_LIST.value)

        block = (
            "* This is an unordered list\nwith muyltiple lines\nand multiple bullets"
        )
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH.value)

        block = (
            "1. this is an ordered list\n2. with multiple lines\n3. from one to three"
        )
        self.assertEqual(block_to_blocktype(block), BlockType.ORDERED_LIST.value)

        block = (
            "1. this is an ordered list\n3. with multiple lines\n4. from one to three"
        )
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH.value)

        block = "This is a regular paragraph isnt it"
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH.value)


if __name__ == "__main__":
    unittest.main()
