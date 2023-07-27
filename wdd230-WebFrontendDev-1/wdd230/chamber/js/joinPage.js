/* Join.html hidden date script */
const dateHiddenObj = `Loaded by user (ISO format): ${now.toISOString()}`;
let hiddenDateElem = document.querySelector(".hiddenDate").firstChild;
hiddenDateElem.textContent = dateHiddenObj;
hiddenDateElem.parentElement.style.visibility = "hidden";