#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;
  let tmp;
  for (let i = 0; i < len / 2; i++) {
    tmp = list[i];
    list[i] = list[len - i - 1];
    list[len - i - 1] = tmp;
  }
  return list;
};
