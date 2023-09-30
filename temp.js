let number=0;
function addFields(){
    document.getElementById("submit").remove();
    // Generate a dynamic number of inputs
    number = document.getElementById("comp").value;    
    // Get the element where the inputs will be added to
    var container = document.getElementById("container");
    // Remove every children it had before
    while (container.hasChildNodes()) {
        container.removeChild(container.lastChild);
    }
    for (i=0;i<number;i++){
        var label=document.createElement("label");
        var input = document.createElement("input");
        label.style="font-size: 30px; margin-left: 100px;";
        label.innerText="Enter the name of City " + (i+1) + ": ";
        input.type = "text";
        input.name = "city" + i;
        input.id = "city" + i;
        input.style = "height: 25px; width: 200px; font-size: 30px";
        container.appendChild(label);
        container.appendChild(input);
        // Append a line break 
        container.appendChild(document.createElement("br"));
        container.appendChild(document.createElement("br"));
    }
    document.getElementById("compare").style.visibility="visible";
}

function compare(){
    let csvdata="";
    for (i=0;i<number;i++){
        csvdata+=document.getElementById("city" + i).value+',';
    }
    let anchor = document.createElement('a');
    anchor.href = 'data:text/csv;charset=utf-8,' + encodeURI(csvdata);
    anchor.target = '_blank';
    anchor.download = 'Temp_Data.csv';
    anchor.click();
}
   