#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    let count = 0;
    const results = JSON.parse(body).results;
    const wedge = '/api/people/18/';
    for (let i = 0; i < results.length; i++) {
      if (results[i].characters.find(el => el.includes(wedge))) {
        count++;
      }
    }
    console.log(count);
  }
});
