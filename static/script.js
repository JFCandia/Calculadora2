document.querySelector("form").addEventListener("submit", function(event) {
    let num1 = document.querySelector("input[name='num1']").value;
    let num2 = document.querySelector("input[name='num2']").value;

    if (!num1 || !num2) {
        alert("Por favor, ingresa ambos números.");
        event.preventDefault();
    }
    function toggleTheme() {
        document.body.classList.toggle("dark-mode");
    }
    
    
});
