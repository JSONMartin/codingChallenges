function ArrayList(){

  var array = []; //{1}

  this.insert = function(item){ //{2}
    array.push(item);
  };

  this.toString= function(){ //{3}
    return array.join();
  };

  this.length = function() {
    return array.length;
  };

  /*
     BUBBLE SORT: Time Complexity O(N^2)

     Bubble sort works by iterating through the array, swapping each element one by one.
     Then, moves to the next position in the array and loops through until the end
   */

  this.bubbleSort = function() { // Version from the book
    for(var outer = 0; outer < array.length; outer++) {
      for(var inner = 0; inner < array.length - 1; inner++) {
        if(array[inner] > array[inner + 1]) {
          swap(inner, (inner+1));
        }
      }
    }
  };

  this.modifiedBubbleSort = function(){
    var length = array.length;
    for (var i=0; i<length; i++){
      for (var j=0; j<length-1-i; j++ ){ //{1} length - 1 - i, the last i elements will have already been sorted
        if (array[j] > array[j+1]){
          swap(j, j+1);
        }
      }
    }
  };

  this.recursiveBubbleSort = function () { // My Recursive version
    var done = true;
    for(var i = 0; i < array.length; i++) {
      if(array[i] > array[i + 1]) {
        swap(i, (i+1));
        done = false;
      }
    }
    if(!done) { this.bubbleSort(); }
  };

  /*
    SELECTION SORT: Time Complexity? O^n2?

   “The selection sort algorithm is an in-place comparison sort algorithm.
   The general idea of the selection sort is to find the minimum value in the data structure
   and place it in the first position, then find the second minimum value and place it in the
   second position, and so on.”

   */

  this.selectionSort = function() {

    for(var i = 0; i < array.length; i++) {
      var minIndex = i;
      for(var j = i; j < array.length; j++) {
        if(array[j] < array[minIndex]) {
          minIndex = j;
        }
      }
      if(i !== minIndex) {
        swap(minIndex, i);
      }
      //console.log("Swapping:", minIndex, i)
    }
  };

  /*
   INSERTION SORT

   “The insertion sort algorithm builds the final sorted array one item at a time.
   It assumes that the first element is already sorted.
   Then, a comparison with the second item is performed—should the second item stay in its place or be inserted before the first item?
   So, the first two items get sorted and the comparison takes place with the third item (should it be inserted in the first,
   second, or third position?), and so on.”
   */

  this.insertionSortBookVersion = function(){ //BOOK VERSION
      var length = array.length,            //{1}
        j, temp;
      for (var i=1; i<length; i++){         //{2}
        j = i;                            //{3}
        temp = array[i];                  //{4}
        while (j>0 && array[j-1] > temp){ //{5}
          array[j] = array[j-1];        //{6}
          j--;
        }
        array[j] = temp;                  //{7}
      }
    };

  this.insertionSort = function () { // MY VERSION
    var results = [];
    var arr = array.slice();
    results.push(arr.shift());
    while(arr.length > 0) {
      for(var i = 0; i < arr.length; i++) {
        var elem = arr.shift();
        // console.log("----------");
        // console.log("arr:", arr);
        // console.log("Results:", results);
        // console.log("ELEM:", elem);
        var swapped = false;
        for(var j = 0; j < results.length; j++) {
          if(elem < results[j]) {
            //results.splice(j, 0, arr.splice(i, 1)[0])
            results.splice(j, 0, elem);
            swapped = true;
            break;
          }
        }
        if(!swapped) {
          results.push(elem);
        }
        // console.log("arr:", arr);
        // console.log("Results:", results);
        // console.log("----------");
      }
    }
    array = results;
  };

  /*
    MERGE SORT: Time complexity — O(log n), logarithmic time because it works through binary search (splitting list in half)

   “The merge sort algorithm is the first sorting algorithm that can be used in the real world.
   The three first sorting algorithms you learned in this book do not give a good performance,
   but the merge sort gives a good performance, with a complexity of O(n log n).”

   “The merge sort is a divide and conquer algorithm. The idea behind it is to divide the original array
   into smaller arrays until each small array has only one position and then merge these smaller arrays
   into bigger ones until we have a single big array at the end that is sorted.”

   “Note that first the algorithm splits the original array until it has smaller arrays
    with a single element, and then it starts merging. While merging,
    it does the sorting as well until we have the original array completely back together and sorted.”
   */

  // My first attempt version is much worse than the book version, over 20X worse.
  this.mergeSortFirstAttempt = function() { // This version is much worse than the book version, over 20X worse.
    var divideArray = function(arr) {
      var length = arr.length;
      var midpoint = Math.floor( (length) /2);
      //console.log("Divide Array called, arr:", arr);
      //console.log("Length:", length);
      //console.log("midpoint:", midpoint);
      if(length <= 1) {
        return arr;
      }
      var left = divideArray(arr.slice(0, midpoint));
      var right = divideArray(arr.slice(midpoint, length));
      //console.log("Left:", left);
      //console.log("right:", right);
      if(left < right) {
        return [left, right];
      } else {
        return [right, left];
      }
    };
    array = divideArray(array);
  };

  //My second attempt, much better than the first but still not as good as book
  this.mergeSortSecondAttempt = function() { // My Second attempt, much better than the first but still not as effective as the books

    var recurse = function(arr) {
      var len = arr.length;

      if(len === 1) {
        return arr;
      }


      var mid = Math.floor( len / 2);

      return merge( (recurse(arr.slice(0, mid))), (recurse(arr.slice(mid, len))) );
    };

    var merge = function(left, right) {
      var results = [];
      //console.log("Left:", left);
      //console.log("right:", right);

      while(left.length && right.length) {
        if(left[0] < right[0]) {
          results.push(left.shift());
        } else {
          results.push(right.shift());
        }
      }

      while(left.length) {
        results.push(left.shift());
      }

      while(right.length) {
        results.push(right.shift());
      }

      return results;
    };

    array = recurse(array.slice());

  };

  // My Third Attempt
  this.mergeSortThirdAttempt = function() {

    var recurse = function(arr) {
      var len = arr.length;

      if(len === 1) {
        return arr;
      }

      var mid = Math.floor( len / 2);
      //return merge( (recurse(arr.slice(0, mid))), (recurse(arr.slice(mid, len))) );

      var left = arr.slice(0, mid);
      var right = arr.slice(mid, len);

      return merge( recurse(left), recurse(right) );

    };

    var merge = function(left, right) {
      var results = [];
      //console.log("Left:", left);
      //console.log("right:", right);

      while(left.length && right.length) {
        if(left[0] < right[0]) {
          results.push(left.shift());
        } else {
          results.push(right.shift());
        }
      }

      while(left.length) {
        results.push(left.shift());
      }

      while(right.length) {
        results.push(right.shift());
      }

      return results;
    };

    array = recurse(array.slice());

  };

  // My Fourth Attempt
  // Here, instead of shifting off the element in the merge function,
  // I use an increment counter and loop through the arr without modifying
  this.mergeSortFourthAttempt = function() {

    var recurse = function(arr) {
      var len = arr.length;

      if(len === 1) {
        return arr;
      }

      var mid = Math.floor( len / 2);
      //return merge( (recurse(arr.slice(0, mid))), (recurse(arr.slice(mid, len))) );

      var left = arr.slice(0, mid);
      var right = arr.slice(mid, len);

      return merge( recurse(left), recurse(right) );

    };

    var merge = function(left, right) {
      var results = [], leftCounter = 0, rightCounter = 0;

      while(leftCounter < left.length && rightCounter < right.length) {
        if(left[leftCounter] < right[rightCounter]) {
          results.push(left[leftCounter++]);
        } else {
          results.push(right[rightCounter++]);
        }
      }

      while(leftCounter < left.length) {
        results.push(left[leftCounter++]);
      }

      while(rightCounter < right.length) {
        results.push(right[rightCounter++]);
      }

      return results;
    };

    array = recurse(array.slice());
  };

  this.mergeSortBook = function() {
    var mergeSortRec = function(array){
      var length = array.length;
      if(length === 1) {      //{1}
        return array;       //{2}
      }
      var mid = Math.floor(length / 2),     //{3}
        left = array.slice(0, mid),       //{4}
        right = array.slice(mid, length); //{5}

      return merge(mergeSortRec(left), mergeSortRec(right)); //{6}
    };

    var merge = function(left, right){
      var result = [], // {7}
        il = 0,
        ir = 0;
      while(il < left.length && ir < right.length) { // {8}
        if(left[il] < right[ir]) {
          result.push(left[il++]);  // {9}
        } else{
          result.push(right[ir++]); // {10}
        }
      }

      while (il < left.length){    // {11}
        result.push(left[il++]);
      }

      while (ir < right.length){   // {12}
        result.push(right[ir++]);
      }

      return result; // {13}
    };

    array = mergeSortRec(array);
  };

  /*
  QUICK SORT

   “The quick sort is probably the most used sorting algorithm. It has a complexity of O(n log n),
   and it usually performs better than other O(n log n) sorting algorithms.
   Like the merge sort, it also uses the divide and conquer approach,
   dividing the original array into smaller ones (but without splitting them as the merge sort does) to do the sorting.

   The quick sort algorithm is a little bit more complex than the other ones you have learned so far.
   Let's learn it step by step as follows:

   First, we need to select an item from the array that is called as a pivot, which is the middle item in the array.
   We will create two pointers—the left one will point to the first item of the array and the right one will point
   to the last item of the array. We will move the left pointer until we find an item that is bigger than the pivot
   and we will also move the right pointer until we find an item that is less than the pivot and we will swap them.
   We repeat this process until the left pointer passes the right pointer. This process helps to have values lower
   than the pivot before the pivot and values greater than the pivot after the pivot. This is called the partition operation.

   Next, the algorithm repeats the previous two steps for smaller arrays (sub-arrays with smaller values,
   and then sub-arrays with greater values) until the array is completely sorted.”
   */

  this.quickSortMyFirstAttempt = function () {

    var results = [];

    function quickSort(arr, left, right) {
      //console.log("Quicksort called with:", arr);
      if(arr.length === 1) {
        results.push(arr[0]);
        return arr;

      }
      if(left >= right) { return true; }
      var mid = Math.floor( (arr.length - 1) / 2);
      var pointer = arr[mid];
      left = 0;
      right = arr.length - 1;

      //console.log("mid:", arr[mid]);
      //console.log("left:", arr[left]);
      //console.log("right:", arr[right]);


      while(left <= right) {
        //console.log("-----------------");
        //console.log("pointer:", pointer);
        //console.log("left:", left, " VALUE:", arr[left]);
       // console.log("right:", right, " VALUE:", arr[right]);

        while( (left < arr.length - 1) && (arr[left] < pointer) ) {
          left++;
        }

        while( right > 0 && (arr[right] > pointer) ) {
          right--;
        }

        if(left > right) {
          break;
        }

        //console.log("Left stopped on position:", left, "Value:", arr[left]);
        //console.log("right stopped on position:", right, "Value:", arr[right]);
        //if(arr[left] > pointer && arr[right] < pointer) {
          swap(left, right, arr);
          //console.log("!!!Swapping " + arr[left] + " with " + arr[right]);
          left++;right--;
        //}
        //console.log("-----------------")
    }
      //console.log("Ending LEFT:", left);
      //console.log("Ending right:", right);
      //console.log("ENDING ARR:", arr);

      // quickSort(arr.slice(0, mid)); // Sort lower half
      // quickSort(arr.slice(mid, arr.length)); // Sort lower half
      var lh = quickSort(arr.slice(0, left)); // Sort lower half
      var rh = quickSort(arr.slice(left, arr.length)); // Sort lower half

      //results.concat(lh).concat(rh);
      //results.push(arr);
      //quickSort(arr.slice(right, arr.length)); // Sort upper half
      return arr;
      //quickSort(arr, 0, left -1);
      //quickSort(arr, left, right);
      // return arr;
    }

    // array = quickSort(array, 0, array.length - 1);
    quickSort(array, 0, array.length - 1);
    //console.log("ENDING RESULTS:", results);
    array = results;
    return results;
  };

  this.quickSortMySecondAttemptUnrevised = function () {

    var partition = function(left, right) {
      var start = left, end = right;
      //Select middle element as "pivot"
      var pivot = Math.floor( (right+left) / 2); //If starting on left half of array, left will be zero, so will add to zero at end. If right half of array, need to add starting left to get correct middle value

      while(left < right) {

        while(array[left] < array[pivot]) { //Move left pointer until it finds an element > pivot
          left++;
        }

        while(array[right] > array[pivot]) {  //Move right pointer until it finds an element < pivot
          right--;
        }

        if(left < right) {
          swap(left, right);
        }
      }

      if(Math.abs(start- (pivot - 1)) > 1) {
        partition(start, pivot - 1); //partition elements on left side of pivot
      }
      if(Math.abs(end- (pivot + 1) ) > 1) {
        partition(pivot + 1, end); //partition elements on right side of pivot
      }
    };

    partition(0, array.length - 1);
  };

  this.quickSortMySecondAttemptComments = function () {

    var partition = function(left, right) {
      console.log("----------------------------");
      console.log("Partition called with:", array.slice(left, right + 1)); //Slice extracts up to, but not including end (which is why it has to be length of array, not len - 1

      //Select middle element as "pivot"
      if(Math.abs(right - left) <= 0) { return; }


      var start = left, end = right;
      var pivotPos = Math.floor( (right+left) / 2); //If starting on left half of array, left will be zero, so will add to zero at end. If right half of array, need to add starting left to get correct middle value
      var pivot = array[pivotPos];
      console.log("Pivot Position:", pivot, " | value:", pivot);

      while(left <= right) {
        console.log("Initial Left:", left, " | value:", array[left]);
        console.log("Initial right:", right, " | value:", array[right]);
        //Move left pointer until it finds an element > pivot
        while(array[left] < pivot) {
          left++;
        }

        //Move right pointer until it finds an element < pivot
        while(array[right] > pivot) {
          right--;
        }

        if(left <= right) {
          //Swap left & right elements
          console.log("Left position to swap:", left, " | value:", array[left]);
          console.log("right position to swap:", right, " | value:", array[right]);
          swap(left, right);
          left++; //Increment left pointer
          right--; //Decrement right pointer
        }
      }

      // if(left === right) {
      //   left++;right--;
      // }

      console.log("ending left:", left, " | value:", array[left]);
      console.log("ending right:", right, " | value:", array[right]);
      console.log("RESULTS SUBARRAY:", array.slice(start, end + 1)); //Slice extracts up to, but not including end (which is why it has to be length of array, not len - 1
      console.log("Results after partition call:", array);
      console.log("----------------------------\n");

      //if(Math.abs( start - (left - 1) ) > 1) {
      partition(start, left - 1); //partition elements on left side of pivot
      // }
      //if(Math.abs( end- (left + 1) ) > 1) {
      partition(left, end); //partition elements on right side of pivot
      //}
    };

    partition(0, array.length - 1);
  }; //Revised

  this.quickSortMySecondAttempt = function () { //Without comments for speed test

    var partition = function(left, right) {

      //Select middle element as "pivot"
      if(Math.abs(right - left) <= 0) { return; } //Base case, means that the array is length of 1 or less

      var start = left, end = right;

      var pivotPos = Math.floor( (right+left) / 2); //If starting on left half of array, left will be zero, so will add to zero at end. If right half of array, need to add starting left to get correct middle value
      var pivot = array[pivotPos];

      while(left <= right) {

        while(array[left] < pivot) { //Move left pointer until it finds an element > pivot
          left++;
        }

        while(array[right] > pivot) { //Move right pointer until it finds an element < pivot
          right--;
        }

        if(left <= right) { //Swap left & right elements
          swap(left, right);
          left++; //Increment left pointer after swap
          right--; //Decrement right pointer after swap
        }
      }
      partition(start, left - 1); //partition elements on left side of pivot
      partition(left, end); //partition elements on right side of pivot
    };
    partition(0, array.length - 1);
  };

  this.quickSort = function () {

    var quick = function(array, left, right){

      var index; //{1}

      if (array.length > 1) { //{2}

        index = partition(array, left, right); //{3}

        if (left < index - 1) {		      //{4}
          quick(array, left, index - 1);     //{5}
        }

        if (index < right) {                   //{6}
          quick(array, index, right);        //{7}
        }
      }
    };

    var partition = function(array, left, right) {

      var pivot = array[Math.floor((right + left) / 2)], //{8}
        i = left,                                      //{9}
        j = right;                                     //{10}

      while (i <= j) {                //{11}
        while (array[i] < pivot) {  //{12}
          i++;
        }
        while (array[j] > pivot) {  //{13}
          j--;
        }
        if (i <= j) { //{14}
          swap(i, j, array); //{15}
          i++;
          j--;
        }
      }
      return i; //{16}
    };

    quick(array, 0, array.length - 1);
  };

  function swap(a, b, arr) {
    array = arr || array;
    var temp = array[a];
    array[a] = array[b];
    array[b] = temp;
  }

  /*




  SEARCHING ALGORITHMS!!!



   */

  /*
  SEQUENTIAL SEARCh
   */

  this.sequentialSearch = function(item) {
    for(var i = 0; i < array.length; i++) {
      if(item === array[i]) { return i; }
    }
    return -1;
  };

  this.binarySearchRecursive = function (item) { //Assumes array is sorted
    var found = false;

    var search = function(arr) {
      var midPoint = Math.floor( (arr.length - 1) / 2 ); //Calculate midpoint of array

      //Check if middle value === item, if so return true
      if(arr[midPoint] === item) {
        found = true;
        return found;
      }
      else {
        if(arr.length <= 1) { return; } //Base Case
        // if middle value is > item, check left half of array
        if(arr[midPoint] > item) {
          search(arr.slice(0, midPoint));
        }
        if(arr[midPoint] < item) {
          search(arr.slice(midPoint + 1, arr.length));
        }
        // if middle value is < item, check right half of array
      }
    };

    search(array.slice());
    return found;
  };

  this.binarySearchWhileVersion = function (item) { //Assumes array is sorted

    var start = 0, end = (array.length - 1);
    var mid = Math.floor( (start+end) / 2);
    while(mid !== start && mid !== end) { //Book has while( start <= end
      mid = Math.floor( (start+end) / 2);
      if(array[mid] === item) {
        return mid;
      } else {
        if(array[mid] > item) { //Check left half
          end = mid - 1;
        } else if(array[mid] < item){
          start = mid + 1;
        }
      }
    }
    return -1;
  };

  this.binarySearch = function(item){
    //this.quickSort();  //{1}

    var low = 0,                 //{2}
      high = array.length - 1, //{3}
      mid, element;

    while (low <= high){ //{4}
      mid = Math.floor((low + high) / 2); //{5}
      element = array[mid];               //{6}
      if (element < item) {               //{7}
        low = mid + 1;                  //{8}
      } else if (element > item) {        //{9}
        high = mid - 1;                 //{10}
      } else {
        return mid;                     //{11}
      }
    }
    return -1; //{12}
  };
}

function createNonSortedArray(size){ //{6}
  var array = new ArrayList();
  for (var i = size; i> 0; i--){
    array.insert(i);
  }
  return array;
}

/******************************************
 * TESTS
 ******************************************/


var array = createNonSortedArray(100000); //{7}
//var array = createNonSortedArray(8); //{7}

//var array = createNonSortedArray(0);
//array.insert(3);array.insert(5);array.insert(1);array.insert(6);array.insert(4);array.insert(7);array.insert(2);array.insert(0);
//array.insert(65);array.insert(72);array.insert(23);array.insert(36);array.insert(99);array.insert(20);array.insert(1);array.insert(44);array.insert(-300);array.insert(2);


console.log("Array length:", array.length());
//console.log("BEFORE SORT:", array.toString());          //{8}
var before = new Date().getTime();

//array.bubbleSort(); console.log("Bubble Sort"); // Approx 300 MS for  createNonSortedArray(10000);

//array.modifiedBubbleSort(); console.log("Modified Bubble Sort"); // Approx 180 MS for  createNonSortedArray(10000);

//array.selectionSort(); console.log("Selection Sort"); // Approx 115 MS for  createNonSortedArray(10000);

//array.insertionSortBookVersion(); console.log("Insertion Sort — Book version"); // Approx 95 MS for  createNonSortedArray(10000);
//array.insertionSort(); console.log("Insertion Sort — My version"); // Approx 30 MS for  createNonSortedArray(10000); //YAY!! MINE IS MORE EFFICIENT!!!

// Approx 220 MS for createNonSortedArray(10000);
// Approx 2600 MS for createNonSortedArray(100000);
//array.mergeSortFirstAttempt(); console.log("Merge Sort — My First Attempt");

// Approx 45 MS for createNonSortedArray(10000)
// Approx 260 MS for createNonSortedArray(100000);
// An order of magnitude more efficient than my first, ~10X faster
//array.mergeSortSecondAttempt(); console.log("Merge Sort — My Second Attempt");

// Approx 45 MS for createNonSortedArray(10000), equal to second attempt
// Approx 260 MS for createNonSortedArray(100000);
//array.mergeSortThirdAttempt(); console.log("Merge Sort — My Third Attempt");

// Approx 35 MS for createNonSortedArray(10000), better than third and equal to book
// Approx 120 MS for createNonSortedArray(100000)
// The difference is in shifting off element from array, rather than iterating. Adds to runtime
// Because it has to alter the array each pass, rather than iterate through it
//array.mergeSortFourthAttempt(); console.log("Merge Sort — My Fourth Attempt");

// Approx 35 MS for createNonSortedArray(10000), better than third and equal to book
// Approx 120 MS for createNonSortedArray(100000)
//array.mergeSortBook(); console.log("Merge Sort — Book version"); // Approx 35 MS for createNonSortedArray(10000), better than third equal to book

//array.quickSortMyFirstAttempt(); // Approx 12 MS for createNonSortedArray(10000)
array.quickSortMySecondAttempt(); // Approx 3 MS for createNonSortedArray(10000); 8-12 MS for 100,000; 50-60MS for 1,000,000; 750MS for 10,000,000 — MINE IS MORE EFFICIENT! Most likely because not slicing into subarray!
//array.quickSort(); // Approx 4 MS for createNonSortedArray(10000),; 12-15 MS for 100,000; 75-85MS for 1,000,000; 875MS for 10,000,000


var after = new Date().getTime();
var difference = after - before;

if(array.length() <= 10000) {
  console.log("RESULTS AFTER SORT:", array.toString());       //{10}
}

console.log("Runtime in MS:", difference + "ms");

console.log("-------------------");

before = new Date().getTime();

var found = array.binarySearch(1500);
console.log("Binary Search Found:", found);

after = new Date().getTime();
difference = after - before;
console.log("Runtime for SEARCH in MS:", difference + "ms");

/*
// var a = new ArrayList();
// // a.insert(4);a.insert(1);a.insert(2);a.insert(3);a.insert(5);
// // a.insert(4);a.insert(1);a.insert(5);a.insert(3);a.insert(2);
// a.insert(3);a.insert(5);a.insert(1);a.insert(2);a.insert(4);
// console.log(a.toString());
// var before = new Date().getTime();
//  a.bubbleSort();
// // a.selectionSort();
// //a.insertionSort();
// var after = new Date().getTime();
// var difference = after - before;
// console.log("Runtime in MS:", difference + "ms");
// console.log(a.toString());
//
*/