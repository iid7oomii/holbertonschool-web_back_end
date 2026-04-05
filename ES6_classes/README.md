# ES6 Classes

This directory contains practical exercises focused on object-oriented programming in modern JavaScript (ES6+).

The tasks cover class syntax, encapsulation patterns, inheritance, static methods, symbol-based customization, and class cloning behavior.

## Learning Objectives

By completing these exercises, you practice how to:

- Define classes with constructors and internal properties.
- Build helper functions that instantiate multiple objects.
- Add getters and setters with type validation.
- Design class relationships using inheritance.
- Enforce subclass contracts in base classes.
- Use static methods for utility behavior.
- Customize object behavior with `Symbol.toStringTag`, `Symbol.toPrimitive`, and `Symbol.species`.

## File Overview

- `0-classroom.js`
  - Defines `ClassRoom` with `maxStudentsSize` storage.

- `1-make_classrooms.js`
  - Exports `initializeRooms()` returning an array of 3 `ClassRoom` instances.

- `2-hbtn_course.js`
  - Defines `HolbertonCourse` with validated properties:
  - `name` (string), `length` (number), `students` (array).
  - Includes getters and setters with runtime `TypeError` checks.

- `3-currency.js`
  - Defines `Currency` with `code` and `name`.
  - Includes `displayFullCurrency()` formatted as `Name (CODE)`.

- `4-pricing.js`
  - Defines `Pricing` with `amount` and `currency` (`Currency` instance).
  - Includes `displayFullPrice()` and static `convertPrice(amount, conversionRate)`.

- `5-building.js`
  - Defines abstract-like base class `Building`.
  - Requires subclasses to implement `evacuationWarningMessage()`.

- `6-sky_high.js`
  - Defines `SkyHighBuilding` extending `Building`.
  - Adds `floors` and implements `evacuationWarningMessage()`.

- `7-airport.js`
  - Defines `Airport` with custom `Symbol.toStringTag` returning airport code.

- `8-hbtn_class.js`
  - Defines `HolbertonClass` with custom `Symbol.toPrimitive` behavior:
  - number hint -> class size
  - string hint -> location

- `9-hoisting.js`
  - Defines `HolbertonClass`, `StudentHolberton`, and exports a populated `listOfStudents`.
  - Demonstrates class composition and structured student descriptions.

- `10-car.js`
  - Defines `Car` with `cloneCar()` using `Symbol.species` to control clone constructor.

## Requirements

- Node.js (LTS recommended)
- npm (if you want to run lint/tests via project tooling)

## Run Examples

Use Babel Node (or equivalent ES module support) to test files quickly:

```bash
npx babel-node 1-make_classrooms.js
npx babel-node 4-pricing.js
npx babel-node 9-hoisting.js
```

If your environment already supports ES modules natively, you can run with Node.js directly.

## Notes

- These exercises prioritize class design and language features over framework usage.
- Some files are library-style exports and may not print output unless imported by a test/driver file.
- Symbol-based methods are intentionally used to demonstrate advanced object customization.

## Author

Holberton School - Web Back End track exercises.
