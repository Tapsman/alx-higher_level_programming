#!/usr/bin/node
// Script that will compute the number of taskes completed
// Where the first argument is API url

const request = require('request');

request.get(process.argv[2], { json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const tasksCompleted = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(tasksCompleted);
});
