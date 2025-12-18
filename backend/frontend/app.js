async function askQuestion() {
    const input = document.getElementById("question");
    const chatBox = document.getElementById("chat-box");
    const question = input.value.trim();

    if (!question) return;

    // Show user message
    chatBox.innerHTML += `
        <div class="message user"><strong>You:</strong> ${question}</div>
    `;
    input.value = "";

    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        const data = await response.json();

        chatBox.innerHTML += `
            <div class="message bot">
                <strong>Assistant:</strong><br/>
                ${data.answer.replace(/\n/g, "<br/>")}
                <div class="sources">
                    <strong>Sources:</strong> ${data.sources.join(", ")}
                </div>
            </div>
        `;
    } catch (err) {
        chatBox.innerHTML += `
            <div class="message bot" style="color:red;">
                Error fetching response.
            </div>
        `;
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}
