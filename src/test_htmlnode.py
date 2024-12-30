import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError): node.to_html()

    def test_props_to_html(self):
        html_props = {
            "href": "https://www.google.com", 
            "target": "_blank",
                    }
        node = HTMLNode(tag="Testtag", props=html_props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        testtag = "Testtag"
        testchildren = "Testchildren"
        testvalue = "Testvalue"
        html_props = {
            "href": "https://www.google.com", 
            "target": "_blank",
                    }
        node = HTMLNode(tag=testtag, props=html_props, children = testchildren, value=testvalue)
        self.assertEqual(f"HTMLNode(tag: {testtag} | value: {testvalue} | children: {testchildren} | props: {html_props})", repr(node))

if __name__ == "__main__":
    unittest.main()


