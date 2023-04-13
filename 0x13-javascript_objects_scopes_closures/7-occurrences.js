#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    let isOccur = 0;
    let i;
    for (i = 0; i < list.length; i++) {
        isOccur = (list[i] === searchElement)
            ? isOccur + 1
            : isOccur;
    }
    return isOccur;
};