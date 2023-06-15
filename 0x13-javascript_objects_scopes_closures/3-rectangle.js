#!/usr/bin/node
/**
 * Check the parameters provided
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let myChar = '';
      for (let j = 0; j < this.width; j++) {
        myChar += 'X';
      }

      console.log(myChar);
    }
  }
}
module.exports = Rectangle;
