$(function(){
    var $menu = $('nav > ul > li');
        $header = $('header');
    $menu.mouseover(function(){
        $header.animate({height:'300px'},300);
    })
    .mouseout(function(){
        $header.stop().animate({height:'90px'},300);
    });
})