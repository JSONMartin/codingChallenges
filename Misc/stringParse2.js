/*
 {
 'index': {
 'about': {
 'team': true,
 'company': ['Jim', 'Barry']
 }
 }
 }
 Is transformed into:
 {
 'index/about/team': true,
 'index/about/company': ['Jim', 'Barry']
 }
 */
"use strict";
function convertToURLMap(obj) {
  let results = {};

  let traverse = (node, cur_path) => {
    for(let key in node) {
      let element = node[key];
      if (typeof(element) === 'object' && !Array.isArray(element)) { // If object & not array
        traverse(element, cur_path + key + "/");
      }
      else {
        results[cur_path + key] = element;
      }
    }
  };

  traverse(obj, "");
  return results;
}

function convertToURLMapDirty(obj) {
  let results = {};

  let traverse = (node, cur_path) => {
    for(let key in node) {
      console.log(cur_path);
      console.log(node);
      let element = node[key];
      console.log(element);
      if (typeof(element) === 'object' && !Array.isArray(element)) { // If object & not array
        traverse(element, cur_path + key + "/");
      }
      else {
        //results.push(cur_[])
        results[cur_path + key] = element;
      }
    }
  };

  traverse(obj, "");
  console.log(results);
  return results;
}

let input1 = {
  'index': {
    'about': {
      'team': true,
      'company': ['Jim', 'Barry'],
    }
  }
};

let input2 = {
  'index': {
    'about': {
      'team': true,
      'company': ['Jim', 'Barry'],
      'archive': {
        'key': 'value',
        'otherkey': [1, 2, 3]
      }
    }
  }
};

//convertToURLMap(input1)
convertToURLMap(input2)