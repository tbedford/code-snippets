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

//////////

function getConversations() {
  return new Promise(function(resolve, reject) {
    nexmo.conversations.get({}, (error, result) => {
      if (error) {
        return reject(error);
      }
      return resolve(result._embedded.conversations);
    });
  });
}

function getConversation(name, conversations) {
  return new Promise(function(resolve, reject) {
    let conversation = conversations.find(o => o.name === name);
    nexmo.conversations.get(conversation.uuid, (error, result) => {
      if (error) {
        return reject(error);
      }
      return resolve(result);
    });
  });
}

function getMember(username, conversation) {
  return conversation.members.find(
    o => o.name === username && o.state === "JOINED"
  );
}

async function main() {
  let name = "send-in-blue-user-456";
  let username = "user-456";

  let conversations = await getConversations();
  let con = await getConversation(name, conversations);
  let mem = getMember(username, con);
  console.log("MEM_ID: ", mem.member_id);
}

main();
