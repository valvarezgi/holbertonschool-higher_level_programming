#!/usr/bin/node

const req = require('request');
req.get(process.argv[2], (error, response) => {
  if (error) {
    console.error('code:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
