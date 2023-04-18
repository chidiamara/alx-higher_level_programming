#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
    charPrint(c) {
        let char;
        if (c === undefined) {
            char = 'X';
        } else {
            char = c;
        };
        let character = '';
        let i;
        for (i = 0; i < this.width; i++) {
            character += char;
        };
        for (i = 0; i < this.height; i++) {
            console.log(character);
        };
    };
};
module.exports = Square;