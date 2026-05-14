import sys
import urllib.request
from html.parser import HTMLParser

class TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = []
        self.in_td = False
        self.current_row = []
        self.current_cell = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self.in_td = True
            self.current_cell = ''

    def handle_endtag(self, tag):
        if tag == 'td':
            self.in_td = False
            self.current_row.append(self.current_cell.strip())
        elif tag == 'tr':
            if len(self.current_row) == 3:
                try:
                    x = int(self.current_row[0])
                    char = self.current_row[1]
                    y = int(self.current_row[2])
                    self.data.append((x, char, y))
                except ValueError:
                    pass
            self.current_row = []

    def handle_data(self, data):
        if self.in_td:
            self.current_cell += data

def fetch_and_render(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')

    parser = TableParser()
    parser.feed(html)
    data = parser.data

    if not data:
        print("No data found.")
        return

    max_x = max(x for x, _, _ in data)
    max_y = max(y for _, _, y in data)

    grid = [[' '] * (max_x + 1) for _ in range(max_y + 1)]

    for x, char, y in data:
        grid[y][x] = char

    for row in reversed(grid):
        print(''.join(row))
