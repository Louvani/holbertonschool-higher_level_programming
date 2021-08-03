#!/usr/bin/node
let increment = 0;
exports.logMe = function (item) {
	console.log(increment + ': ' + item)
	increment += 1;
}