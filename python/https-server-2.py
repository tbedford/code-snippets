from flask import Flask
app = Flask(__name__)

def read_file(filename):
    f = open (filename, mode='r', encoding='utf-8')
    source = f.read()
    f.close()
    return source

@app.route("/")
def hello():
  return ("Hello world\n")

@app.route("/get-file")
def get_file():
  data = read_file('test.json')
  return (data)


if __name__ == "__main__":
  app.run(ssl_context='adhoc')
