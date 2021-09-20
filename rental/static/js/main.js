$(document).ready(function(){
    // home page scripts
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown({
        hover: true
    });
    $('.tooltipped').tooltip();
    $('.collapsible').collapsible();

    // apartments sidebar
    $('.collapsible li._sidebar').each(function(index){
        let location = window.location.pathname;
        if(location.includes(this.id)){
            console.log(index);
            $('.collapsible').collapsible('open', index);
        }
    });

    // apartment detail scripts
    $('.carousel').carousel();
    if ($("[data-fancybox]").length) {
        $("[data-fancybox]").fancybox()
    }

    // commercial structure
    $('.materialboxed').materialbox();

    // find object (search) form
    $('input#enter_search_text').characterCounter();

    // price slider
    $( "#price-slider" ).slider({
        range: true,
        min: 0,
        max: 500,
        values: [ 75, 300 ],
        slide: function( event, ui ) {
            $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
            $( "#am1" ).val(ui.values[ 0 ]);
            $( "#am2" ).val(ui.values[ 1 ]);
        }
    });
    $( "#amount" ).val( "$" + $( "#price-slider" ).slider( "values", 0 ) +
        " - $" + $( "#price-slider" ).slider( "values", 1 ) );
    $( "#am1" ).val($( "#price-slider" ).slider( "values", 0 ));
    $( "#am2" ).val($( "#price-slider" ).slider( "values", 1 ));

});