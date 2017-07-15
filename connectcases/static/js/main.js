var setUpClickableTeeth = function setUpClickableTeeth(){
    var $diagram = $('#teeth-diagram');

    $('path', $diagram).on('click keypress', function(e){
        e.preventDefault();
        var id = $(this).attr('id'); // eg: "tooth-upper-left-4"
        var $input = $('#id_' + id.replace(/teeth-/g, '').replace(/-/g, '_'));
        $input.trigger('click');
    });

    $('input[type="checkbox"]').on('click', function(){
        var id = $(this).attr('name'); // eg: "upper_left_4"
        var $tooth = $('#teeth-' + id.replace(/_/g, '-'));
        if( $(this).is(':checked') ){
            $tooth.addClass('missing');
        } else {
            $tooth.removeClass('missing');
        }
    }).each(function(){
        var id = $(this).attr('name'); // eg: "upper_left_4"
        var $tooth = $('#teeth-' + id.replace(/_/g, '-'));
        if( $(this).is(':checked') ){
            $tooth.addClass('missing');
        } else {
            $tooth.removeClass('missing');
        }
    })
};

$(function(){
    if( $('#teeth-diagram').length ){
        setUpClickableTeeth();
    }
});
