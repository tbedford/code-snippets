"use strict";

const nexmoclient = require("nexmo-client");

require("dotenv").config({
  path: __dirname + "/.env"
});

const Nexmo = require("nexmo");
var nexmo = new Nexmo({
  apiKey: process.env.NEXMO_API_KEY,
  apiSecret: process.env.NEXMO_API_SECRET,
  applicationId: process.env.NEXMO_APPLICATION_ID,
  privateKey: process.env.NEXMO_APPLICATION_PRIVATE_KEY_PATH
});

////////////////////////////////////////////////////////////////

function createUser(username) {
  return new Promise(function(resolve, reject) {
    nexmo.users.create({ name: username }, (error, result) => {
      if (error) {
        return reject(error);
      }
      return resolve(result);
    });
  });
}

function createConversation(name, display_name) {
  return new Promise(function(resolve, reject) {
    nexmo.conversations.create(
      { name: name, display_name: display_name },
      (error, result) => {
        if (error) {
          return reject(error);
        }
        return resolve(result);
      }
    );
  });
}

// add user to conversation(id)
function addMember(id, username) {
  return new Promise(function(resolve, reject) {
    nexmo.conversations.members.add(
      id,
      {
        action: "join",
        user_name: username,
        channel: {
          type: "app"
        }
      },
      (error, result) => {
        if (error) {
          return reject(error);
        }
        return resolve(result);
      }
    );
  });
}

async function main() {
  const username = "test-user-1";
  
  let user = await createUser(username).catch(error => console.error(error));
  console.log(user);
  
  
  let conversation = await createConversation(
    "test-convo-1",
    "The display name"
  ).catch(error => console.error(error));
  console.log(conversation);
  
  
  let member = await addMember(conversation.id, username).catch(error =>
    console.error(error)
  );
  console.log(member);
}

main();
