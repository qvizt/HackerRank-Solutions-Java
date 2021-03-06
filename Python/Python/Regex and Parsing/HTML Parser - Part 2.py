# Solution for HTML Parser - Part 2

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        if not data == "\n":
            if "\n" in data:
                print(">>> Multi-line Comment")
            else:
                print(">>> Single-line Comment")
            print(data)

    def handle_data(self, data):
        if not data == "\n":
            print(">>> Data")
            print(data)


if __name__ == '__main__':
    html = ""
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'

    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
