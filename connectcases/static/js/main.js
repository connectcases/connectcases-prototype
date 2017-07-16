var setUpClickableTeeth = function setUpClickableTeeth(){
    var $diagram = $('#teeth-diagram');

    var shadeToothIfMissing = function shadeMissingTeeth(jaw, side, tooth){
        var $tooth = $('path[jaw="' + jaw + '"][side="' + side + '"][tooth="' + tooth + '"]', $diagram);
        var $input = $('input[name="' + jaw + '_' + side + '_' + tooth + '"]');
        if( $input.is(':checked') ){
            $tooth.addClass('missing');
        } else {
            $tooth.removeClass('missing');
        }
    };

    $('path[tooth]', $diagram).on('click keypress', function(e){
        e.preventDefault();
        var tooth = $(this).attr('tooth');
        var jaw = $(this).attr('jaw');
        var side = $(this).attr('side');
        var $input = $('input[name="' + jaw + '_' + side + '_' + tooth + '"]');
        $input.trigger('click');
    });

    $('input[type="checkbox"]').on('click', function(){
        var jst = $(this).attr('name').split('_'); // eg: "upper_left_4" -> ["upper", "left", "4"]
        shadeToothIfMissing(jst[0], jst[1], jst[2]);

    }).each(function(){
        var jst = $(this).attr('name').split('_'); // eg: "upper_left_4" -> ["upper", "left", "4"]
        shadeToothIfMissing(jst[0], jst[1], jst[2]);
        $(this).parents('.form-group').hide();
    });
};

var setUpColetLines = function setUpColetLines(){
    var $diagram = $('#teeth-diagram');
    var $upper_colet_from = $('select[name="upper_colet_from"]');
    var $upper_colet_to = $('select[name="upper_colet_to"]');
    var $lower_colet_from = $('select[name="lower_colet_from"]');
    var $lower_colet_to = $('select[name="lower_colet_to"]');

    var hideColetLines = function hideColetLines(){
        $('path[jaw][left][right]', $diagram).hide(0); // back borders
        $('path[jaw][side][colet]', $diagram).hide(0); // colet edges
    };

    var drawColetLinesBetween = function drawColetLinesBetween(jaw, from_side, from_tooth, to_side, to_tooth){
        $('path[jaw="' + jaw + '"][' + from_side + '="' + from_tooth + '"][' + to_side + '="' + to_tooth + '"]', $diagram).show(0);
        for( var i=from_tooth; i>0; i-- ){
            $('path[jaw="' + jaw + '"][side="' + from_side + '"][colet="' + i + '"]', $diagram).show(0);
        }
        for( var i=to_tooth; i>0; i--){
            $('path[jaw="' + jaw + '"][side="' + to_side + '"][colet="' + i + '"]', $diagram).show(0);
        }
    };

    $('select[name*="_colet_"]').on('change', function(){
        hideColetLines();

        if( $upper_colet_from.val() && $upper_colet_to.val() ){
            var from_jst = $upper_colet_from.val().split('_');
            var to_jst = $upper_colet_to.val().split('_');
            drawColetLinesBetween(
                from_jst[0],
                from_jst[1],
                from_jst[2],
                to_jst[1],
                to_jst[2]
            );
        }

        if( $lower_colet_from.val() && $lower_colet_to.val() ){
            var from_jst = $lower_colet_from.val().split('_');
            var to_jst = $lower_colet_to.val().split('_');
            drawColetLinesBetween(
                from_jst[0],
                from_jst[1],
                from_jst[2],
                to_jst[1],
                to_jst[2]
            );
        }
    });

    $upper_colet_from.trigger('change');
};

var setUpDraggableColets = function setUpDraggableColets(){
    var $diagram = $('#teeth-diagram');
    var colet_dragging_from = {};

    $('path[tooth]', $diagram).on('mousedown', function(e){
        colet_dragging_from = {
            tooth: $(this).attr('tooth'),
            jaw: $(this).attr('jaw'),
            side: $(this).attr('side')
        };
    }).on('mouseover', function(e){
        if( colet_dragging_from.jaw == $(this).attr('jaw') ){
            if( colet_dragging_from.side != $(this).attr('side') ){
                if( colet_dragging_from.side == 'right'){
                    var from = 'from';
                    var to = 'to';
                } else {
                    var from = 'to';
                    var to = 'from';
                }

                $('select[name="' + colet_dragging_from.jaw + '_colet_' + from + '"]')
                    .val(colet_dragging_from.jaw + '_' + colet_dragging_from.side + '_' + colet_dragging_from.tooth)
                    .change();
                $('select[name="' + $(this).attr('jaw') + '_colet_' + to + '"]')
                    .val($(this).attr('jaw') + '_' + $(this).attr('side') + '_' + $(this).attr('tooth'))
                    .change();
            }
        }
    }).on('mouseup', function(e){
        colet_dragging_from = {};
    });

    $('select[name*="_colet_"]').parents('.form-group').hide();
};

$(function(){
    if( $('#teeth-diagram').length ){
        setUpClickableTeeth();
        setUpColetLines();
        setUpDraggableColets();
    }
});
