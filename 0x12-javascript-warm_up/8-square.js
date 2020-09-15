#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let index = 0; index < parseInt(process.argv[2]); index++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
