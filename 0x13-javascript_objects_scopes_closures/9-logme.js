#!/usr/bin/node
let a = 0;
exports.logMe = function (item) {
    console.log('%d: %s', a, item);
    a++;
};