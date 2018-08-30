var http = require('http');
var url = require('url');

// ?month=may&year=2018  
http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(req.url);
    var q = url.parse(req.url, true).query;
    var txt = "<p><b>"+ q.year + " " + q.month + "</b></p>";
    res.end(txt);
}).listen(8080);
