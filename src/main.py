from copystatic import generate_public_files
from gencontent import generate_page_recursive

public_path = "./public"
static_path = "./static"


def main():
    generate_public_files(public_path, static_path)
    generate_page_recursive("content/", "template.html", "public/")


if __name__ == "__main__":
    main()
