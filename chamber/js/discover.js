/*
lazy-loading script
*/
const images = document.querySelectorAll('[data-src]');

const loadImages = (image) => {
    image.setAttribute('src', image.getAttribute('data-src'));
    image.onload = () => {image.removeAttribute('data-src');};
};

if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((items, observer) => {
        items.forEach((item) => {
            if (item.isIntersecting) {
                loadImages(item.target);
                observer.unobserve(item.target);
            }
        });
    });

    images.forEach((image) => {
        observer.observe(image);
    });
} else {
    images.forEach((image) => {
        loadImages(image);
    });
}

/*
localStorage script
*/
const timeOfLoad = Date.now();
const displayVisitsElem = document.querySelector('#visitsLSBanner');
const numberDecimalFormat = 0; //no decimal places

let lastUserVisit = Number(window.localStorage.getItem('ls-visits'));

const daysInMillSec = 1000 * 60 * 60 * 24; //1000ms/1sec, 60sec/1minute, 60min/1hr, 24hr/1d
let daysFormatToWholeNumber = 0; //initialize day number format

if (lastUserVisit) {
    let daysSpanLastVisit = timeOfLoad - lastUserVisit;
    daysFormatToWholeNumber = (daysSpanLastVisit / daysInMillSec).toFixed(numberDecimalFormat);
}

if (daysFormatToWholeNumber > 0) {
    displayVisitsElem.innerHTML = `You last visited us ${daysFormatToWholeNumber} days ago.`
} else {
    displayVisitsElem.textContent = `This is your first visit. Welcome to GPC!`;
}

localStorage.setItem('ls-visits', timeOfLoad);