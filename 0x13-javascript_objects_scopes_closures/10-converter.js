#!/usr/bin/bash
exports.converter = function (base) {
    return function (x) {
        return x.toString(base);
    };
};
