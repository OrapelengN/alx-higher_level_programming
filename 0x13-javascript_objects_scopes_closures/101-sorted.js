#!/usr/bin/node

const dict = require('./101-data').dict;

const sortedDict = {};

for (const userId in dict) {
  const occurrence = dict[userId];
  
  // If the occurrence is not already a key in sortedDict, initialize it
  if (!sortedDict[occurrence]) {
    sortedDict[occurrence] = [];
  }

  // Push the userId into the list for the corresponding occurrence
  sortedDict[occurrence].push(userId.toString()); // Convert userId to string
}

console.log(sortedDict);
