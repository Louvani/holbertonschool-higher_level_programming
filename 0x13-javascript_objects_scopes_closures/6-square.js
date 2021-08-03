#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
