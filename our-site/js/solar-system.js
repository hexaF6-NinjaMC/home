const postListEl = document.querySelector("#repo-link-list");
const copyYearEl = document.querySelector("#copy-year");
const copyHolderEl = document.querySelector("#copy-holder");

const now = new Date();
const fullDate = new Intl.DateTimeFormat("en-US", { dateStyle: "full" }).format(now);
const copyYear = now.getFullYear();
const copyHolderName = document.querySelector("meta[name='author']").content;
// console.log(copyHolderName);
copyYearEl.textContent = copyYear;
copyHolderEl.textContent = copyHolderName;