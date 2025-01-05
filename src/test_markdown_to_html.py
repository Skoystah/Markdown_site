import unittest

from parentnode import ParentNode
from markdown_to_html import markdown_to_html


class TestMarkDownToHTML(unittest.TestCase):
    def test_markdown_to_html_heading(self):
        md = """
# This is a heading level 1

This is just some paragraph text

## This is heading level 2

With some more paragraph text
"""
        expected_html = "<div><h1>This is a heading level 1</h1><p>This is just some paragraph text</p><h2>This is heading level 2</h2><p>With some more paragraph text</p></div>"
        generated_node = markdown_to_html(md)
        print(generated_node.to_html())
        self.assertEqual(markdown_to_html(md).to_html(), expected_html)

    def test_markdown_to_html_list(self):
        md = """
# This is a heading level 1

This is just some paragraph text

* Which is followed by a list
* With no specific `order` in code

## This is heading level 2

1. This has a list
2. Ordered with **numbers**
3. From *one* to *three*
"""
        expected_html = "<div><h1>This is a heading level 1</h1><p>This is just some paragraph text</p><ul><li>Which is followed by a list</li><li>With no specific <code>order</code> in code</li></ul><h2>This is heading level 2</h2><ol><li>This has a list</li><li>Ordered with <b>numbers</b></li><li>From <i>one</i> to <i>three</i></li></ol></div>"
        generated_node = markdown_to_html(md)
        print(generated_node.to_html())
        self.assertEqual(markdown_to_html(md).to_html(), expected_html)

    def test_markdown_to_html_blockquote_code(self):
        md = """
# This is a heading level 1

This is just some paragraph text

> Which includes a famous quote
> From a famous person
> Whose name I've forgotten

## This is heading level 2

``` In this block there is some Javascript coding, handy ```
"""
        expected_html = "<div><h1>This is a heading level 1</h1><p>This is just some paragraph text</p><blockquote>Which includes a famous quote From a famous person Whose name I've forgotten</blockquote><h2>This is heading level 2</h2><pre><code> In this block there is some Javascript coding, handy </code></pre></div>"
        generated_node = markdown_to_html(md)
        print(generated_node.to_html())
        self.assertEqual(markdown_to_html(md).to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()
