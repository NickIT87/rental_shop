$(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown({
        hover: true
    });
    $('.tooltipped').tooltip();
    $('.collapsible').collapsible();

    $('.collapsible li._sidebar').each(function(index){
        let location = window.location.pathname;
        if(location.includes(this.id)){
            console.log(index);
            $('.collapsible').collapsible('open', index);
        }
    });

});