#!/usr/bin/node

const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let idx = 0;
      while (idx < this.height) {
        console.log(c.repeat(this.width));
        idx += 1;
      }
    }
  }
}
module.exports = Square;
