$(document).ready(function(){
    $("#login").click(function(){
        obj=$.ajax({
            url:"http://192.168.174.1/login",
            asyn: false,
            data: {username: $("#exampleInputEmail").val(), password: $("#exampleInputPassword").val()},
            dataType: "json",
            type: "post",
            success: function(data) {
                if(data.succeed == "true") {
                    window.location.href = "http://192.168.174.1/index"
                }
            }
        })
    })
});