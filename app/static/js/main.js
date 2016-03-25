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









