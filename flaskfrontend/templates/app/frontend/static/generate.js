$(document).ready(function(e){

    $("#addButton").click(function(e){

        e.preventDefault;

    canvas = document.getElementById('canvas');

    console.log(canvas.toDataURL());

    $.post("/uploadImage", {"theImage" : canvas.toDataURL()}, 
    function(data){
        $("#answer").text(data.message);
    });
});

    $("#clearButton").click(function(e){
        context.clearRect(0, 0, canvas.width, canvas.height)
    });

});
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

ctx.fillStyle = 'white';
window.onload=function(){
        var canvas = new fabric.Canvas('sheet');
        canvas.isDrawingMode = true;
        canvas.freeDrawingBrush.width = 15;
        canvas.freeDrawingBrush.color = "#008000"};

console.log()

$(document).getElementById('clear').addEventListener('click', 
    function () {
        context.clearRect(0, 0, canvas.width, canvas.height)
    }, false);