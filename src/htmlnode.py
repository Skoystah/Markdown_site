class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_string = ''

        if not self.props:
            return html_string

        for prop, value in self.props.items():
            html_string = f'{html_string} {prop}="{value}"'

        return html_string

    def __repr__(self):
        return f"HTMLNode(tag: {self.tag} | value: {self.value} | children: {self.children} | props: {self.props})"
