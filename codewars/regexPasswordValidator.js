const validate = password => /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])\w{6,}$/.test(password)
    
// Other way to solve this without lookaheads, and probably faster would be like this:
//return /[a-z]/.test(password) && /[A-Z]/.test(password) && /[0-9]/.test(password) && password.length >= 6;


///// TESTING ///////
validate("djI38D55")