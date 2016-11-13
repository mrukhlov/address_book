/**
 * Created by s4d_panda on 13-Nov-16.
 */
$(document).ready(function() {

    $('#make_csv').click(function(){
        $.ajax({
            url: "/make_csv/",
            contentType: 'application/x-www-form-urlencoded;charset=UTF-8',
            type: "POST",
            error: function (data) {
                console.log(data);
                alert('Oops, something went wrong. Check console.');
            },
            success: function (data) {
                location.replace('/make_csv/');
            }
        })
    })

});