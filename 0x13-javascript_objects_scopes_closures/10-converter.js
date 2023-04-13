#!/usr/bin/bash
exports.converter = function (base) {
    return (x) => {
        return x.toString(base);
    };
};