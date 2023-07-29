const postListEl = document.querySelector("#repo-link-list");
const copyYearEl = document.querySelector("#copy-year");
const copyHolderEl = document.querySelector("#copy-holder");
const spinningElWrapper = document.querySelector("#animation-wrapper");
const shadesEl = document.querySelector("#shades");
const shadeLeftEl = document.querySelector("#shade-left");
const shadeRightEl = document.querySelector("#shade-right");
const timeoutVal = 3000;

setTimeout(
	function loaded() {
		spinningElWrapper.style = `
			transition: all 0.3s ease-out;
			transform: translateY(-100%);
			opacity: 0;
		`;
		shadeLeftEl.style = `
			transform: translateX(-100%);
			transition: all 0.7s 0.3s ease-out;
			opacity: 0;
		`;
		shadeRightEl.style = `
			transform: translateX(+100%);
			transition: all 0.7s 0.3s ease-out;
			opacity: 0;
		`;
		shadesEl.style = `
			visibility: hidden;
		`;
	},
	timeoutVal);

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
		text: "Showcasing the temples of the Church of Jesus Christ of Latter-Day Saints, while enjoying a stay at the Temple Inn & Suites",
		url: "./wdd230/temple-inn-and-suites/"
	},
	{
		text: "A DOM-manipulation example, allowing you to present your favorite chapter from the Book of Mormon",
		url: "./wdd230/dom-practice/bom.html"
	},
	{
		text: "An Animated Representation of Our Solar System, in Only CSS3 and HTML!",
		url: "./our-site/html/solar-system.html"
	},
	{
		text: "Our Blogging Site (currently in development!!!)",
		url: "./our-site/html/"
	},
	{
		text: "An Example of Utlizing the Position properties in CSS",
		url: "./our-site/html/html-testing-file.html"
	}
];

anchors.forEach((anchor) => {
	const liElTemplate = `<li><a href="${anchor.url}" target="_blank">${anchor.text}</a></li>`;
	postListEl.insertAdjacentHTML("beforeend", liElTemplate);
});

const now = new Date();
const fullDate = new Intl.DateTimeFormat("en-US", { dateStyle: "full" }).format(now);
const copyYear = now.getFullYear();
const copyHolderName = document.querySelector("meta[name='author']").content;
// console.log(copyHolderName);
copyYearEl.textContent = copyYear;
copyHolderEl.textContent = copyHolderName;