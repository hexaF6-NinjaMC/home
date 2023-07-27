/* Date objects to be modified */
const now = new Date();
const fullDate = new Intl.DateTimeFormat("en-UK", {dateStyle: "full"}).format(now);

/* Footer date script */
const currentYear = now.getFullYear();
const currentDay = now.getDay();
const author = "Aaron Bechtel";
const locationOfAuthor = "Oklahoma";
const headerTextContent = `${fullDate}`;
const footerTextContent = `${currentYear} Great Plains C.O.C. | ${author} | ${locationOfAuthor}`;
let footerTextElement = document.querySelector("#footer-text");
footerTextElement.append(footerTextContent);
let date = document.lastModified;
let updateElement = document.querySelector("#last-update");
updateElement.append(date);

/* Header date script */
let headerDateTextElement = document.querySelector("#header-date");
headerDateTextElement.append(headerTextContent);

/* Banner invitation to join script */
let bannerElem = document.querySelector('#banner');
if (currentDay === 1 || currentDay === 2) {
    // const dayOfWeek = 'Monday'
    bannerElem.stlye = 'display: block;';
    bannerElem.style.backgroundColor = 'burlywood';
} else {
    bannerElem.style = 'display: none;';
}