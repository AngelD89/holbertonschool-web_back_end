import fs from 'fs';

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }

      const lines = data.split('\n');

      // Remove header and filter out empty lines
      const students = lines
        .slice(1)
        .filter((line) => line.trim().length > 0)
        .map((line) => line.split(','));

      // Group students by field
      const fields = {};
      students.forEach((student) => {
        const field = student[3];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(student[0]);
      });

      resolve(fields);
    });
  });
}

export default readDatabase;
