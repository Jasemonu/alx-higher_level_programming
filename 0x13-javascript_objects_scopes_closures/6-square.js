#!/usr/bin/node

/**
*a class Square that defines a square and inherits
* from Square of 5-square.js
*/

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let char = '';
      for (let j = 0; j < this.width; j++) {
        char += c;
      }
      console.log(char);
    }
  }
}

module.exports = Square;
