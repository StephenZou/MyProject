$(document).ready(function () {
   $("#begin-analysis").click(function () {
       const text = $("#text-analysis").val();
       $.ajax({
           url: '/analysis',
           async: true,
           contentType: 'application/json',
           data: {
               corpus: text
           },
           success: function (result) {
                let tr_str='';
                result.data.forEach(function (item,index) {
                    tr_str=tr_str+"<tr><td>" + item['person'] + "</td><td>" + item['view'] + "</td></tr>"
                })
                const table_str = "<table class=\"table table-bordered\" id=\"dataTable\" width=\"100%\" cellspacing=\"0\">" +
                    "<thead><tr><th>Person</th><th>View</th></tr></thead><tbody>"+tr_str+"</tbody></table>";
                $("#result").empty();
                $("#result").append(table_str);
           }
       });
   })
    $("#textrank").click(function () {
        summary('/text_rank_summary');
    })
    $("#embedding").click(function () {
        summary('/embedding_rank_summary')
    })
    function summary(url) {
        const text = $("#text-summary").val();
        $.ajax({
            url:url,
            async: true,
            contentType: 'application/json',
            data: {
                textInfo: text
            },
            success: function (result) {
                const tr_str="<tr><td>Summary</td><td>" + result["summary"] + "</td></tr>"
                const table_str = "<table class=\"table table-bordered\" id=\"dataTable\" width=\"100%\" cellspacing=\"0\">" +
                    "<tbody><tr><td>Text</td><td>" + text + "</td></tr>"+tr_str+"</tbody></table>";
                $("#result").empty();
                $("#result").append(table_str);
            }
        })
    }
});