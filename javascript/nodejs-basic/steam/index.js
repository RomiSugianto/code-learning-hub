const fs = require('fs');
const { resolve } = require('path');
const inputFile = resolve(__dirname, 'input.txt');
const outputFile = resolve(__dirname, 'output.txt');
const writeableStream = fs.createWriteStream(outputFile)

const readableStream = fs.createReadStream(inputFile, {
    highWaterMark: 15
});
readableStream.setEncoding('utf-8');

readableStream.on('readable', () => {
    try {
        const msg = `[${readableStream.read()}]\n`;
        writeableStream.write(msg)
        console.log(msg)
    } catch(error) {
        // catch the error when the chunk cannot be read.
    }
});

readableStream.on('end', () => {
    console.log('Done');
    writeableStream.end()
});