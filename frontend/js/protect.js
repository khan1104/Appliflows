(function () {
    const isLoggedIn = localStorage.getItem('auth');
    if (isLoggedIn !== 'true') {
        window.location.href = 'index.html'; // redirect if not logged in
    }
})();