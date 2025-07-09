// Fetch and display contacts
async function loadContacts() {
    try {
        const res = await fetch("http://localhost:8000/api/contacts");
        const data = await res.json();

        const tableBody = document.getElementById("contacts-table");
        tableBody.innerHTML = "";

        data.forEach(contact => {
            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${contact.domain || "-"}</td>
                <td>${contact.name || "-"}</td>
                <td>${contact.title || "-"}</td>
                <td>${contact.email || "-"}</td>
                <td><a href="${contact.linkedin}" target="_blank">${contact.linkedin ? "View Profile" : "-"}</a></td>
            `;

            tableBody.appendChild(row);
        });

        window.allContacts = data; // For search filtering
    } catch (error) {
        console.error("Failed to load contacts:", error);
    }
}

// Filter contacts by company name
function filterTable() {
    const query = document.getElementById("search").value.toLowerCase();
    const filtered = window.allContacts.filter(contact =>
        contact.domain && contact.domain.toLowerCase().includes(query)
    );

    const tableBody = document.getElementById("contacts-table");
    tableBody.innerHTML = "";

    filtered.forEach(contact => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${contact.domain || "-"}</td>
            <td>${contact.name || "-"}</td>
            <td>${contact.title || "-"}</td>
            <td>${contact.email || "-"}</td>
            <td><a href="${contact.linkedin}" target="_blank">${contact.linkedin ? "View Profile" : "-"}</a></td>
        `;

        tableBody.appendChild(row);
    });
}

// Load contacts on page load
document.addEventListener("DOMContentLoaded", loadContacts);
