function createChart(data) {
	$("svg").empty()
	nv.addGraph(function() {
	    var chart = nv.models.pieChart()
	      .x(function(d) { return d.label })
	      .y(function(d) { return d.value })
	      .showLabels(true);

	    d3.select("#chart svg")
	        .datum(data)
	      .transition().duration(1200)
	        .call(chart);
	          return chart;
	});
}

function getValuesFromType (selector) {
	var elems = $(selector);
	var data = [];
	elems.each(function(y,x){
		var temp = {"label":x.id, "value":x.value};
		data.push(temp);
	});
	return data
}

$("input").change(function(){
	createChart(getValuesFromType("input"));
})

createChart(getValuesFromType("input"));
