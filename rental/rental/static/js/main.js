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
});