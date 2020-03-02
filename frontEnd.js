function ajaxGetRequest(path, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("GET", path);
    request.send();
}




function getData(){
  ajaxGetRequest("/charts", table)
  ajaxGetRequest("/pies", pieChart)
}

function table(notanything){
  let final2 = JSON.parse(notanything)
  let data2009 = final2["2009"]
  let data2010 = final2["2010"]
  let data2011 = final2["2011"]
  let data2012 = final2["2012"] 
  var values = [
        ['Manhattan', 'Bronx', 'Brooklyn', 'Queens','Staten Island', '<b>TOTAL</b>'],
        [data2009["Manhattan"], data2009["Bronx"], data2009["Brooklyn"], data2009["Queens"], data2009["Staten Island"], data2009["TOTAL"]],
        [data2010["Manhattan"], data2010["Bronx"], data2010["Brooklyn"], data2010["Queens"], data2010["Staten Island"], data2010["TOTAL"]],
        [data2011["Manhattan"], data2011["Bronx"], data2011["Brooklyn"], data2011["Queens"], data2011["Staten Island"], data2011["TOTAL"]],
        [data2012["Manhattan"], data2012["Bronx"], data2012["Brooklyn"], data2012["Queens"], data2012["Staten Island"], data2012["TOTAL"]]]

  var data = [{
    type: 'table',
    header: {
      values: [["<b>Years</b>"], ["<b>2009</b>"],
				  ["<b>2010</b>"], ["<b>2011</b>"], ["<b>2012</b>"]],
      align: "center",
      line: {width: 1, color: 'black'},
      fill: {color: "grey"},
      font: {family: "Arial", size: 12, color: "white"}
    },
    cells: {
      values: values,
      align: "center",
      line: {color: "black", width: 1},
      font: {family: "Arial", size: 11, color: ["black"]}
    }
  }]
  var layout = {
  title: 'Homeless Population By Year in New York City'
  }
  Plotly.plot('graph_table', data, layout);
}


function pieChart(anything){
  console.log(anything)
  let final = JSON.parse(anything)
  var data = [{
    values: [final["Manhattan"], final["Bronx"], final["Brooklyn"], final["Queens"], final["Staten Island"]],
    labels: ['Manhattan', 'Bronx', 'Brooklyn','Queens', 'Staten Island'],
    type: 'pie'
  }];

  var layout = {
    title:"Homeless Population in New York City By Specifc Years",
    height: 400,
    width: 500
  };

  Plotly.newPlot('pie', data, layout);
}

function requestData(year){
  let toSend = JSON.stringify(year);
    ajaxPostRequest("/send", toSend, pieChart);
    console.log(toSend)
}

function ajaxPostRequest(path, data, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}