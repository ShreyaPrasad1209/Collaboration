const csvFilePath = './output.csv';
const csv = require('csvtojson');
let obj;
let obj1=[];
csv().fromFile(csvFilePath).then((jsonObj) => {
    obj = jsonObj;
    for (let i = 0; i < obj.length; i++) {
        obj1.push(obj[i]['ProjectID'])
    }
});

const jsonArray = csv().fromFile(csvFilePath);
document.querySelector('Aloo').addEventListener('click',function(){
    console.log('hello')
    appendData();
});
function appendData() {
    var mainContainer = document.getElementById("recommendation");
    for (var i = 0; i < jsonArray.length; i++) {
      var div = document.createElement("div");
      div.innerHTML = 'yo';
      mainContainer.appendChild(div);
    }
  }


