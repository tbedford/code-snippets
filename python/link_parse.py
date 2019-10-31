from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import urljoin 

s1 = "https://tonys-notebook.com"
s2 = "https://tonys-notebook.com/articles/doom.html"
s3 = "https://tonys-notebook.com/index.html"
s4 = "./doom.html"
s5 = "../../articles/doom.html"
s6 = "/doom.html"
s7 = "https://api.nexmo.com/beta/audit/events?search_text=text&date_from=2018-06-01&date_to=2019-11-01"
s8 = "https://tonys-notebook.com/"
s9 = "https://twitter.com/tonytechwriter"

obj = urlparse(s7)
print(obj)

# Now parse the query string specifically
qs = parse_qs(obj.query)
print(qs)
print("Date_to: {date}".format(date=qs['date_to']))

# Make a URL from base and part
link = urljoin(s8, s4)
print(link)

link = urljoin(s8, s5)
print(link)

link = urljoin(s8, s2)
print(link)

link = urljoin(s8, s9)
print(link)

