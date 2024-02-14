#!/usr/bin/node

exports.esrever = function (list) {
  list.sort((a,b) => b - a);
  return list;
}
