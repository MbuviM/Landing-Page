// Open sidebar
function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
}

// Close sidebar
function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
}

document.addEventListener('DOMContentLoaded', function() {
    // Handle "Get Started" button click
    const getStartedButton = document.querySelector('.information button');
    if (getStartedButton) {
        getStartedButton.addEventListener('click', function() {
            // Redirect to the "Find a Therapist" page
            window.location.href = "{% url 'find_a_therapist' %}";
        });
    } else {
        console.error('Get Started button not found');
    }
});