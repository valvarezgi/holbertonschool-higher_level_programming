#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const obj = {};

request.get(url, (error, response, data) => {
  if (error) {
    console.log(error);
  } else {
    for (const list of JSON.parse(data)) {
      if (list.completed === true) {
        if (list.userId in obj) {
          obj[list.userId]++;
        } else {
          obj[list.userId] = 1;
        }
      }
    }
    console.log(obj);
  }
});
