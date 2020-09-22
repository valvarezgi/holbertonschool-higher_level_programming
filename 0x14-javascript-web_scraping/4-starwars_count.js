#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, data) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(data).results;
    let counter = 0;
    for (let i = 0; i < films.length; i++) {
      if (films[i].characters.includes('https://swapi.co/api/people/18/')) {
        counter++;
      }
    }
    console.log(counter);
  }
});
