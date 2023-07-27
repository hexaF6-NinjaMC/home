const chapterInput = document.querySelector('#favchap');
const addButton = document.querySelector('button');
const listElem = document.querySelector('.list');

addButton.addEventListener('click', () => {
    if(chapterInput.value != '') {
        const valueChapter = chapterInput.value;
        chapterInput.value = '';

        const listItem = document.createElement('li');
        const spanContent = document.createElement('span');
        const delBtn = document.createElement('button');

        listItem.appendChild(spanContent);
        listItem.appendChild(delBtn);
        spanContent.textContent = valueChapter;
        delBtn.textContent = '❌';
        listElem.appendChild(listItem);

        delBtn.addEventListener('click', () => {
            listElem.removeChild(listItem);
        });

        chapterInput.focus();
    }
})