-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS flight_anomaly;

-- Create the user (or update password if exists)
CREATE USER IF NOT EXISTS 'flightuser'@'localhost' IDENTIFIED BY 'flightpass';
ALTER USER 'flightuser'@'localhost' IDENTIFIED BY 'flightpass';

-- Grant permissions
GRANT ALL PRIVILEGES ON flight_anomaly.* TO 'flightuser'@'localhost';
FLUSH PRIVILEGES;

-- Verify
SELECT User, Host FROM mysql.user WHERE User = 'flightuser';
