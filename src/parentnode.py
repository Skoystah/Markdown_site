from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Invalid HTML: no tag")

        if not self.children:
            raise ValueError("Invalid HTML: no children")

        html_value = ''
        for child in self.children:
            html_value += child.to_html()

        return f'<{self.tag}{self.props_to_html()}>{html_value}</{self.tag}>'

    def __repr__(self):
        return f"ParentNode(tag: {self.tag} | children: {self.children} | props: {self.props})"
