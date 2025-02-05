function sprawdzLink(url) {
    const regex = /^https:\/\/www\.youtube\.com\/watch\?v=[\w-]+$/;
    return regex.test(url);
}


const form = document.getElementById('formularz');
const urlInput = document.getElementById('urlInput');
const wiadomosc = document.getElementById('urlError');

form.addEventListener('submit', function(event) {
    const link = urlInput.value;

    if (!sprawdzLink(link) && link != "") {
        event.preventDefault();
        wiadomosc.style.display = 'block';
    }
});


document.getElementById("polePlik").addEventListener("change", function(event) {
    const plik = event.target.files[0];
    if (plik) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const zdjecie = document.getElementById("podgladZdjecia");
            zdjecie.src = e.target.result;
            zdjecie.style.display = "block";
        };
        reader.readAsDataURL(plik);
    }
});