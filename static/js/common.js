$(function(){

$(".omikuji_btn").on("click",function(){

    var omikuji = [
        '../static/images/大吉.png',
        '../static/images/中吉.png',
        '../static/images/末吉.png',
        '../static/images/吉.png'
        ];

    var num = Math.floor(Math.random() * omikuji.length);
    var random_img = omikuji[num];

    $('.omikuji_random').attr('src', random_img);
});

});