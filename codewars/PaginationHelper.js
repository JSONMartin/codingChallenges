// The constructor takes in an array of items and a integer indicating how many
// items fit within a single page
function PaginationHelper(collection, itemsPerPage){
  console.log(collection, itemsPerPage)
  this._collection = collection;
  this._pages = [];
  this._itemsPerPage = itemsPerPage;
  
  for (let i = 0; i < collection.length; i += itemsPerPage) {
    this._pages.push(collection.slice(i, i + itemsPerPage));
  }
  
  console.log(this._pages);
}

// returns the number of items within the entire collection
PaginationHelper.prototype.itemCount = function() {
  return this._collection.length;
}

// returns the number of pages
PaginationHelper.prototype.pageCount = function() {
  return this._pages.length;
}

// returns the number of items on the current page. page_index is zero based.
// this method should return -1 for pageIndex values that are out of range
PaginationHelper.prototype.pageItemCount = function(pageIndex) {
  try {  
    return this._pages[pageIndex].length
  } catch(e) {
    return -1;
  }
}

// determines what page an item is on. Zero based indexes
// this method should return -1 for itemIndex values that are out of range
PaginationHelper.prototype.pageIndex = function(itemIndex) {
console.log("itemINdex:", itemIndex);
  return itemIndex <= this._collection.length && itemIndex >= 0 && this._collection.length > 0 
          ? parseInt(itemIndex / this._itemsPerPage) : -1;
}


