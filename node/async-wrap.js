function saySomething(t){
    console.log(t);
}

function failureCallback(err){
    console.error(err)
}

// We're going to wrap setTimeout() so you don't need to call it directly 
//setTimeout( () => saySomething("A unit of time passed"), 1*1000);

const myDelayFunc = timeInMS => new Promise (resolve => setTimeout(resolve, timeInMS));

// spiffy new way to call (indirectly) with Promises
myDelayFunc(1000).then(() => saySomething("Time passed")).catch(failureCallback);


