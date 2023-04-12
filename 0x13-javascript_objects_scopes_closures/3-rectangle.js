#!/usr/bin/node
class Rectangle {
	constructor (w, h) {
		if (w && h > 0) {
			this.width = w;
			this.height = h;
		};
	};
	print () {
		let character = '';
		let i;
		for (i = 0; i < this.width; i++) {
			character += 'X';
		};
		for (i = 0; i < this.height; i++) {
			console.log(character);
		};
	};
};
module.exports = Rectangle;
