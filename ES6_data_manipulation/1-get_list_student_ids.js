// array return list of objects

export default function getListStudents() {
  return [{ id: 1, firstName: 'Guillaume', location: 'San Francisco' },
    { id: 2, firstName: 'James', location: 'Columbia' },
    { id: 5, firstName: 'Serena', location: 'San Francisco' }];
}


function getListStudentIds(getListStudents) {
  return getListStudents.map((student) => student.id);   
}

console.log(getListStudentIds(getListStudents()));
