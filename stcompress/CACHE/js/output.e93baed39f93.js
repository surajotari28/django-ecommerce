;$(document).ready(function(){"use strict";$(document).on('click','.dropdown-menu',function(event){event.stopPropagation();});if($(window).width()>780){$(window).scroll(function(){if($(this).scrollTop()>125){$('.sticky').addClass('sticky-top');}else{$('.sticky').removeClass('sticky-top');}});}
if($('[data-fancybox="gallery"]').length>0){$('[data-fancybox="gallery"]').fancybox();}
if($('.slick-slider').length>0){$('.slick-slider').slick({centerPadding:'40px',infinite:true,slidesToShow:5,slidesToScroll:4,responsive:[{breakpoint:992,settings:{arrows:true,centerPadding:'20px',slidesToShow:3}},{breakpoint:768,settings:{arrows:true,centerPadding:'20px',slidesToShow:3}},{breakpoint:600,settings:{slidesToShow:2,slidesToScroll:2}},{breakpoint:480,settings:{arrows:false,centerPadding:'50px',slidesToShow:1}}]});}
if($('.owl-init').length>0){$(".owl-init").each(function(){var myOwl=$(this);var data_items=myOwl.data('items');var data_nav=myOwl.data('nav');var data_dots=myOwl.data('dots');var data_margin=myOwl.data('margin');var data_custom_nav=myOwl.data('custom-nav');var id_owl=myOwl.attr('id');myOwl.owlCarousel({loop:true,margin:data_margin,nav:eval(data_nav),dots:eval(data_dots),autoplay:true,items:data_items,navText:["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"],items:4,responsive:{0:{items:1},600:{items:data_items},1000:{items:data_items}}});$('.'+data_custom_nav+'.owl-custom-next').click(function(){$('#'+id_owl).trigger('next.owl.carousel');});$('.'+data_custom_nav+'.owl-custom-prev').click(function(){$('#'+id_owl).trigger('prev.owl.carousel');});});}
new WOW().init();if($('.grid').length>0){$(".grid").each(function(){$('.grid').masonry({itemSelector:'.grid-item',columnWidth:160,gutter:20});});$('.grid').imagesLoaded().progress(function(){$grid.masonry()});}});