var empty_card = null;

function setEmptyCard(index) {
    index  = index -1;
    if(index >= 0){
        empty_card = $('.card').eq(index);
        empty_card.attr('id', 'empty_card');
    }
}


function shuffleArray(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    return array;
}

