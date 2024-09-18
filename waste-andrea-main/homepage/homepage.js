document.getElementById('about-link').addEventListener('click', function(event) {
    event.preventDefault();
    window.location.href = '../about/about.html';
});

document.addEventListener('DOMContentLoaded', function () {
    // Handle navigation highlighting
    const currentLocation = window.location.href;
    const navLinks = document.querySelectorAll('nav ul li a');

    navLinks.forEach(link => {
        if (link.href === currentLocation) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
});
