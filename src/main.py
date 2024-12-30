from textnode import *
#./main.sh
# hello world

def main():
    dummy = TextNode("This is a text node",
                     TextType.BOLD,
                     "https://www.boot.dev")
    print(dummy)
    
if __name__ == "__main__":
    main()
