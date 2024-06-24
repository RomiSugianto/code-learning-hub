const firstName = process.argv[2];
const lastName = process.argv[3];
const coffe = require('./coffee')
const moment = require('moment')
const date = moment().format("MMM Do YY")

console.log(`Hello ${firstName} ${lastName}`);
console.log(coffe);
console.log(date)