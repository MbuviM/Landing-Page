document.addEventListener('DOMContentLoaded', function() {
    // Get all navigation links and pages
    const navLinks = document.querySelectorAll('.header-links a');
    const pages = document.querySelectorAll('.page');

    // Function to show a page
    function showPage(hash) {
        // Hide all pages
        pages.forEach(page => page.classList.remove('active'));
        // Show the page that matches the hash
        const targetPage = document.querySelector(hash);
        if (targetPage) {
            targetPage.classList.add('active');
        }
    }

    // Set up event listeners for navigation links
    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const target = this.getAttribute('href');
            showPage(target);
        });
    });

    // Show the home page by default
    showPage('#home');
});
