rotateArray : function(a, b){
		ret=[];
		for (var i = 0; i < a.length; i++) {
		    var pos = (b + i) % a.length
		    ret.push(a[pos]);
		}
		return ret;
	}
