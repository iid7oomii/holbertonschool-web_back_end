# ES6 Data Manipulation

This directory contains hands-on ES6 exercises focused on manipulating collections in modern JavaScript: arrays, objects, typed arrays, sets, and maps.

The tasks progress from basic array transformations to practical usage of `Set`, `Map`, and `DataView`, with one implementation file per exercise.

## Learning Objectives

By completing these exercises, you practice how to:

- Transform data with `map`, `filter`, and `reduce`.
- Create reusable functions for student datasets.
- Work with typed arrays and `ArrayBuffer` memory.
- Use `Set` for uniqueness and membership checks.
- Use `Map` for key/value data structures and updates.
- Handle invalid inputs with clear error behavior.

## File Overview

### Implementations

- `0-get_list_students.js`: returns a base list of student objects.
- `1-get_list_student_ids.js`: returns an array of student IDs (or `[]` for invalid input).
- `2-get_students_by_loc.js`: filters students by location.
- `3-get_ids_sum.js`: sums all student IDs.
- `4-update_grade_by_city.js`: filters students by city and merges grades from a second array.
- `5-typed_arrays.js`: creates an `ArrayBuffer`/`DataView` and sets an `Int8` value at a position.
- `6-set.js`: builds a `Set` from an array.
- `7-has_array_values.js`: checks whether all array values exist in a set.
- `8-clean_set.js`: extracts and joins string suffixes for values starting with a prefix.
- `9-groceries_list.js`: returns a groceries `Map` with predefined quantities.
- `10-update_uniq_items.js`: updates all `Map` entries with quantity `1` to `100`, and throws on non-Map input.

### Demo Entry Points

- `1-main.js` to `10-main.js`: sample usage for each task.

### Tooling

- `package.json`: lint and test scripts.
- `babel.config.js`: Babel preset configuration.
- `.eslintrc.js`: ESLint rules.

## Requirements

- Node.js (LTS recommended)
- npm

## Installation

From this directory:

```bash
npm install
```

## Available Scripts

```bash
# Lint all exercise files
npm run check-lint

# Run tests (if present)
npm test

# Run lint + tests
npm run full-test
```

## Run Exercise Examples

Use Babel Node to execute any `*-main.js` file.

```bash
npx babel-node 1-main.js
npx babel-node 4-main.js
npx babel-node 8-main.js
npx babel-node 10-main.js
```

## Notes

- The implementation follows ES module syntax (`import` / `export default`).
- Input validation behavior differs by task and matches exercise requirements:
  - some functions return safe defaults (for example, `[]` or empty string),
  - others throw explicit `Error` objects for invalid usage.

## Author

Holberton School - Web Back End track exercises.
