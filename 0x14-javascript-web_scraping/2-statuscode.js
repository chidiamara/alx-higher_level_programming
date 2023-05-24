#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  error ? console.log(error) : console.log('code:', response.statusCode);
});
