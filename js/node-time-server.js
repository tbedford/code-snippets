const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {

    // request
    console.log(`Request Method: ${req.method}`);
    console.log(`Request URL: ${req.url}`);

    // response  
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    const d = new Date();
    res.end(`${d}`);
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
