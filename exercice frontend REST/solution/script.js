async function askQuestion() {
    const question = document.getElementById("question").value;
    const responseElement = document.getElementById("answer");

    try {
        const response = await fetch('http://localhost:8080/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query: question })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        responseElement.textContent = data.answer;
    } catch (error) {
        responseElement.textContent = `Error: ${error.message}`;
    }
}