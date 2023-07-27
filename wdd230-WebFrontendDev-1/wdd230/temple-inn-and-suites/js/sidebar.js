function openSidebar() {
    document.querySelector(".sidebar").style.width = "200px";
    document.querySelector("#content").style.marginLeft = "200px";
    document.querySelector(".toggler").setAttribute("onclick", "closeSidebar()");
    document.querySelector(".toggler span").innerHTML = "&#8920; &#10006;";
}

function closeSidebar() {
    document.querySelector(".sidebar").style.width = "0";
    document.querySelector("#content").style.marginLeft = "0";
    document.querySelector(".toggler").setAttribute("onclick", "openSidebar()");
    document.querySelector(".toggler span").innerHTML = "&#9776; &#8921;"
}