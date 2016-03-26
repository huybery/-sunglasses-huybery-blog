/**
 * Created by huybery on 16-3-25.
 */
$(function() {
function scroll_fn(){

    document_height = $(document).height();
    scroll_so_far = $(window).scrollTop();
    window_height = $(window).height();

	max_scroll = document_height-window_height;

	scroll_percentage = scroll_so_far/(max_scroll/100);

    $('#loading').width(scroll_percentage + '%');

}
$(window).scroll(function() {
scroll_fn();
});
$(window).resize(function() {
scroll_fn();
});
});

//go_up
$(document).ready(function(){
        //首先将#back-to-top隐藏
            $(".go_up").hide();
            //当滚动条的位置处于距顶部100像素以下时，跳转链接出现，否则消失
            $(function () {
                $(window).scroll(function(){
                if ($(window).scrollTop()>400){
                    $(".go_up").fadeIn(800);}
                else{
                    $(".go_up").fadeOut(800);}
                });
//当点击跳转链接后，回到页面顶部位置
            $(".go_up").click(function () {
                var speed=800;//滑动的速度
                $('body,html').animate({ scrollTop: 0 }, speed);
                return false;});
            });
        });










