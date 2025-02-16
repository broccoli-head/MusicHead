const gwiazdki = document.querySelectorAll(".gwiazdka");
const gwiazdkiInput = document.getElementById("ocena");

gwiazdki.forEach(gwiazdka => {
    gwiazdka.addEventListener("click", function () {
        const ilosc = this.getAttribute("ilosc");
        gwiazdkiInput.value = ilosc;

        gwiazdki.forEach(element => element.src = pustaGwiazdka);
        for (let i = 0; i < ilosc; i++) {
            gwiazdki[i].src = pelnaGwiazdka;
        }
    });
});


const form = document.getElementById('dodajOpinie');

form.addEventListener('submit', function(event) {
    if (gwiazdkiInput.value == 0) {
        event.preventDefault();
        document.getElementById("error").style.display = 'block';
    }
});