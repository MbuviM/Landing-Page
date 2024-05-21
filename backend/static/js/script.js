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

document.getElementById('therapist-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = new FormData();
    formData.append('first_name', document.getElementById('first_name').value);
    formData.append('last_name', document.getElementById('last_name').value);
    formData.append('email', document.getElementById('email').value);
    formData.append('phone', document.getElementById('phone').value);
    formData.append('address', document.getElementById('address').value);
    formData.append('location', document.getElementById('location').value);
    formData.append('gender', document.getElementById('gender').value);
    formData.append('age', document.getElementById('age').value);
    formData.append('type_of_therapy', document.getElementById('type_of_therapy').value);
    formData.append('years_of_experience', document.getElementById('years_of_experience').value);
    formData.append('image', document.getElementById('image').files[0]);
    formData.append('fee_per_session', document.getElementById('fee_per_session').value);
    formData.append('monthly_slots', document.getElementById('monthly_slots').value);
    formData.append('monthly_fee', document.getElementById('monthly_fee').value);
    formData.append('accepts_queer_clients', document.getElementById('accepts_queer_clients').checked);

    fetch('http://127.0.0.1:8000/therapists/user/create/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.id) {
            alert('Therapist registered successfully!');
        } else {
            alert('Error: ' + JSON.stringify(data));
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    });
});

document.getElementById('search-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const location = document.getElementById('location').value;
    const therapyType = document.getElementById('therapy-type').value;

    fetch(`http://127.0.0.1:8000/therapists/search/?location=${location}&type_of_therapy=${therapyType}`, {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';

        if (data.length > 0) {
            data.forEach(therapist => {
                const therapistDiv = document.createElement('div');
                therapistDiv.innerHTML = `
                    <h3>${therapist.first_name} ${therapist.last_name}</h3>
                    <p>Location: ${therapist.location}</p>
                    <p>Specialization: ${therapist.type_of_therapy}</p>
                    <p>Years of Experience: ${therapist.years_of_experience}</p>
                `;
                resultsDiv.appendChild(therapistDiv);
            });
        } else {
            resultsDiv.innerHTML = '<p>No therapists found matching your criteria.</p>';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    });
});