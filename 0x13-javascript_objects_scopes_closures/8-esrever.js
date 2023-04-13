#!/usr/bin/node
exports.esrever = function (list) {
    const isReverse = [];
    let i;
    for (i = list.length - 1; i >= 0; i--) {
        isReverse.push(list[i]);
    }
    return isReverse;
};
