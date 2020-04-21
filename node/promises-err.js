new Promise((resolve, reject) => {
    console.log('Initial');

    resolve();
})
.then(() => {
    throw new Error('Something failed');
        
    console.log('Do this');
})
.catch((err) => {
    //console.error('Do that');
    console.error(err);
})
.then(() => {
    console.log('Do this, no matter what happened before');
});

