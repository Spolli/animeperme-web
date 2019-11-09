< script type = "text/javascript" >

    function goToVideo(anime) {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                //document.getElementById("demo").innerHTML = this.responseText;
            }
        };
        xhttp.open("POST", anime, true);
        xhttp.send();
    }

    function goToVideo(anime) {
        console.log(anime);
        $.ajax({
            type: "POST",
            contentType: "application/json; charset=utf-8",
            url: "/",
            data: anime,
            success: function (data) {
                console.log(data);
            },
            dataType: "json"
        });
    } 
</script>