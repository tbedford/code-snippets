/_ ES5 _/;
var isMomHappy = true;

// Promise
var willIGetNewPhone = new Promise(function (resolve, reject) {
  if (isMomHappy) {
    var phone = {
      brand: "Samsung",
      color: "black",
    };
    resolve(phone); // fulfilled
  } else {
    var reason = new Error("mom is not happy");
    reject(reason); // reject
  }
});

// 2nd promise
var showOff = function (phone) {
  return new Promise(function (resolve, reject) {
    var message =
      "Hey friend, I have a new " + phone.color + " " + phone.brand + " phone";
    resolve(message);
  });
};

// call our promise
var askMom = function () {
  willIGetNewPhone
    .then(showOff)
    .then(function (fulfilled) {
      console.log(fulfilled);
    })
    .catch(function (error) {
      console.log(error.message);
    });
};

askMom();
