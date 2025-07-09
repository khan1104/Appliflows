// LOGIN HANDLER
document.getElementById('loginForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const res = await fetch('http://localhost:8000/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        if (res.ok) {
            const data = await res.json();
            alert(data.message);
            localStorage.setItem('auth', 'true'); // set auth flag
            window.location.href = 'dashboard.html';
        } else {
            const error = await res.json();
            alert("Login failed: " + (error.detail || 'Unknown error'));
        }
    } catch (err) {
        console.error("Error:", err);
        alert("Could not connect to server.");
    }
});

// LOGOUT FUNCTION
function logout() {
    localStorage.removeItem('auth');
    window.location.href = 'index.html';
}

