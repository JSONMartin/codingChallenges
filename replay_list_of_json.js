/**
 * Created by jsonmartin on 3/16/16.
 */
//Write the code to replay a list of HTTP requests from a file represented as JSON

/*
  METHOD #1
 */
var fs = require("fs"); //Require the FS library
fs.readFile('dummy.json', 'utf8', function(err, data) { //Read in the file asynchronously
  //After file has been read, pass to a JSON parse function
  var object = JSON.parse(data);
  console.log(object);
  console.log("Username:", object.username)
});

/*
 METHOD #2 (https://www.codementor.io/nodejs/tutorial/how-to-use-json-files-in-node-js)
 */
var obj = require ("./dummy.json");
console.log(obj);
console.log(obj.username);