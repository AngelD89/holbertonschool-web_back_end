const http = require('http');
const fs = require('fs');

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const database = process.argv[2];

    if (!database) {
      res.statusCode = 400;
      res.end('Database file not provided');
      return;
    }

    fs.readFile(database, 'utf8', (err, data) => {
      if (err) {
        res.statusCode = 400;
        res.end('Cannot load the database');
        return;
      }

      let output = 'This is the list of our students\n';

      const lines = data.split('\n');

      // Remove header and filter out empty lines
      const students = lines
        .slice(1)
        .filter((line) => line.trim().length > 0)
        .map((line) => line.split(','));

      output += `Number of students: ${students.length}\n`;

      // Group students by field
      const fields = {};
      students.forEach((student) => {
        const field = student[3];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(student[0]);
      });

      // Add count and list for each field
      Object.keys(fields).sort().forEach((field) => {
        const fieldStudents = fields[field];
        output += `Number of students in ${field}: ${fieldStudents.length}. List: ${fieldStudents.join(', ')}\n`;
      });

      res.end(output);
    });
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;
