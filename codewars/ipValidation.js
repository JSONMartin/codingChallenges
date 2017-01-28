function isValidIP(str) {
  const ipStr = str.split('.').map(i => parseInt(i));
  
  // Abort cases
  if (!str || /[a-zA-Z]| /.test(str) || ipStr.length !== 4) return false;
  
  // Check each IP segment is within range
  for (let ipSegment of ipStr) {        
    if (ipSegment < 0 || ipSegment > 255) { return false; }
  }
  
  // All IP segments are valid, return true
  return true;
}
