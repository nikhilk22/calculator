async function calculate() {
    const a = document.getElementById('num1').value;
    const b = document.getElementById('num2').value;
    const op = document.getElementById('operation').value;

    if(a === "" || b === "") {
        alert("Please enter both numbers!");
        return;
    }

    const response = await fetch(`/${op}?a=${a}&b=${b}`);
    const data = await response.json();

    if(data.error) {
        document.getElementById('result').innerText = "Error: " + data.error;
    } else {
        document.getElementById('result').innerText = "Result: " + data.result;
    }
}
