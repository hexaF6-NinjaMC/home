let likeBtnClass = localStorage;

function changeImg(numbered_btn) {
    let original_image = document.querySelector(`.likeImg-${numbered_btn}`);
    let source = original_image.getAttribute('src');
    if (source = 'images/assets/like.png') {
        let reSource = 'images/assets/like-colored.png';
        original_image.setAttribute('src', reSource);
        if (localStorage.getItem(likeBtnClass) != (original_image.className)) {
            localStorage.setItem(`likeImg-${numbered_btn}`, reSource);
            console.log(original_image);
        };
        return;
    } else {
        let reSource = 'images/assets/like.png';
        original_image.setAttribute('src', reSource);
        localStorage.setItem(`likeImg-${numbered_btn}`, reSource);
        return;
    }
}