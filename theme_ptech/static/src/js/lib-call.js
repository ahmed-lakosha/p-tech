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
                    items: 1,
                    nav: false,
                },
                768: {
                    items: 2,
                    nav: true,
                },
                992: {
                    items: 3,
                    nav: true,
                },
                1200: {
                    items: 4,
                    nav: true,
                },
            },
        });
    });
});
