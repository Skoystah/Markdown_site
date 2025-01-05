from markdown_to_blocks import markdown_to_blocks, block_to_blocktype
from block import BlockType
from parentnode import ParentNode
from text_to_node import text_to_textnodes
import string


def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = []
    for block in blocks:
        html_blocks.append(block_to_html_node(block))

    return ParentNode("div", html_blocks)


def block_to_html_node(block):
    block_type = block_to_blocktype(block)

    match block_type:
        case BlockType.HEADING.value:
            return make_heading_node(block)
        case BlockType.CODE.value:
            return make_code_node(block)
        case BlockType.QUOTE.value:
            return make_quote_node(block)
        case BlockType.PARAGRAPH.value:
            return make_paragraph_node(block)
        case BlockType.UNORDERED_LIST.value:
            return make_unordered_list(block)
        case BlockType.ORDERED_LIST.value:
            return make_ordered_list(block)
        case _:
            raise ValueError(
                f"block not yet supported : {block_type} - {block}")


def text_to_children(text):
    textnodes = text_to_textnodes(text)
    htmlnodes = []
    for node in textnodes:
        htmlnodes.append(node.text_node_to_html_node())

    return htmlnodes


def make_heading_node(block):
    prefix, text = block.split(" ", 1)

    match prefix:
        case "#":
            tag = "h1"
        case "##":
            tag = "h2"
        case "###":
            tag = "h3"
        case "####":
            tag = "h4"
        case "#####":
            tag = "h5"
        case "######":
            tag = "h6"
        case _:
            raise ValueError(f"incorrect heading {block}")

    children = text_to_children(text)
    return ParentNode(tag, children)


def make_code_node(block):
    if not block.startswith("```") and block.endswith("```"):
        raise ValueError(f"Invalid code block: {block}")

    text = block.strip("`")
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def make_quote_node(block):
    lines = block.split("\n")
    stripped_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError(f"Invalid quote block: {block}")

        stripped_lines.append(line.lstrip(">").strip())

    quote = " ".join(stripped_lines)
    children = text_to_children(quote)
    return ParentNode("blockquote", children)


def make_paragraph_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def make_unordered_list(block):
    lines = block.split("\n")
    children = []

    for line in lines:
        list_children = text_to_children(line.lstrip("*-").strip())
        children.append(ParentNode("li", list_children))
    return ParentNode("ul", children)


def make_ordered_list(block):
    lines = block.split("\n")
    children = []

    for line in lines:
        list_children = text_to_children(
            line.lstrip(string.digits + ".").strip())
        children.append(ParentNode("li", list_children))
    return ParentNode("ol", children)
