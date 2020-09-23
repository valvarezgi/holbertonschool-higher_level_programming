#!/usr/bin/node

const request = require('request');
request(`http://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (error, response, data) => {
  if (error);
  for (const character of JSON.parse(data).characters) {
    request(character, (error, response, data) => {
      if (error);
      console.log(JSON.parse(data).name);
    });
  }
});
