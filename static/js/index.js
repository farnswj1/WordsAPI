const search = document.getElementById("search");

search.addEventListener("input", function(event) {
    if (search.validity.patternMismatch) {
        search.setCustomValidity("Please insert only letters with no spaces!");
    } else {
        search.setCustomValidity("");
    }
});