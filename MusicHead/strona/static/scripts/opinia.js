const gwiazdki = document.querySelectorAll(".gwiazdka");
const gwiazdkiInput = document.getElementById("ocena");

gwiazdki.forEach(gwiazdka => {
    gwiazdka.addEventListener("click", () => {
        const ilosc = gwiazdka.getAttribute("ilosc");
        gwiazdkiInput.value = ilosc;

        gwiazdki.forEach(element => element.src = pustaGwiazdka);
        for (let i = 0; i < ilosc; i++) {
            gwiazdki[i].src = pelnaGwiazdka;
        }
    });
});


const dodajOpinie = document.getElementById('dodajOpinie');
const usun = document.getElementById('przyciskUsun');

if(dodajOpinie) dodajOpinie.addEventListener('submit', (event) => {
    if (gwiazdkiInput.value == 0) {
        event.preventDefault();
        document.getElementById("error").style.display = 'block';
    }
});

if (usun) usun.addEventListener('click', () => {
    if (confirm("Czy na pewno chcesz usunąć swoją opinię?")) {
        document.getElementById("inputUsun").value = 1;
        document.getElementById('formularzUsuwania').submit();
    }
});