const requestURL = 'json/temple-info.json';
const cards = document.querySelector('#temple-cards');
const loadedTime = Date.now();

let number = 0;

fetch(requestURL)
.then(function (response) {return response.json();})
.then(
    window.addEventListener('DOMContentLoaded', n => {
    while (n <= window.localStorage.length) {
        let key = window.localStorage.key(n);
        document.querySelector(`.${key}`).removeAttribute('src');
        document.querySelector(`.${key}`).setAttribute('src', `${window.localStorage.getItem(key)}`);
    };
}))
.then(function (jsonObject) {
    const temples = jsonObject['temples'];
    temples.forEach(displayTemples);
    
});

function displayTemples(temple) {
    // Create each element to add to the document
    let card = document.createElement('section');
    let templeImg = document.createElement('img');
    let name = document.createElement('h3');
    let announcement = document.createElement('p');
    let groundbreaking = document.createElement('p');
    let dedication = document.createElement('p');
    let likeBtn = document.createElement('img');

    // Change the textContent of the h3 to the Temple name
    name.textContent = `${temple.name}`;

    // Change the textContent of the p elements to groundbreaking, announcement, and dedicatory dates
    announcement.textContent = `Announcement: ${temple.milestones.announcement}`;
    groundbreaking.textContent = `Groundbreaking: ${temple.milestones.groundbreaking}`;
    dedication.textContent = `1st Dedication: ${temple.milestones.dedicatory}`;

    // Set the image attributes of the Temple info
    templeImg.setAttribute('src', temple.image);
    templeImg.setAttribute('alt', `Picture of the ${temple.name} of the Church of Jesus Christ of Latter-Day Saints`);
    templeImg.setAttribute('loading', 'lazy');
    templeImg.setAttribute('width', '100%');

    let likeBtnKeys = localStorage.getItem(`likeBtns-${number}`);

    // Set the likeBtn image up
    if (likeBtnKeys != `likedBtn-${number}`) {
        likeBtn.setAttribute('src', 'images/assets/like.png');
    } else {
        likeBtn.setAttribute('src', 'images/assets/like-colored.png');
    }
    likeBtn.setAttribute('alt', 'Like button');
    likeBtn.setAttribute('width', '20px');
    likeBtn.setAttribute('class', `likeImg-${number}`);
    likeBtn.setAttribute('onclick', `changeImg(${number})`);

    // Add/append the temple cards data
    card.appendChild(templeImg);
    card.appendChild(name);
    card.appendChild(likeBtn);
    card.appendChild(announcement);
    card.appendChild(groundbreaking);
    card.appendChild(dedication);

    // Add/append the card to the document
    document.querySelector('#temple-cards').appendChild(card);
    number ++;
}