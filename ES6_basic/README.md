# ES6 Basics

This directory contains foundational ES6 exercises focused on modern JavaScript syntax and core language features.

The tasks are organized as small, focused modules that demonstrate practical usage of `const`/`let`, arrow functions, default/rest/spread syntax, template literals, enhanced object literals, computed property names, and iteration patterns.

## Learning Objectives

By completing these exercises, you practice how to:

- Use `const` and `let` with proper block scope.
- Write and use arrow functions.
- Apply default parameters.
- Handle variable argument lists with rest parameters.
- Merge and expand values with spread syntax.
- Build dynamic strings using template literals.
- Use object property shorthand and computed property names.
- Add methods directly inside object literals.
- Iterate collections with `for...of`.

## File Overview

- `0-constants.js`
  - Demonstrates use of `const` and `let` in simple exported functions.

- `1-block-scoped.js`
  - Shows block scoping behavior and returns values unaffected by inner block redeclarations.

- `2-arrow.js`
  - Defines an object initializer using arrow function syntax for methods.

- `3-default-parameter.js`
  - Uses default values for optional numeric parameters.

- `4-rest-parameter.js`
  - Returns the number of arguments passed using rest parameters.

- `5-spread-operator.js`
  - Concatenates arrays and a string with spread syntax.

- `6-string-interpolation.js`
  - Builds a multi-value sentence using template literals.

- `7-getBudgetObject.js`
  - Uses object property shorthand to construct a budget object.

- `8-getBudgetCurrentYear.js`
  - Uses computed property names based on the current year.

- `9-getFullBudget.js`
  - Merges objects with spread and adds inline methods to format income.

- `10-loops.js`
  - Uses `for...of` to modify each element in an array with a prefix.

- `11-createEmployeesObject.js`
  - Creates an object with a dynamic department key.

- `12-createReportObject.js`
  - Creates a report object containing employees and a method to count departments.

## Requirements

- Node.js (LTS recommended)
- npm (optional, depending on your parent project tooling)

## Quick Usage Examples

Run examples in Node.js (ES module capable environment):

```bash
node -e "import('./4-rest-parameter.js').then(m => console.log(m.default(1,2,3,4)))"
node -e "import('./8-getBudgetCurrentYear.js').then(m => console.log(m.default(1000, 2000, 3000)))"
node -e "import('./11-createEmployeesObject.js').then(m => console.log(m.default('engineering', ['Bob', 'Jane'])))"
```

If your environment does not support direct ESM execution by default, use Babel Node or configure Node.js modules accordingly.

## Notes

- These files are intentionally small and educational.
- The focus is on language features and syntax clarity rather than app structure.
- Some implementations mutate input values (for example, `10-loops.js`) by design for the exercise.

## Author

Holberton School - Web Back End track exercises.
