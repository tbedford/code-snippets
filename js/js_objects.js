let o = {
    name: "Fred",
    age: 59,
    hobbies: ['diving', 'stamps', 'coins', 'boardgames']
};

console.log(o);

for (h of o['hobbies']) {
    console.log(h);
}
