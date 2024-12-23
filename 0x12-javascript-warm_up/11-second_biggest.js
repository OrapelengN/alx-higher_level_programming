#!/usr/bin/node

const args = process.argv.slice(2); // Get all arguments except the script name

if (args.length < 2) {
  console.log(0); // If there are fewer than two arguments, print 0
} else {
  // Convert arguments to integers and sort in descending order
  const numbers = args.map(Number).sort((a, b) => b - a);
  console.log(numbers[1]); // The second biggest number
}
