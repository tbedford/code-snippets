
var p = new Promise((resolve, reject) => {
    console.log('Promise created.');
    // some asynch activity is performed here
    
    // complete as appropriate
    var resolved = false;
    if (resolved){
        resolve('Operation resolved.');
    }
    else {
        reject('Operation rejected.');
    }
});


p.then((msg) => {
    console.log("Status: ", msg);
})
.catch((msg) => {
    console.log("Status: ", msg);
});