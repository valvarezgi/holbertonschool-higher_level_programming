#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let counter = 0;

request(url, (error, response, data) => {
  if (!error && response.statusCode === 200) {
    const completeData = JSON.parse(data);
    for (const film of completeData.results) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          counter++;
        }
      }
    }
  }
  console.log(counter);
});
