// old way - callbacks are passed to an async function

function createAudioFileAsync(audioSettings, successCallback, failureCallback) {

    // do asynchronous stuff
    
}

function successCallback(result) {
  console.log("Audio file ready at URL: " + result);
}

function failureCallback(error) {
  console.error("Error generating audio file: " + error);
}

createAudioFileAsync(audioSettings, successCallback, failureCallback);

// using Promises

createAudioFileAsync(audioSettings).then(successCallback, failureCallback);

// which is the same as

const promise = createAudioFileAsync(audioSettings); 
promise.then(successCallback, failureCallback);

// what you've done here is add the callbacks to the promise, rather
// than pass then to the function call.

/*
Unlike "old-style", passed-in callbacks, a promise comes with some
guarantees:

1. Callbacks will never be called before the completion of the current
run of the JavaScript event loop.

2. Callbacks added with then() even after the success or failure of the
asynchronous operation, will be called, as above.

3. Multiple callbacks may be added by calling then() several times. Each
callback is executed one after another, in the order in which they
were inserted. (Chaining)
*/

// chaining
doSomething()
.then(result => doSomethingElse(result))
.then(newResult => doThirdThing(newResult))
.then(finalResult => {
  console.log(`Got the final result: ${finalResult}`);
}).catch(failureCallback);
