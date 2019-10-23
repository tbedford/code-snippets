
// convert JS object to JSON string
var o = { name: "Tony", age: 59 };
console.log(o);

var s = JSON.stringify(o);
console.log(s);

var j = JSON.parse(s);
console.log(j);

console.log(j.name);
console.log(j.age);


