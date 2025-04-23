$(function () {
    "use strict";

    // select function
    $(document).ready(function () {
        $("#services .owl-carousel").owlCarousel({
            margin: 36,
            autoHeight: false,
            autoHeightClass: 'owl-height',
            loop: true,
            autoplay: true,
            autoplayTimeout: 7000,
            touchDrag: true,
            dots: false,
            responsive: {
                0: {
                    slideBy: 1,
                    items: 1,
                    nav: false,
                },
                768: {
                    slideBy: 2,
                    items: 2,
                    nav: true,
                },
                992: {
                    slideBy: 3,
                    items: 3,
                    nav: true,
                },
                1200: {
                    slideBy: 4,
                    items: 4,
                    nav: true,
                },
            },
        });
        $("#partners .owl-carousel").owlCarousel({
            margin: 36,
            autoHeight: false,
            autoHeightClass: 'owl-height',
            loop: true,
            autoplay: true,
            autoplayTimeout: 7000,
            touchDrag: true,
            dots: false,
            responsive: {
                0: {
                    slideBy: 2,
                    items: 2,
                    nav: false,
                },
                768: {
                    slideBy: 3,
                    items: 3,
                    nav: true,
                },
                992: {
                    slideBy: 4,
                    items: 4,
                    nav: true,
                },
                1200: {
                    slideBy: 5,
                    items: 5,
                    nav: true,
                },
            },
        });
        $("#odoo_apps .owl-carousel").owlCarousel({
            margin: 36,
            autoHeight: false,
            autoHeightClass: 'owl-height',
            loop: true,
            autoplay: true,
            autoplayTimeout: 7000,
            touchDrag: true,
            dots: false,
            nav: false,
            responsive: {
                0: {
                    items: 2,
                },
                768: {
                    items: 4,
                },
            },
        });
    });
});
