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

    var omikuji_comment = [
        '<p>「おさんぽ中に素敵な風景に出会えそう！」</p>',
        '<p>「おさんぽで姿勢が良くなる予感！」</p>',
        '<p>「おさんぽすると運気上昇！」</p>',
        '<p>「おさんぽ中に思い出せなかったことが思い出せるかも！」</p>',
        '<p>「おさんぽすると美味しいご飯に出会えるかも！」</p>',
        '<p>「おさんぽすると骨密度UP！」</p>',
        '<p>「おさんぽ中に懐かしの友と再会するかも！」</p>',
        '<p>「おさんぽしたら思わぬ臨時収入があるかも！」</p>',
        '<p>「おさんぽでビタミンDを作り出そう！」</p>',
        '<p>「おさんぽで迷わず家に帰れたあなたは、まだ大丈夫！」</p>',
    ];

    var num = Math.floor(Math.random() * omikuji_comment.length);
    var random_comment = omikuji_comment[num];

    $(".omikuji_comment").html(random_comment);

});

$(".hum_menu").on("click",function(){
    $("header").toggleClass("open");
});

});