// https://www.codewars.com/kata/deodorant-evaporator/train/javascript

function evaporator(content, evap_per_day, threshold){
  let thresholdAmt = content * (threshold / 100), days = 0;

  while (content > thresholdAmt) {
    content *= ((100 - evap_per_day) / 100);
    days++;
  }

  return days;
}
