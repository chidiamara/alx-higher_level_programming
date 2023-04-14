#!/usr/bin/node
const numProcess = Number(process.argv[2]);

if (isNaN(numProcess)) {
    console.log('Missing number of occurences');
} else {
    let multiple;
    let square = '';
    for (multiple = 0; multiple < numProcess; multiple++) {
        square += 'X';
    }
    for (multiple = 0; multiple < numProcess; multiple++) {
        console.log(square);
    }
}