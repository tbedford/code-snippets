from html.parser import HTMLParser

html = '''
<html>
<head><title>The Title</title></head>
<body>
<p>Hello 
<a href="https://tonys-notebook.com" id="1234">My Site</a>
World</p>
<p>Hello 
<a id="12" href="https://developer.nexmo.com">NDP</a>
World</p>
</body>
</html>
'''

links = []

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for a in attrs:
                if a[0] == 'href':
                    links.append(a[1])
            
    def handle_endtag(self, tag):
        #print("End tag --> ", tag)
        return
    
    def handle_data(self, data):
        #print("Data --> ", data)
        return
    
parser = MyHTMLParser()
parser.feed(html)
print(links)


        

