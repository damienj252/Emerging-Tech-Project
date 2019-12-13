$(document).ready(function(e){

    $("#addButton").click(function(e){

        e.preventDefaul;
    });

    $.post("/uploadImage", {theImage : canvas.toDataURL()}, function(data){
        $("#answer").text(data.message);
    });

    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');

    ctx.fillStyle = 'white';

    console.log(canvas.toDataURL())
});