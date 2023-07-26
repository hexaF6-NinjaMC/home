const compilationDate = new Date(2020, 11, 20);
const month = compilationDate.getMonth() + 1; /* set the month value to 1 through 12, not 0-based. */
const day = compilationDate.getDate();
const year = compilationDate.getFullYear();
const formatDate = `${month}.${day}.${year}`;

const spanElem = document.querySelector('span');
spanElem.innerText = formatDate;