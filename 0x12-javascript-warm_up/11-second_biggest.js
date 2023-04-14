#!/usr/bin/node
let array = 0;
if (process.argv.length <= 3) {
    console.log(array);
} else {
    array = process.argv.slice(2);
    array.sort(
        function (a, b) {
            return b - a;
        }
    );
    console.log(array[1]);
}