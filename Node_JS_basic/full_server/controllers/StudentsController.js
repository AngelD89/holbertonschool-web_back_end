import { readDatabase } from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    const dbPath = process.argv[2];

    readDatabase(dbPath)
      .then((fields) => {
        let output = 'This is the list of our students\n';

        // Sort fields alphabetically (case insensitive)
        const sortedFields = Object.keys(fields).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

        sortedFields.forEach((field) => {
          const students = fields[field];
          output += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
        });

        res.status(200).send(output);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const major = req.params.major.toUpperCase();
    const dbPath = process.argv[2];

    // Validate major parameter
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(dbPath)
      .then((fields) => {
        if (!fields[major]) {
          res.status(500).send('Cannot load the database');
          return;
        }

        const students = fields[major];
        res.status(200).send(`List: ${students.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
