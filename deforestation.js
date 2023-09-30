let number=0;
function submit(){
    let csvdata="";
    csvdata+=document.getElementById("states").value;
    let anchor = document.createElement('a');
    anchor.href = 'data:text/csv;charset=utf-8,' + encodeURI(csvdata);
    anchor.target = '_blank';
    anchor.download = 'Deforestation.csv';
    anchor.click();
}
   