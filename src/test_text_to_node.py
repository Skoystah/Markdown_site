import unittest

from textnode import TextNode, TextType
from text_to_node import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)


class TestTextToNode(unittest.TestCase):
    def test_split_nodes_error(self):
        node1 = TextNode("This is text with a `code block word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node1], "`", TextType.TEXT)

    def test_split_nodes(self):
        node1 = TextNode("This is text with a `code block` word", TextType.CODE)
        expected_nodes1 = [
            TextNode("This is text with a `code block` word", TextType.CODE)
        ]
        self.assertEqual(
            split_nodes_delimiter([node1], "`", TextType.CODE), expected_nodes1
        )

        node2 = TextNode("This is text with a `code block` word", TextType.TEXT)
        expected_nodes2 = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(
            split_nodes_delimiter([node2], "`", TextType.CODE), expected_nodes2
        )

        node3 = TextNode(
            "**This is** text with a **bold word** written in *italic*", TextType.TEXT
        )
        expected_nodes3 = [
            TextNode("This is", TextType.BOLD),
            TextNode(" text with a ", TextType.TEXT),
            TextNode("bold word", TextType.BOLD),
            TextNode(" written in *italic*", TextType.TEXT),
        ]
        new_nodes3 = split_nodes_delimiter([node3], "**", TextType.BOLD)
        self.assertEqual(new_nodes3, expected_nodes3)

        expected_nodes4 = [
            TextNode("This is", TextType.BOLD),
            TextNode(" text with a ", TextType.TEXT),
            TextNode("bold word", TextType.BOLD),
            TextNode(" written in ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
        ]
        new_nodes4 = split_nodes_delimiter(new_nodes3, "*", TextType.ITALIC)
        self.assertEqual(new_nodes4, expected_nodes4)

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_images = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        images = extract_markdown_images(text)
        self.assertEqual(images, expected_images)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected_links = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        links = extract_markdown_links(text)
        # print(extract_markdown_links(text))
        self.assertEqual(links, expected_links)

    def test_split_image(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        # print(
        #    f"test-split-image - new nodes: {new_nodes} \n| expected: {expected_nodes}"
        # )
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected_nodes = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        # print(f"test-split-link - new nodes: {new_nodes}")
        self.assertEqual(new_nodes, expected_nodes)

    def test_text_to_node(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        new_nodes = text_to_textnodes(text)
        print(new_nodes)
        self.assertEqual(new_nodes, expected_nodes)


if __name__ == "__main__":
    unittest.main()
