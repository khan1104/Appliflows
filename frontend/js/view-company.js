async function loadCompanies() {
    try {
        const res = await fetch("http://localhost:8000/api/companies");
        const data = await res.json();

        window.allCompanies = data;
        displayCompanies(data);
    } catch (error) {
        console.error("Failed to load companies:", error);
    }
}

function displayCompanies(companies) {
    const tableBody = document.getElementById("company-table");
    tableBody.innerHTML = "";

    companies.forEach(company => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${company.name || "-"}</td>
            <td>${company.website || "-"}</td>
            <td>${company.funding_stage || "-"}</td>
            <td>${new Date(company.created_at).toLocaleDateString()}</td>
        `;

        tableBody.appendChild(row);
    });
}



// Load data on page load
document.addEventListener("DOMContentLoaded", loadCompanies);

