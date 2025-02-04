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