function getValuesFromType (selector) {
	var elems = $(selector);
	var data = [];
	elems.each(function(y,x){
		if (x.id !== "submitForm") {
			var temp = {"label":x.id, "value":x.value};
			data.push(temp);
		};
	});
	return data;
}

function checkSum (selector) {
	var elems = $(selector);
	var sum = 0;
	for (var i = 0; i < elems.length; i++) {
		if (elems[i].id !== "submitForm") {
			sum += parseInt(elems[i].value);
		}
	};
	var msg = "Total: " + sum + "%";
	var disable = false;
	if (sum > 100) {
		msg += "\n Sum exceeds 100% :(";
		disable = true;
	};
	if (sum < 100) {
		msg += "\n Sum is less than 100% :(";
		disable = true
	};
	showMessage(msg);
	disableSubmit(disable);
}

function disableSubmit (bool) {
	if (bool) {
		$("input[type=submit]").attr('disabled','disabled');
	} else{
		$("input[type=submit]").removeAttr('disabled');
	};
}

function showMessage(msg){
	$("#msg").html(msg);
}

$("input").change(function(){
	checkSum("input");
	createChart(getValuesFromType("input"));
})

createChart(getValuesFromType("input"));
checkSum("input");
