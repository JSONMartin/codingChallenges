function Graph() {
  var verticies = [];
  var adjList = new Dictionary();

  this.addVertex = function (v) {
    verticies.push(v);
    adjList.set(v, []);
  };

  this.getVertex = function (v) {
    adjList.get(v);
  };

  this.addEdge = function (v1, v2) {
    adjList.get(v1).push(v2);
    adjList.get(v2).push(v1); //No need to add this if it is a directed (one way) graph
  };

  this.toString = function () {
    var s = "";
    verticies.forEach(function (vertex) {
      s+="Vertex:" + vertex + ", Edges:" + adjList.get(vertex).toString()+ "\n";
    });
    return s;
  };

  this.bfs = function (vertex, cb) {
    vertex = vertex || verticies[0];
    cb = cb || function(v) { console.log("Visiting:", v); };

    var q = [];
    var explored = {};

    var visitOrder = [];

    explored[vertex] = true;
    q.push(vertex);

    while(q.length > 0) {
      var v = q.shift();
      visitOrder.push(v);
      cb(v);

      adjList.get(v).forEach(function (curVertex) {
        if(!explored.hasOwnProperty(curVertex)) {
          explored[curVertex] = true;
          q.push(curVertex);
        }
      });
    }

    // console.log("Explored:", explored);
    console.log("visitOrder:", visitOrder);
  };

  this.dfs = function (vertex, cb) {
    var visited = {};
    vertex = vertex || verticies[0];
    var visitOrder = [];

    var traverse = function (vertex) {
      var edges = adjList.get(vertex);
      visited[vertex] = true;
      visitOrder.push(vertex);
      edges.forEach(function (edge) {
        console.log("Edge:", edge);
        if(!visited.hasOwnProperty(edge)) {
          traverse(edge);
        }
      });
    };

    traverse(vertex);
    console.log("Visit Order:", visitOrder);
  };
}

/******************************************
 * TESTS
 ******************************************/

var graph = new Graph();
var myVertices = ['A','B','C','D','E','F','G','H','I']; //{7}
for (var i=0; i<myVertices.length; i++){ //{8}
  graph.addVertex(myVertices[i]);
}
graph.addEdge('A', 'B'); //{9}
graph.addEdge('A', 'C');
graph.addEdge('A', 'D');
graph.addEdge('C', 'D');
graph.addEdge('C', 'G');
graph.addEdge('D', 'G');
graph.addEdge('D', 'H');
graph.addEdge('B', 'E');
graph.addEdge('B', 'F');
graph.addEdge('E', 'I');
console.log(graph.toString());
console.log(graph.bfs());
console.log(graph.dfs());



  function Dictionary() {
  var items = {};

  this.set = function(key,value) {
    items[key] = value;
  }; //This adds a new item to the dictionary.

  this.remove = function(key){
    if(this.has(key)) {
      delete items[key];
      return true;
    }
    return false;
  }; //This removes the value from the dictionary using the key.

  this.has = function(key){
    return items.hasOwnProperty(key);
  }; //This returns true if the key exists in the dictionary and false otherwise.

  this.get = function(key){
    if(this.has(key)) {
      return items[key];
    }
    return undefined;
  }; //This returns a specific value searched by the key.

  this.clear = function(){
    items = {};
  };// This removes all the items from the dictionary.

  this.size = function(){
    return Object.keys(items).length;
  }; //This returns how many elements the dictionary contains. It is similar to the length property of the array.

  this.keys = function(){
    return Object.keys(items);
  }; //This returns an array of all the keys the dictionary contains.

  this.values = function(){
    var vals = [];
    for(var item in items) {
      vals.push(items[item]);
    }
    //console.log(Object.values(items));
    // return Object.values(items);
    return vals;
  }; //This returns an array of all the values of the dictionary.

  this.getItems = function() {
    return items;
  }
}