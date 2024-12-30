import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode(
            "This is a text node", TextType.BOLD, "https://boot.dev/unit-test"
        )
        self.assertEqual(
            "TextNode(This is a text node, bold, https://boot.dev/unit-test)",
            repr(node),
        )

    def test_text_to_html(self):
        node = TextNode(
            "This is a text node", TextType.BOLD, "https://boot.dev/unit-test"
        )
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), "<b>This is a text node</b>")
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()
