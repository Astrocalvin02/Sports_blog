// Main JavaScript for Sports Blog

document.addEventListener("DOMContentLoaded", function () {
  // Like post functionality
  const likeButtons = document.querySelectorAll(".like-btn");

  likeButtons.forEach((button) => {
    button.addEventListener("click", function (e) {
      e.preventDefault();
      const url = this.getAttribute("data-url");

      fetch(url, {
        method: "POST",
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": getCookie("csrftoken"),
        },
      })
        .then((response) => response.json())
        .then((data) => {
          // Update like count
          const countElement = this.querySelector(".like-count");
          countElement.textContent = data.count;

          // Toggle like icon
          const iconElement = this.querySelector("i");
          if (data.liked) {
            iconElement.classList.remove("not-liked");
            iconElement.classList.add("liked");
          } else {
            iconElement.classList.remove("liked");
            iconElement.classList.add("not-liked");
          }
        })
        .catch((error) => console.error("Error:", error));
    });
  });

  // Function to get CSRF token from cookies
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  // Bootstrap initialization for tooltips and popovers
  const tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });
});
