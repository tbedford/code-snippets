const https = require('https')

const options = {
    hostname: 'flawless-buttery-legal.glitch.me',
    port: 443,
    path: '/jwt',
    method: 'GET',
    headers: {  // will fail if you don't set this
        'User-Agent': 'IoT client v0.1',
    }
}

const req = https.request(options, res => {
    console.log(`statusCode: ${res.statusCode}`)

    res.on('data', d => {
        process.stdout.write(d)
    })
})

req.on('error', error => {
    console.error(error)
})

req.end()
