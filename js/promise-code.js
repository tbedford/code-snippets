let p1 = new Promise(function (resolve, reject) {

    resolve('Promise 1 resolved')

});

let p2 = new Promise( (resolve, reject) => {

    let status = true; // status of async op, hardcoded for testing 

    if (status){
        resolve('Promise resolved')
    }
    else {
        reject('Promise rejected')
    }
});

//p2.then( resolve => { console.log(resolve) }).catch( reject => console.error(reject) )

p1.then( resolve => { console.log(resolve) }).then(resolve => p2)
    .then( resolve => { console.log(resolve) })
    .catch( reject => console.error(reject) )

let f1 = (x) => { console.log (x) }

f1('Fred')
