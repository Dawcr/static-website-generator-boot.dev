from textnode import *
from htmlnode import *
from node_utils import *


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)


if __name__ == "__main__":
    main()