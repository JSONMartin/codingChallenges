/**
 * Created by jsonmartin on 5/30/16.
 */


// Brute force approach
// function maxSubArray(a) {
//   var arr = a.slice();
//   var max = parseInt(arr[0]);
//   var end = 0;
//
//   while(arr.length > 1) {
//     var curArr = arr.slice(0, end + 1);
//     //console.log("Cur Arr:", curArr);
//     var total = curArr.reduce(function(prev, cur) {
//       return parseInt(prev) + parseInt(cur);
//     });
//     //console.log("Total:", total);
//     max = Math.max(total, max);
//     if(end >= arr.length) {
//       end = 0;
//       arr.shift();
//     } else {
//       end++;
//     }
//   }
//
//   //console.log("Max:" + max);
//   return max;
// }

function maxSubArray(a) {
  var ans = -5000, sum = 0, hasPositive = false, maxSeenNum = -5000;
  for(var i = 0; i < a.length; ++i) {
    maxSeenNum = Math.max(maxSeenNum, parseInt(a[i]));
    if(!hasPositive && parseInt(a[i]) > 0) { hasPositive = true; }
    if(sum + parseInt(a[i]) > 0) {
      sum+=parseInt(a[i]);
    } else {
      sum = 0;
    }
    ans = Math.max(ans, sum);
  }

  //console.log("hasPositive:", hasPositive);

  if(!hasPositive) {
    return maxSeenNum;
    // ans = -99999;
    // a.forEach(function(num) {
    //   //console.log(num);
    //   ans = Math.max(ans, parseInt(num));
    // });
  }
  //console.log("Ans:", ans);
  return ans;
}



//var res = maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]);
//var res = maxSubArray([ -120, -202, -293, -60, -261, -67, 10, 82, -334, -393, -428, -182, -138, -167, -465, -347, -39, -51, -61, -491, -216, -36, -281, -361, -271, -368, -122, -114, -53, -488, -327, -182, -221, -381, -431, -161, -59, -494, -406, -298, -268, -425, -88, -320, -371, -5, 36, 89, -194, -140, -278, -65, -38, -144, -407, -235, -426, -219, 62, -299, 1, -454, -247, -146, 24, 2, -59, -389, -77, -19, -311, 18, -442, -186, -334, 41, -84, 21, -100, 65, -491, 94, -346, -412, -371, 89, -56, -365, -249, -454, -226, -473, 91, -412, -30, -248, -36, -95, -395, -74, -432, 47, -259, -474, -409, -429, -215, -102, -63, 80, 65, 63, -452, -462, -449, 87, -319, -156, -82, 30, -102, 68, -472, -463, -212, -267, -302, -471, -245, -165, 43, -288, -379, -243, 35, -288, 62, 23, -444, -91, -24, -110, -28, -305, -81, -169, -348, -184, 79, -262, 13, -459, -345, 70, -24, -343, -308, -123, -310, -239, 83, -127, -482, -179, -11, -60, 35, -107, -389, -427, -210, -238, -184, 90, -211, -250, -147, -272, 43, -99, 87, -267, -270, -432, -272, -26, -327, -409, -353, -475, -210, -14, -145, -164, -300, -327, -138, -408, -421, -26, -375, -263, 7, -201, -22, -402, -241, 67, -334, -452, -367, -284, -95, -122, -444, -456, -152, 25, 21, 61, -320, -87, 98, 16, -124, -299, -415, -273, -200, -146, -437, -457, 75, 84, -233, -54, -292, -319, -99, -28, -97, -435, -479, -255, -234, -447, -157, 82, -450, 86, -478, -58, 9, -500, -87, 29, -286, -378, -466, 88, -366, -425, -38, -134, -184, 32, -13, -263, -371, -246, 33, -41, -192, -14, -311, -478, -374, -186, -353, -334, -265, -169, -418, 63, 77, 77, -197, -211, -276, -190, -68, -184, -185, -235, -31, -465, -297, -277, -456, -181, -219, -329, 40, -341, -476, 28, -313, -78, -165, -310, -496, -450, -318, -483, -22, -84, 83, -185, -140, -62, -114, -141, -189, -395, -63, -359, 26, -318, 86, -449, -419, -2, 81, -326, -339, -56, -123, 10, -463, 41, -458, -409, -314, -125, -495, -256, -388, 75, 40, -37, -449, -485, -487, -376, -262, 57, -321, -364, -246, -330, -36, -473, -482, -94, -63, -414, -159, -200, -13, -405, -268, -455, -293, -298, -416, -222, -207, -473, -377, -167, 56, -488, -447, -206, -215, -176, 76, -304, -163, -28, -210, -18, -484, 45, 10, 79, -441, -197, -16, -145, -422, -124, 79, -464, -60, -214, -457, -400, -36, 47, 8, -151, -489, -327, 85, -297, -395, -258, -31, -56, -500, -61, -18, -474, -426, -162, -79, 25, -361, -88, -241, -225, -367, -440, -200, 38, -248, -429, -284, -23, 19, -220, -105, -81, -269, -488, -204, -28, -138, 39, -389, 40, -263, -297, -400, -158, -310, -270, -107, -336, -164, 36, 11, -192, -359, -136, -230, -410, -66, 67, -396, -146, -158, -264, -13, -15, -425, 58, -25, -241, 85, -82, -49, -150, -37, -493, -284, -107, 93, -183, -60, -261, -310, -380 ]);
//var res = maxSubArray([ -418, -186, 30, -103, -58, 17, -155, -294, -428, 53, -198, 36, -219, -34, -278, -7, 63, -258, -144, -325, -100, -35, -315, 57, -263, 66, -59, -347, -142, -390, -101, -460, -357, -149, -20, -96, 71, -96, -430, -92, -483, -244, 16, -234, -327, -390, -48, -291, -98, -67, -54, -274, -19, -207, -442, -382, -167, -103, -14, -409, 94, -16, -32, -12, -46, -80, -93, -499, -240, -117, -168, 94, -62, -414, -32, -272, -282, -99, -45, -363, -101, -239, 52, -484, -315, -459, 52, -14, -286, -147, -274, -231, -116, -408, -46, -133, -415, -157, -141, -119, -113, -498, -241, 62, -68, -428, -246, -52, -494, -422, -360, -477, 21, -386, -151, -92, -137, -401, -114, -249, 25, -322, -313, -199, 32, -488, 5, -416, -328, -91, 48, -414, -388, -367, 73, -16, -233, -100, -368, 79, -235, -110, -345, -329, 27, 37, -380, -296, -390, -92, -140, -110, -113, -204, -299, -101, -491, -19, -487, -16, -219, 68, -237, -156, -314, -494, -166, -422, 62, -164, -83, -162, 44, -450, -154, -399, 12, -61, -433, -48, -228, -31, -145, -4, 95, -141, 72, -21, -14, 66, -149, -347, -238, 71, -82, -89, -463, -397, -457, -312, -6, -196, -326, -117, -443, -10, 14, -194, -48, -383, -124, 90, 58, -309, -419, -453, -221, 92, -107, -366, 24, -395, 22, 100, 98, -107, -391, -457, -197, 21, -208, 25, -320, -479, -406, -496, 20, -481, -473, 71, -255, -102, 68, -457, -148, -220, 61, -449, -354, -124, -312, 2, 64, 73, 34, -238, -94, -299, -307, -348, -140, -271, -490, -389, 65, -193, 47, -108, -20, -234, -483, 89, -182, -483, -178, -367, -364, 37, -47, -97, -202, -55, -429, -234, -107, 70, -446, -462, -179, -119, -210, 66, -239, -58, -435, -343, 4, -119, 28, -124, 13, 74, -452, -362, 26, -149, -480, -168, -402, -238, 96, 90, -167, -213, -202, -458, -225, -358, 24, -488, -209, -302, -161, -383, -39, -466, -384, -166, -236, -238, -38, -375, -492, -218, -352, 47, 10, 37, -268, -268, -248, 91, -425, -375, -374, 31, 0, 42, 21, -178, 41, -49, -337, 10, -395, -472, -432, -198, -411, -48, 55, 67, -382, 13, -499, 30, -98, 92, -34, -410, -488, -408, -257, -153, -301, -338, -247, -241, -97, -197, -212, -1, -240, -391, -460, 88, -71, 49, -111, -309, 19, -427, -213, -28, 44, -27, 85, -322, -157, -338, -383, -473, -316, -315, -458, -319, 23, -97, -303, -128, -238, -239, -303, -19, -258, -183, -133, -407, -486, 49, -381, -393, 52, -289, -403, -438, 39, -288, -497, -197, 32, -146, -284, -460, -409, -431, 78, -77, -313, 79, -293, -12, -281, -74, -304, -96, -123, -413, -198, -306, -39, -495, -276, -466, 18, -360, -347, -441, -326, -290, 93, -230, -86, -74, 11, -226, -362, -276, -372, 79, -285, -191, -60, -214, -105, 38, -474, -149, -82, -256, 58, -446, 3, 99, -308, -287, 62, -192, -39, -106, -396, -196, -307, 14, -90, -150, -447, -110, -13, -262, 74, -78, -262, -337, -499, -58, -359, -461, -438, -318, -22, -413, 18, -374, -206, -317, -308, -345, -495, 15, -326, -112, 81, -455, -125, 38, -3, 6, 12, -357, -122, -132, 40, -248, 61, -180, -87, -273, -334, -228, -77, -165, -404, -375, 64, 18, -36, -44, -244, -54, -171, -340, -26, -489, -317, 56, -233, 9, 4, -221, -337, -147, -465, -237, -372, -326, 90, -183, -250, -256, -338, -104, -155, -475, -200, -269, -367, -13, -147, -236, -218, -64, -290, 64, 83, -316, -98, -378, 71, -125, -346, -238, -252, -304, -44, -452, -420, -38, -291, -103, -259, -66, -84, 54, -288, -470, 56, -178, 18, -125, -156, -345, -252, -464, 13, -306, 57, -473, -278, -445, -35, -283, -116, -300, -242, -499, -424, -200, 3, -317, -264, -293, -33, -95, -285, -396, -344, -167, -256, -254, -51, -489, -161, 37, -28, -302, 61, -28, -177, 85, -42, 5, -451, -375, -140, -400, 81, 69, -169, -136, -249, 42, -41, -482, 42, -42, -17, -119, 59, -446, -423, -190, -396, 0, -157, -341, -248, -325, -51, -445, -470, -422, -464, -185, -228, -123, -182, -471, -391, -84, -191, -308, -316, -121, -382, -402, -426, 18, 92, -489, -351, -11, -174, 88, 40, -189, -394, -70, -359, -48, -235, 74, 64, -423, -151, -16, 4, 90, -24, -368, -287, 81, -69, 88, -469, 85, -235, -143, -52, 37, -215, -41, -383, -8, -441, -158, -404, -367, -164, -260, 67, -196, -401, -405, 92, -263, -353, 62, -422, -500, -183, -464, -426, -341, -345, 36, -500, -371, 73, -339, -207, -282, -174, 54, -76, -126, 42, -251, 75, -86, -49, -324, 69, -388, -472, -336, -27, -212, -197, 73, -68, -241, -82, -161, -72, 39, -279, -316, -230, 82, 45, -233, -47, -396, -444, -68, 26, 70, -216, -438, -331, -295, -437, -389, -324, -372, -357, -121, -5, -479, -416, -135, 31, -279, -333, -479, 85, -294, -272, -384, -251, -176, -172, -77, -428, -54, 58, -422, -199, -258, -270, -114, -132, -135, 99, -342, -76, 55, 37, -110, -462, -17, -245, -131, -67, -414, -184, -460, -49, -427, -412, -19, -266, -200, -259, -433, -500, -487, -248, -288, 73, -166, 80, -21, 69, -4, -498, -447, 5, -438, -345, -303, -28, -203, -236, -305, -255, -353, -122, -346, -219, -405, -226, 36, -141, -30, -297, -358, -306, -147, -364, 13, -299, -90, -293, -107, -114, -475, 58, -67, 72, -90, 49, -113, -159, -301, 38, -383, -57, 7, -487, -276, -266, -48, -281, -52, 66, -60, -238, -443, -445, -304, 32, -407, -79, -110, -418, -44, -287, 100, -111, -67, -416, 60, 79, -86, -15, -65, -440, -296, -449, 44, -492, -256, -296, -18, -80, -131, 89, -79, -123, -120, -490, 11, 13, -395, -69, -447, -148, -481, -229, -368, -431, 32, -285, -105, 67, -169, -423, -238, -265, -6, 52, 34, -130, 12, -418 ]);
//var res = maxSubArray([-500]);
var res = maxSubArray([ -163, -20 ]);
console.log(res);
