const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

document.querySelector("#sign-in-form").addEventListener("submit", (event) => {
  event.preventDefault();
  
  const username = document.querySelector("#sign-in-form input[type='text']").value;
  const password = document.querySelector("#sign-in-form input[type='password']").value;
  
  // Fetch the users' data from the JSON file
  fetch('users.json')
    .then(response => response.json())
    .then(users => {
      const user = users.find(user => user.username === username && user.password === password);
      
      if (user) {
        // User is registered, redirect to the homepage
        window.location.href = "../homepage/homepage.html";
      } else {
        // User is not registered, show an error message
        alert("Invalid username or password");
      }
    })
    .catch(error => {
      console.error('Error fetching user data:', error);
      alert("An error occurred while processing your request. Please try again later.");
    });
});
