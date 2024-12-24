#!/usr/bin/node

const fs = require('fs');

// Get the file paths from command-line arguments
const [sourceFile1, sourceFile2, destinationFile] = process.argv.slice(2);

// Read the first source file
fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${sourceFile1}: ${err.message}`);
    return;
  }

  // Read the second source file
  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${sourceFile2}: ${err.message}`);
      return;
    }

    // Concatenate the contents of both files and write to the destination file
    const concatenatedData = data1 + '\n' + data2; // Add newline between contents
    fs.writeFile(destinationFile, concatenatedData, (err) => {
      if (err) {
        console.error(`Error writing to ${destinationFile}: ${err.message}`);
        return;
      }
      console.log(`Contents concatenated to ${destinationFile}`);
    });
  });
});
