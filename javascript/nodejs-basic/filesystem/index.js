const fs = require('fs');
const { resolve } = require('path');

const fileReadCallback = (error, data) => {
    if(error) {
        console.log('Gagal membaca berkas');
        return;
    }
    console.log(data);
};
const file = resolve(__dirname, 'notes.txt');

fs.readFile(file, 'UTF-8', fileReadCallback);
data = fs.readFileSync(file, 'utf-8')
console.log(data)