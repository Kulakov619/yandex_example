import csv
import io
import urllib.request


url = 'https://docs.google.com/spreadsheets/d/1VKjsb4sanastsb0Q5tIZiOjPbRpPa0t80ADBqxZAtfU/export?format=csv'

response = urllib.request.urlopen(url)

with io.TextIOWrapper(response, encoding='utf-8') as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)