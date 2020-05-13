// returns Hello
function hello() {
    return "Hello"
};

// returns Promise { 'Hello' }
async function ahello() {
    return "Hello"
};

console.log(hello())
console.log(ahello())

// async function expression
let bhello = async function() { return "Hello" };
console.log(bhello())

// big arrow notation
let chello = async () => { return "Hello" };
console.log(chello())

// consume promise
chello().then( (value) => console.log("Debug: " + value) )

// same as
chello().then( (foobar) => console.log("Debug: " + foobar) )

// really short hand same as
chello().then(console.log)

