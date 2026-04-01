// Create a function getStudentIdsSum that returns the sum of all the student ids.
export default function getStudentIdsSum(studentSumid) {
  return studentSumid.reduce((accumlator, currentValue) => accumlator + currentValue.id, 0);
}
