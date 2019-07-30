function setUpPieChart(){
        var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            var data = getPieParams(this.response);
            var layout = {height: 400, width: 500};
            Plotly.newPlot('pie_chart', data, layout);
        }
    };
    xhttp.open("GET", "../lyrics");
    xhttp.send();
}
function getPieParams(this_response) {
    var normal = JSON.parse(this_response);
    var params = [{values: normal["y"], labels: normal["x"], type: 'pie'}];
    return params
}