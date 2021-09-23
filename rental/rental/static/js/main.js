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
        min: 1000,
        max: 40000,
        values: [ 3000, 25000 ],
        slide: function( event, ui ) {
            $( "#amount" ).val( "$  " + ui.values[ 0 ] + "   -   $  " + ui.values[ 1 ] );
            $( "#am1" ).val(ui.values[ 0 ]);
            $( "#am2" ).val(ui.values[ 1 ]);
        }
    });
    $( "#amount" ).val( "$  " + $( "#price-slider" ).slider( "values", 0 ) +
        "   -   $  " + $( "#price-slider" ).slider( "values", 1 ) );
    $( "#am1" ).val($( "#price-slider" ).slider( "values", 0 ));
    $( "#am2" ).val($( "#price-slider" ).slider( "values", 1 ));

    // select initialize for searchform
    $('select').formSelect();
    // logic for search form select item
    if (performance.navigation.type == 1) {
        // reload page logic when page is reloaded
        if($("#sot_sel").val() == "Apartment") {
            $("#sfrc").show()
        } else {
            $("#sfrc").hide()
        }
        if($("#sot_sel").val() == "House") {
            $("#setl").show()
        } else {
            $("#setl").hide()
        }
    } else {
        // default value enabling on loaded page
        if($("#sot_sel").val() == "Apartment") {
            $("#sfrc").show()
        } else {
            $("#sfrc").hide()
        }
    }
    // select object type menu change function
    $("#sot_sel").change(function(){
        if($(this).val() == "Apartment") {
            $("#sfrc").show()
        } else {
            $("#sfrc").hide()
        }
        if($(this).val() == "House") {
            $("#setl").show()
        } else {
            $("#setl").hide()
        }
    });
    // promotion slider
    var elems = document.querySelectorAll('.slider');
    var instance = M.Slider.init(elems);
    instance.start();
});