// Create a function that returns an array of objects who are located in a specific city.
export default function getStudentsByLocation(students, location) {
  return students.filter((student) => student.location === location);
}
