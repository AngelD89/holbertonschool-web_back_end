const fs = require('fs');

function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = data.split('\n');

  // Remove header and filter out empty lines
  const students = lines
    .slice(1)
    .filter((line) => line.trim().length > 0)
    .map((line) => line.split(','));

  console.log(`Number of students: ${students.length}`);

  // Group students by field
  const fields = {};
  students.forEach((student) => {
    const field = student[3];
    if (!fields[field]) {
      fields[field] = [];
    }
    fields[field].push(student[0]);
  });

  // Log count and list for each field
  Object.keys(fields).sort().forEach((field) => {
    const fieldStudents = fields[field];
    console.log(`Number of students in ${field}: ${fieldStudents.length}. List: ${fieldStudents.join(', ')}`);
  });
}

module.exports = countStudents;
