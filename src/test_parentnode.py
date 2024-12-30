import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_mandatory(self):
        testtag = "p"
        testvalue = "This is text"
        testchildren = None

        with self.assertRaises(TypeError):
            ParentNode()

#        with self.assertRaises(TypeError):
#            ParentNode(tag=testtag, children=testchildren)

        with self.assertRaises(TypeError):
            ParentNode(tag=testtag, value=testvalue, children=testchildren)

    def test_to_html_no_children(self):
        testtag = "p"
        testchildren = None
        node = ParentNode(tag=testtag, children=testchildren)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_tag(self):
        testtag = None
        testchildren = [LeafNode("b", "Bold text")]
        node = ParentNode(tag=testtag, children=testchildren)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html(self):
        testtag = "p"
        testchildren = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"), ]

        node = ParentNode(tag=testtag, children=testchildren)
        self.assertEqual(node.to_html(
        ), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

        testchildren = [
            LeafNode("b", "Bold text"),
            ParentNode("p", [
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),]),
            LeafNode(None, "Normal text"), ]

        node = ParentNode(tag=testtag, children=testchildren)
        self.assertEqual(node.to_html(
        ), "<p><b>Bold text</b><p>Normal text<i>italic text</i></p>Normal text</p>")


if __name__ == "__main__":
    unittest.main()
