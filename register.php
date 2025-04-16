<?php
// Database configuration
$host = "localhost";
$dbusername = "root";
$dbpassword = "";
$dbname = "railway";

// Create connection
$conn = new mysqli($host, $dbusername, $dbpassword, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Process form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize inputs
    $first_name = filter_var($_POST['first_name'], FILTER_SANITIZE_STRING);
    $last_name = filter_var($_POST['last_name'], FILTER_SANITIZE_STRING);
    $phone = filter_var($_POST['phone'], FILTER_SANITIZE_STRING);
    $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);

    // Validate inputs
    $errors = [];
    
    if (empty($first_name)) $errors[] = "First name is required";
    if (empty($last_name)) $errors[] = "Last name is required";
    if (empty($phone)) $errors[] = "Phone number is required";
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) $errors[] = "Invalid email format";
    if (strlen($_POST['password']) < 8) $errors[] = "Password must be at least 8 characters";

    // If no validation errors
    if (empty($errors)) {
        // Check if email exists
        $stmt = $conn->prepare("SELECT email FROM register1 WHERE email = ?");
        $stmt->bind_param("s", $email);
        $stmt->execute();
        $stmt->store_result();
        
        if ($stmt->num_rows > 0) {
            echo "Email already registered!";
        } else {
            // Insert new user
            $insert_stmt = $conn->prepare("INSERT INTO register1 (first_name, last_name, phone, email, password) VALUES (?, ?, ?, ?, ?)");
            $insert_stmt->bind_param("sssss", $first_name, $last_name, $phone, $email, $password);
            
            if ($insert_stmt->execute()) {
                echo "Registration successful!";
            } else {
                echo "Error: " . $insert_stmt->error;
            }
            $insert_stmt->close();
        }
        $stmt->close();
    } else {
        foreach ($errors as $error) {
            echo $error . "<br>";
        }
    }
    $conn->close();
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Registration Form</title>
</head>
<body>
    <h2>Register</h2>
    <form method="POST" action="">
        <input type="text" name="first_name" placeholder="First Name" required><br>
        <input type="text" name="last_name" placeholder="Last Name" required><br>
        <input type="tel" name="phone" placeholder="Phone Number" required><br>
        <input type="email" name="email" placeholder="Email" required><br>
        <input type="password" name="password" placeholder="Password (min 8 characters)" required><br>
        <button type="submit">Register</button>
    </form>
</body>
</html>