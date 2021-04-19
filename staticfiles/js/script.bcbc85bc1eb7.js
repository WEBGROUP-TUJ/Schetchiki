var h1 = document.querySelector("#print");
var x = h1.innerHTML;
h1.innerHTML = "";
var i = 0;
function write() {
    h1.innerHTML = h1.innerHTML + x[i];
    i++;
    if (i < x.length) {
        setTimeout(write, 100);
    }

}
setTimeout(function () {
    write();
}, 1500);

$(".mob_but").on('click', function () {
    $(".mob-li").slideToggle()
})

const swiper = new Swiper('.swiper-container', {
    // Optional parameters
    // cssMode: true,
    spaceBetween: 100,
    loop: true,
    effect: 'coverflow',
    speed: 1000,
    autoplay: {
        delay: 4000,
        disableOnInteraction: false,
    },

    // If we need pagination

    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    // And if we need scrollbar
    scrollbar: {
        el: '.swiper-scrollbar',
    },
});