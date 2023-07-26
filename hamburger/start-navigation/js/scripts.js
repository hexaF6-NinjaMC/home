function toggleMenu() {
    let temp = document.getElementsByClassName('toggler')[0];
    temp.classList.toggle('hide');
    if (temp.classList[1] == 'hide') {
        document.querySelector('.toggler > a').innerHTML = "&#9776; Menu";
    } else {
        document.querySelector('.toggler > a').innerHTML = "&#10006; Close";
    }
}