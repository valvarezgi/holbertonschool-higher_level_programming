#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);
const newArray = list.map((number, index) => number * index
);
console.log(newArray);
