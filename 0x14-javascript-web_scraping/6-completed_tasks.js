#!/usr/bin/node
const request = require('request');
const urlReq = process.argv[2];

request(urlReq, function (e, response, body) {
  if (e) {
    console.error(e);
  } else {
    const todos = JSON.parse(body);
    const tasksComp = {};
    todos.forEach((todo) => {
      if (todo.completed) {
        if (!tasksComp[todo.userId]) {
          tasksComp[todo.userId] = 1;
        } else if (todo.completed) {
          tasksComp[todo.userId]++;
        }
      }
    });
    console.log(tasksComp);
  }
});
