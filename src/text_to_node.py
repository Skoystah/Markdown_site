from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        new_node = []
        text = node.text
        # There should be an even number of given delimiters
        if text.count(delimiter) % 2 != 0:
            raise Exception(
                f"Invalid Markdown syntax - non-matching delimiter {delimiter}"
            )

        segments = text.split(delimiter)

        for s in range(0, len(segments)):
            if len(segments[s]) > 0:
                if s % 2 == 0:  # segment outside delimiter
                    new_node.append(TextNode(segments[s], TextType.TEXT))
                else:  # segment inside delimiter
                    new_node.append(TextNode(segments[s], text_type))
        new_nodes.extend(new_node)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[(.+?)\]\((.+?)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[(.+?)\]\((.+?)\)"
    matches = re.findall(pattern, text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text

        images = extract_markdown_images(text)

        if len(images) == 0:
            new_nodes.append(node)
            continue

        for image in images:
            image_alt_text, image_url = image
            sections = text.split(f"![{image_alt_text}]({image_url})", 1)
            if len(sections) != 2:
                raise ValueError(
                    f"Invalid markdown - image section incomplete - {sections}"
                )

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(image_alt_text, TextType.IMAGE, image_url))

            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text

        links = extract_markdown_links(text)

        if len(links) == 0:
            new_nodes.append(node)
            continue

        for link in links:
            link_anchor_text, link_url = link
            sections = text.split(f"[{link_anchor_text}]({link_url})", 1)

            if len(sections) != 2:
                raise ValueError(
                    f"Invalid markdown - link section incomplete - {sections}"
                )

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(link_anchor_text, TextType.LINK, link_url))

            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_link(
            split_nodes_image(
                split_nodes_delimiter(
                    split_nodes_delimiter(
                        split_nodes_delimiter(
                            split_nodes_delimiter([text_node], "**", TextType.BOLD),
                            "_",
                            TextType.ITALIC),
                        "*",
                        TextType.ITALIC,
                        ),
                    "`",
                    TextType.CODE,
                    )
                )
    )
    return nodes
