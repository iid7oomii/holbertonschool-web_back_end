# ES6 Promise Exercises

This project contains a set of practical ES6 Promise exercises focused on asynchronous JavaScript patterns.  
Each task is implemented in a dedicated file (`0-promise.js` to `9-try.js`) with a matching `*-main.js` file used to demonstrate and test behavior.

## Learning Goals

By working through this folder, you practice how to:

- Create and return basic promises.
- Resolve and reject promises with custom payloads.
- Chain `.then()`, `.catch()`, and `.finally()` handlers.
- Run concurrent async operations with `Promise.all()`.
- Collect partial failures with `Promise.allSettled()`.
- Return the fastest promise with `Promise.race()`.
- Handle synchronous errors using `try/catch/finally`.

## Project Structure

Core files:

- `0-promise.js` to `9-try.js`: implementation tasks.
- `utils.js`: helper async functions used by `3-all.js`.
- `0-main.js` to `9-main.js`: runnable examples for each task.

Tooling files:

- `package.json`: scripts and development dependencies.
- `babel.config.js`: Babel configuration for Node.js execution.
- `.eslintrc.js`: linting rules.

## Requirements

- Node.js (recommended: modern LTS)
- npm

## Installation

From the `ES6_promise` directory:

```bash
npm install
```

## Available Scripts

```bash
# Lint all numbered exercise files
npm run check-lint

# Run a file with Babel Node (example)
npm run dev -- 0-main.js

# Run tests (if test files are present)
npm test

# Run lint + tests
npm run full-test
```

## Exercise Map

| File                 | What it does                                                                                                     |
| -------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `0-promise.js`       | Returns a resolved Promise.                                                                                      |
| `1-promise.js`       | Returns a Promise that resolves with a success object or rejects with an Error based on a boolean argument.      |
| `2-then.js`          | Attaches `then/catch/finally` handlers to a promise and normalizes output shape.                                 |
| `3-all.js`           | Uses `Promise.all()` to run user and photo async operations in parallel and logs output; handles global failure. |
| `4-user-promise.js`  | Returns a resolved Promise with user identity data.                                                              |
| `5-photo-reject.js`  | Returns a rejected Promise describing why a file cannot be processed.                                            |
| `6-final-user.js`    | Uses `Promise.allSettled()` to return both success and failure results in a unified array format.                |
| `7-load_balancer.js` | Uses `Promise.race()` to resolve with the first completed download promise.                                      |
| `8-try.js`           | Divides two numbers and throws an Error when denominator is zero.                                                |
| `9-try.js`           | Executes a function safely and always appends a final guardrail message using `try/catch/finally`.               |

## Quick Examples

Run specific demonstrations:

```bash
npm run dev -- 3-main.js
npm run dev -- 6-main.js
npm run dev -- 7-main.js
```

## Notes

- This project uses ES modules syntax (`import` / `export`).
- Some imports intentionally omit `.js` extension in source files to match exercise style.
- Console output in `*-main.js` files is for educational verification.

## Author

Holberton School - Web Back End track exercises.
