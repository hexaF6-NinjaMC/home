const requestURL = 'json/temple-info.json';

fetch(requestURL)
.then(function (response) {return response.json();})
.then(function (jsonObject) {
    const temples = jsonObject['temples'];
    temples.forEach(displaySelectTemple);
});

function displaySelectTemple(temple) {
    if (temple.featured === "yes") {
        // Create elements to add to the document
        let card = document.querySelector('#featured');
        let h4 = document.createElement('h4');
        let announcement = document.createElement('p');
        let groundbreaking = document.createElement('p');
        let image = document.createElement('img');
    
        // Change the textContent property of the h4 element to contain the temple name
        h4.textContent = `Featured: ${temple.name}`;

        // Change the textContent property of the p elements to contain the temple's announcement and groundbreaking dates
        announcement.textContent = `Announcement: ${temple.milestones.announcement}`;
        groundbreaking.textContent = `Groundbreaking: ${temple.milestones.groundbreaking}`;
    
        // Set the image attributes by using the setAttribute method for the src, alt, and loading attribute values
        image.setAttribute('src', temple.image);
        image.setAttribute('alt', `Picture of ${temple.name}`);
        image.setAttribute('id', 'featured-temple')
        image.setAttribute('loading', 'lazy');
    
        // Add/append the section(card) with the h4 element
        card.appendChild(image);
        card.appendChild(h4);
        card.appendChild(announcement);
        card.appendChild(groundbreaking);
    }
}