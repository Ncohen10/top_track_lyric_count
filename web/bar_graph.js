function setUpBarGraph(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            var get_lyrics = getGraphParams(this.response);
            Plotly.newPlot('bar_graph', get_lyrics);
        }
    };
    xhttp.open("GET", "../lyrics");
    xhttp.send();
}
function getGraphParams(this_response) {
    var normal = JSON.parse(this_response);
    var params = [{x: normal["x"], y: normal["y"], type: "bar"}];
    return params;
}