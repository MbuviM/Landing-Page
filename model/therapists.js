const mysql = require('mysql');

// Create a MySQL connection pool
const pool = mysql.createPool({
    host: 'localhost',
    user: 'root',
    password: 'Mwende#2001!',
    database: 'THERAPISTS',
    waitForConnections: true,
    connectionLimit: 10,
    queueLimit: 0
});

// Check if the connection pool was created successfully
pool.query('SELECT * FROM therapists', (error, results, field) => {
    if (error) {
        return console.error('Error connecting to the database: ' + error.stack);
    }
    else {
        return console.log('Database connected successfully.');
    }
});

// Export the connection pool
module.exports = pool;
