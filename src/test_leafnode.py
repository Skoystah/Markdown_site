import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_mandatory(self):
        with self.assertRaises(TypeError):
            LeafNode()

    def test_withchildren(self):
        testtag = "Testtag"
        testchildren = "Testchildren"
        testvalue = "Testvalue"
        html_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        with self.assertRaises(TypeError):
            LeafNode(tag=testtag, value=testvalue,
                     children=testchildren, props=html_props)

    def test_to_html_no_value(self):
        testtag = "p"
        testvalue = None
        node = LeafNode(tag=testtag, value=testvalue)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_tag(self):
        testtag = None
        testvalue = "This is a paragraph of text."
        node = LeafNode(tag=testtag, value=testvalue)
        self.assertEqual(node.to_html(),
                         'This is a paragraph of text.')

    def test_to_html_props(self):
        testtag = "a"
        testvalue = "Click me!"
        html_props = {
            "href": "https://www.google.com"
        }
        node = LeafNode(tag=testtag, value=testvalue, props=html_props)
        self.assertEqual(node.to_html(),
                         '<a href="https://www.google.com">Click me!</a>')


if __name__ == "__main__":
    unittest.main()
