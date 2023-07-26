const postListEl = document.querySelector('#repo-link-list');
const copyYearEl = document.querySelector('#copy-year');
const copyHolderEl = document.querySelector('#copy-holder');

const anchors = [
  {
    text: "BYU-I - Frontend Web Design and Development I",
    url: "./wdd230/"
  },
  {
    text: "BYU-I - Frontend Web Design and Development II",
    url: "./wdd330/"
  },
  {
    text: "A MSWord-2-HTML Python program to auto fill notes",
    url: "./wdd330/py/"
  },
  {
    text: "Showcasing the temples of the Church of Jesus Christ of Latter-Day Saints, while enjoying a stay at the Temple Inn & Suites",
    url: "./wdd230/temple-inn-and-suites/"
  },
  {
    text: "A DOM-manipulation example, allowing you to present your favorite chapter from the Book of Mormon",
    url: "./wdd230/dom-practice/bom.html"
  }
];

anchors.forEach((anchor) => {
  const liElTemplate = `
<li><a href="${anchor.url}" target="_blank">${anchor.text}</a></li>
  `;

  postListEl.appendChild(liElTemplate);
});

const now = new Date();
const fullDate = new Intl.DateTimeFormat("en-US", {dateStyle: "full"}).format(now);
const copyYear = now.getFullYear();
const copyHolderName = document.querySelector("meta[name='author']").content;
console.log(copyHolderName);
