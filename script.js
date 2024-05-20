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
            window.location.href = 'find-a-therapist.html';
        });
    } else {
        console.error('Get Started button not found');
    }

    // Handle "Find a Therapist" form submission
    const findTherapistForm = document.querySelector('#find-therapist form');
    if (findTherapistForm) {
        findTherapistForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent form from submitting the default way
            
            const location = document.getElementById('location').value;
            const therapyType = document.getElementById('therapy-type').value;
            
            console.log('Location:', location);
            console.log('Type of Therapy:', therapyType);
            
            // Display an alert with the input data (for demonstration)
            alert(`Searching for therapists in ${location} specializing in ${therapyType}`);
            
            // Reset the form fields after submission
            findTherapistForm.reset();
        });
    } else {
        console.error('Find Therapist form not found');
    }

    // Handle "Therapist Registration" form submission
    const registrationForm = document.querySelector('#therapist-registration form');
    if (registrationForm) {
        registrationForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent form from submitting the default way
            
            const name = document.getElementById('name').value;
            const location = document.querySelector('#therapist-registration #location').value;
            const specialization = document.getElementById('specialization').value;
            const contact = document.getElementById('contact').value;
            
            console.log('Name:', name);
            console.log('Location:', location);
            console.log('Specialization:', specialization);
            console.log('Contact:', contact);
            
            // Display an alert with the input data (for demonstration)
            alert(`Therapist Registered:\nName: ${name}\nLocation: ${location}\nSpecialization: ${specialization}\nContact: ${contact}`);
            
            // Reset the form fields after submission
            registrationForm.reset();
        });
    } else {
        console.error('Therapist Registration form not found');
    }

    // Handle other button interactions if needed
    const searchButton = document.querySelector('.search-button');
    if (searchButton) {
        searchButton.addEventListener('click', function() {
            alert('Searching...');
        });
    } else {
        console.error('Search button not found');
    }

    const registerButton = document.querySelector('.register-button');
    if (registerButton) {
        registerButton.addEventListener('click', function() {
            alert('Registering therapist...');
        });
    } else {
        console.error('Register button not found');
    }
});

// JavaScript function to fetch and display therapists
function fetchTherapists() {
    fetch('http://127.0.0.1:8000/therapists/user/')  // Sending GET request to fetch therapists
        .then(response => response.json())
        .then(data => {
            // Process and display therapist data here
        })
        .catch(error => {
            console.error('Error fetching therapists:', error);
        });
}

// JavaScript function to add a new therapist
function addTherapist(newTherapistData) {
    fetch('http://127.0.0.1:8000/therapists/user/create/', {
        method: 'POST',  // Sending POST request to add a therapist
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newTherapistData)
    })
    .then(response => response.json())
    .then(data => {
        // Process response data if needed
        console.log('New therapist added successfully:', data);
    })
    .catch(error => {
        console.error('Error adding therapist:', error);
    });
}
