// Create a function that returns a string of all the set values that start with a specific string.
export default function cleanSet(set, startString) {
  if (!startString) return '';

  return [...set]
    .filter(value => typeof value === 'string' && value.startsWith(startString))
    .map(value => value.slice(startString.length))
    .join('-');
}