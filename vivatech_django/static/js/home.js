window.jQuery = window.$ = jQuery;

$(document).ready(function(){
    // 'use strict';

    // Hero Slider
    var mySwiper = new Swiper('.hero-slider', {
        slidesPerView: 1,
        speed: 800,
        spaceBetween: 0,
        loop: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
            renderBullet: function (index, className) {
                return '<span class="' + className + '">0' + (index + 1) + '</span>';
            },
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
        }
    });
    var mySwiper = document.querySelector('.hero-slider').swiper

    function nextSlide(){
        mySwiper.slideNext();
    }
    
    var mySwiperInterval = setInterval(nextSlide, 3700);


    // Testimonial Slider
    var swiper = new Swiper('.testimonial-slider-wrap', {
        slidesPerView: 1,
        spaceBetween: 0,
        loop: true,
        effect: 'fade',
        speed: 800,
        pagination: {
            el: '.swiper-pagination',
            clickable: true
        }
    });
})