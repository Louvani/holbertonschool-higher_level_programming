#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let idx = 0;
    while (idx < this.height) {
      console.log('X'.repeat(this.width));
      idx += 1;
    }
  }
}
module.exports = Rectangle;
