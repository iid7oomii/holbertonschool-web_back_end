// Create a function getStudentsByLocation that returns an array of objects who are located in a specific city.
export default function getStudentsByLocation(students, location) {
    return location = students.filter((student) => student.location == 'San Francisco');
}
