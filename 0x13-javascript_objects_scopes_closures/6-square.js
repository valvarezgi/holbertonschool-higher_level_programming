#!/usr/bin/node

const Sqr = require('./5-square.js');

class Square extends Sqr {
  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      console.log(c ? String(c).repeat(this.width) : 'X'.repeat(this.width));
    }
  }
}
module.exports = Square;
