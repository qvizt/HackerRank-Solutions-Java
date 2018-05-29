# Solution for HTML Parser - Part 1

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print("-> {} > {}".format(*attr))

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print("-> {} > {}".format(*attr))


if __name__ == '__main__':
    n = int(input())

    code = ""
    for i in range(n):
        code += input()

    parser = MyHTMLParser()
    parser.feed(code)
