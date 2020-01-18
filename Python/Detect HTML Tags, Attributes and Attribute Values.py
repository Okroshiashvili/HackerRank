

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if len(attrs) >= 1:
            for i in range(len(attrs)):
                print("->", attrs[i][0], ">", attrs[i][1])

    def handle_startendtag(self, tag, attrs):
        print(tag)
        if len(attrs) >= 1:
            for i in range(len(attrs)):
                print("->", attrs[i][0], ">", attrs[i][1])



n = int(input())

html_data = ''

for _ in range(n):
    current_line = input()
    html_data += current_line

parser = MyHTMLParser()

parser.feed(html_data)



