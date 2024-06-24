const http = require('http');

const requestListener = (request, response) => {
    response.setHeader('Content-Type', 'application/json');
    response.setHeader('X-Powered-By', 'NodeJS');
    // response.statusCode = 200;

    const { url, method } = request;

    // if(method === 'GET') {
    //     response.end('<h1>Hello!</h1>');
    // }
    //
    // if(method === 'POST') {
    //     let body = [];
    //
    //     request.on('data', (chunk) => {
    //         body.push(chunk);
    //     });
    //
    //     request.on('end', () => {
    //         body = Buffer.concat(body).toString();
    //         const { name } = JSON.parse(body)
    //         response.end(`<h1>Hai, ${name}!</h1>`);
    //     });
    // }

    if (url === '/') {
        if(method === 'GET') {
            response.statusCode = 200
            // response.end('Ini hompage');
            response.end(JSON.stringify({
                message : 'Ini hompage',
            }))
        }else{
            response.statusCode = 400
            // response.end(`Halaman tidak dapat diakses dengan ${method} request`)
            response.end(JSON.stringify({
                message : `Halaman tidak dapat diakses dengan ${method} request`
            }))
        }
    } else if (url === '/about') {
        if(method === 'GET') {
            response.statusCode = 200
            // response.end('Ini about');
            response.end(JSON.stringify({
                message : 'Ini about',
            }))
        }else if (method === 'POST') {
            response.statusCode = 200
            let body = [];

            request.on('data', (chunk) => {
                body.push(chunk);
            });

            request.on('end', () => {
                body = Buffer.concat(body).toString();
                const { name } = JSON.parse(body)
                // response.end(`<h1>Hai, ${name}!</h1>`);
                response.end(JSON.stringify({
                    message : `<h1>Hai, ${name}!</h1>`,
                }))
            });
        } else {
            response.statusCode = 400
            // response.end(`Halaman tidak dapat diakses dengan ${method} request`)
            response.end(JSON.stringify({
                message : `Halaman tidak dapat diakses dengan ${method} request`
            }))
        }
    } else {
        response.statusCode = 400
        // response.end('<h1>Halaman tidak ditemukan!</h1>')
        response.end(JSON.stringify({
            message : '<h1>Halaman tidak ditemukan!</h1>'
        }))
    }
};

const server = http.createServer(requestListener);

const port = 5000;
const host = 'localhost';

server.listen(port, host, () => {
    console.log(`Server berjalan pada http://${host}:${port}`);
});