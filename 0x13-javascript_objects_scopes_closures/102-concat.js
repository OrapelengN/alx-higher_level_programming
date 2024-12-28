#!/usr/bin/node

const fs = require('fs');

// Get arguments from the command line
const args = process.argv.slice(2);

if (args.length < 3) {
  console.error('Usage: ./102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const [file1, file2, destination] = args;

try {
  // Read the content of the first file
  const content1 = fs.readFileSync(file1, 'utf-8');
  // Read the content of the second file
  const content2 = fs.readFileSync(file2, 'utf-8');
  // Concatenate and write the content to the destination file
  fs.writeFileSync(destination, content1 + content2, 'utf-8');
  console.log('Files concatenated successfully');
} catch (error) {
  console.error(`Error: ${error.message}`);
  process.exit(1);
}
