#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
    charPrint(C) {
        let char;
        if (C === undefined) {
            char = 'X';
        } else {
            char = C;
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