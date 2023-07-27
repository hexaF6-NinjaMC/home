const now = new Date();
const fullDate = new Intl.DateTimeFormat("en-UK", { dateStyle: "full" }).format(now);
const currentYear = now.getFullYear();
const author = "Aaron Bechtel";
const locationOfAuthor = "Oklahoma";
const footerTextContent = `${currentYear} | ${author} | ${locationOfAuthor}`;

let footerTextElement = document.querySelector("#footer-text");
footerTextElement.append(footerTextContent);

let date = document.lastModified;
let updateElement = document.querySelector("#last-update");
updateElement.append(date);