#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request(process.argv[2], (error, response, data) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], data, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
