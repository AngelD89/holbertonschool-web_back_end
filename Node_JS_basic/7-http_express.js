const express = require('express');
const fs = require('fs');

const app = express();
const database = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.write('This is the list of our students\n');

  fs.readFile(database, 'utf8', (err, data) => {
    if (err) {
      res.end('Cannot load the database');
      return;
    }

    const lines = data.split('\n');
    const students = [];
    const fields = {};

    for (let i = 1; i < lines.length; i += 1) {
      if (lines[i].trim() !== '') {
        students.push(lines[i]);
      }
    }

    res.write(`Number of students: ${students.length}\n`);

    for (let i = 0; i < students.length; i += 1) {
      const parts = students[i].split(',');
      const firstname = parts[0];
      const field = parts[parts.length - 1];

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    }

    for (const field in fields) {
      if (Object.prototype.hasOwnProperty.call(fields, field)) {
        res.write(
          `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`,
        );
      }
    }

    res.end();
  });
});

app.listen(1245);

module.exports = app;
