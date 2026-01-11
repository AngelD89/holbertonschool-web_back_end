# Node.js Project

## Description

This is a Node.js project that demonstrates basic JavaScript execution using Node.js with testing and linting setup.

## Requirements

- Node.js version 20.x.x
- npm

## Installation

```bash
npm install
```

## Usage

### Run Tests

```bash
npm run test
```

### Run Linter

```bash
npm run lint
```

### Run Full Test (Lint + Tests)

```bash
npm run full-test
```

## Project Structure

- `package.json` - Project metadata and dependencies
- `babel.config.js` - Babel configuration for ES6+ support
- `.eslintrc.js` - ESLint configuration for code quality
- `database.csv` - Sample CSV data file
- `0-console.js` - Example module with displayMessage function
- `0-main.js` - Example usage of the module
- `__tests__/` - Test files directory (for Jest)

## Configuration

### Babel
Configured to transpile ES6+ code for Node.js current version.

### ESLint
Uses Airbnb style guide with customized rules:
- Console logging is allowed (`no-console: off`)
- Shadow variables are allowed (`no-shadow: off`)
- Jest environment is configured

### Jest
Configured to run tests with Babel transpilation support.

## File Requirements

All files must:
- End with a newline character
- Use `.js` extension for JavaScript files
- Export functions/classes using: `module.exports = myFunction;`

## Example

See `0-main.js` for an example of how to use the `displayMessage` function from `0-console.js`:

```javascript
const displayMessage = require('./0-console');

displayMessage("Hello NodeJS!");
```

## License

ISC
