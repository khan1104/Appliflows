document.getElementById("company-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const name = document.getElementById("name").value.trim();
    const website = document.getElementById("website").value.trim();
    const funding_stage = document.getElementById("funding_stage").value;

    const payload = {
        name,
        website,
        funding_stage
    };

    try {
        const res = await fetch("http://localhost:8000/api/companies", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const data = await res.json();
        const msgBox = document.getElementById("response-message");

        if (res.status === 201) {
            msgBox.textContent = "Company added successfully!";
            msgBox.style.color = "green";
            document.getElementById("company-form").reset();
        } 
        else if(res.status==409){
            msgBox.textContent = "Company alreday listed";
            msgBox.style.color = "red";
        }
        else {
            msgBox.textContent = "❌ " + (data.detail || "Failed to add company");
            msgBox.style.color = "red";
        }
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("response-message").textContent = "❌ Server error";
        document.getElementById("response-message").style.color = "red";
    }
});

