document.addEventListener('DOMContentLoaded', function() {
    // Handle "Find a Therapist" form submission
    const findTherapistForm = document.querySelector('#find-therapist form');
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

    // Handle "Therapist Registration" form submission
    const registrationForm = document.querySelector('#therapist-registration form');
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

    // Handle "Get Started" button click
    const getStartedButton = document.querySelector('.information button');
    getStartedButton.addEventListener('click', function() {
        // Redirect to the "Find a Therapist" section
        document.querySelector('#find-therapist').scrollIntoView({ behavior: 'smooth' });
    });

    // Handle other button interactions if needed
    const searchButton = document.querySelector('.search-button');
    searchButton.addEventListener('click', function() {
        alert('Searching...');
    });

    const registerButton = document.querySelector('.register-button');
    registerButton.addEventListener('click', function() {
        alert('Registering therapist...');
    });
});
