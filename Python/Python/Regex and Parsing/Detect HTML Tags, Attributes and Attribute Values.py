# Solution for Detect HTML Tags, Attributes and Attribute Values

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))


if __name__ == '__main__':
    n = int(input())

    html = ""
    for i in range(n):
        html += input()

    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
