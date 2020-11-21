// 1. callbacks

function success(n) {
  console.log(`Success => ${n}`);
}

function error(n) {
  console.error(`Error => ${n}`);
}

function dothis(succ, err) {
  const n = parseInt(Math.random() * 1000);

  // success
  if (n % 2 == 0) setTimeout(() => succ(n), 1000);
  // failure
  else setTimeout(() => err(n), 1000);
}

//dothis(success, error);

// 2. Promises

function dothat() {
  return new Promise((resolve, reject) => {
    const n = parseInt(Math.random() * 1000);

    if (n % 2 == 0) setTimeout(() => resolve(n), 1000);
    else setTimeout(() => reject(n), 1000);
  });
}

/*
dothat()
  .then((v) => {
    console.log(`Resolve 1: ${v}`);
    return dothat(); // the `return` is essential!
  })
  .then((v) => console.log(`Resolve 2: ${v}`))
  .catch((v) => console.error(`Reject: ${v}`))
  .finally((v) => console.log("Finally"));
*/

// 3. async/await

async function executeDoThat() {
  try {
    const n = await dothat();
    console.log(`Async: ${n}`);
  } catch (e) {
    console.error(`Failed: ${e}`);
  } finally {
    console.log("Finaaalllyyy!");
  }
}

executeDoThat();
