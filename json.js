"use strict";

let myRequest = new Request("../convertcsv.json");

fetch(myRequest)
    .then(function(resp){
        return resp.json();

    })
    .then(function(data){
        console.log(data);
        var table = document.getElementById('myTable');

		for (var i = 0; i < data.length; i++){
			var row = `<tr>
							<td>${data[i].ProjectID}</td>
							
					  </tr>`
            table.innerHTML += row
        console.log('hello');
        }
    });