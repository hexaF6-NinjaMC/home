const currentYear = new Date().getFullYear();
const author = "Aaron Bechtel";
const locationOfAuthor = "Oklahoma";
const footerTextContent = `${currentYear} | ${author} | ${locationOfAuthor}`;

let footerTextElement = document.querySelector("#footer-text");
footerTextElement.append(footerTextContent);

let date = document.lastModified;
let updateElement = document.querySelector("#last-update");
updateElement.append(date);