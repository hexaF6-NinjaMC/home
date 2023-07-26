async function dataReturn(dataFile) {
    dataFile.forEach(dataReturn);
}

const jsonFile = "./json/data.json";
fetch(jsonFile).then(function (response) {return response.json();}).then(function (jsonObject) {
    const businesses = jsonObject["businesses"];
    businesses.forEach(displayCards);
});

function displayCards(card) {
    // Create the elements of each card:
    let busiCard = document.createElement("section");
    let busiName = document.createElement("h3");
    let busiLoc = document.createElement("p");
    let busiLogo = document.createElement("img");

    busiName.textContent = `${card.name}`;
    busiLoc.textContent = `${card.address}`;
    busiLogo.setAttribute("src", `${card.brandImage}`);
    busiLogo.style = ("width: 150px");
    busiLogo.style.backgroundColor = "#E6DECA";

    busiCard.appendChild(busiLogo);
    busiCard.appendChild(busiName);
    busiCard.appendChild(busiLoc);
    busiCard.style.backgroundColor = "#FEEBA6";

    document.querySelector(".businessCards").appendChild(busiCard);
}

function gridView() {
    document.querySelector(".businessCards").classList.add("grid");
    document.querySelector(".businessCards").classList.remove("list");
}

function listView() {
    document.querySelector(".businessCards").classList.add("list");
    document.querySelector(".businessCards").classList.remove("grid");
}