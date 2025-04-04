from copystatic import generate_public_files
from gencontent import generate_page_recursive
import sys

public_path = "./docs"
static_path = "./static"


def main():
    basepath = sys.argv[1] if len(sys.argv) > 0 else "/"

    generate_public_files(public_path, static_path)
    generate_page_recursive("content/", "template.html", public_path, basepath)

if __name__ == "__main__":
    main()
