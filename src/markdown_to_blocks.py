import re
from block import BlockType


def markdown_to_blocks(markdown):
    blocks = []
    split_blocks = markdown.split("\n\n")

    for block in split_blocks:
        if block == "":
            continue

        blocks.append(block.strip())
    return blocks


def block_to_blocktype(markdown):
    if re.match(r"^#{1,6}\s.+", markdown) is not None:
        return BlockType.HEADING.value

    lines = markdown.split("\n")

    if (
        re.match(r"^```", lines[0]) is not None
        and re.fullmatch(r"^.*```$", lines[len(lines) - 1]) is not None
    ):
        return BlockType.CODE.value

    count_quote = 0
    count_unordered = 0
    count_ordered = 0
    for line in lines:
        if line[0] == ">":
            count_quote += 1
            continue

        if line[0:2] == "* " or line[0:2] == "- ":
            count_unordered += 1
            continue

        if line[0:2] == f"{(count_ordered + 1)}.":
            count_ordered += 1
            continue

    if count_quote == len(lines):
        return BlockType.QUOTE.value
    if count_unordered == len(lines):
        return BlockType.UNORDERED_LIST.value
    if count_ordered == len(lines):
        return BlockType.ORDERED_LIST.value

    return BlockType.PARAGRAPH.value
