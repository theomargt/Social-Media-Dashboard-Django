// Wait for the DOM to fully load before executing
document.addEventListener("DOMContentLoaded", function () {
    
    console.log("JavaScript Loaded Successfully!"); // Debugging Check

    // Example: Toggle Dark Mode
    const toggleButton = document.getElementById("toggleDarkMode");
    if (toggleButton) {
        toggleButton.addEventListener("click", function () {
            document.body.classList.toggle("dark-mode");
        });
    }

    // Example: Show an alert when the post button is clicked
    const postButton = document.getElementById("postMessage");
    if (postButton) {
        postButton.addEventListener("click", function () {
            alert("Your post has been scheduled!");
        });
    }

    // Example: Animate Social Icons on Hover
    const socialIcons = document.querySelectorAll(".social-icons img");
    socialIcons.forEach(icon => {
        icon.addEventListener("mouseover", function () {
            this.style.transform = "scale(1.2)";
        });
        icon.addEventListener("mouseout", function () {
            this.style.transform = "scale(1)";
        });
    });

});
