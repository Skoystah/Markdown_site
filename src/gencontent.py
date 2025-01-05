import os
from markdown_to_html import markdown_to_html, extract_title


def generate_page(from_path, template_path, dest_path):
    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}")

    md_file = open(from_path, "r")
    md_contents = md_file.read()
    md_file.close()

    template_file = open(template_path, "r")
    template_contents = template_file.read()
    template_file.close()

    html = markdown_to_html(md_contents).to_html()
    title = extract_title(md_contents)

    template_contents = template_contents.replace("{{ Title }}", title).replace(
        "{{ Content }}", html
    )
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    html_file = open(dest_path, "w")
    html_file.write(template_contents)


def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    dir = os.listdir(dir_path_content)

    for item in dir:
        path = os.path.join(dir_path_content, item)
        if os.path.isfile(path):
            if item.endswith(".md"):
                new_item = item.replace(".md", ".html")
            new_path = os.path.join(dest_dir_path, new_item)
            generate_page(path, template_path, new_path)
        elif os.path.isdir(path):
            new_path = os.path.join(dest_dir_path, item)
            os.mkdir(new_path)
            print(f"Creating dir {new_path}")
            generate_page_recursive(path, template_path, new_path)
