const lightToggle = document.getElementById('checkboxInput')
const ligths = document.getElementById("content")
const elements = document.getElementsByClassName("bgs");
lightToggle.addEventListener('change', () => {
    if(lightToggle.checked){
        ligths.style.color = "white";


        for (var i = 0; i < elements.length; i++) {
            elements[i].style.backgroundColor = "var(--bg)";
        }
    }
    else{
        ligths.style.color = "rgba(0, 0, 0, 0)";
        for (var i = 0; i < elements.length; i++) {
            elements[i].style.backgroundColor = "rgba(0, 0, 0, 0)";
        }
    }
})
