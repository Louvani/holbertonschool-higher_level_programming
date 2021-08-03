#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0;
  for (const itm of list) {
    if (itm === searchElement) {
      occurrences += 1;
    }
  }
  return occurrences;
};
