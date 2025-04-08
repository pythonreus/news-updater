fetch("http://localhost:5000/")
  .then((response) => response.json())
  .then((data) => {
    // Get the main section where headlines will be added
     const main_section = document.getElementById("headlines");

    // Iterate through the data (assuming data.headlines is an array of news items)
    data.headlines.forEach((item) => {
      // Create a new element (for example, a div for each headline)
      const headlineElement = document.createElement("div");

      // You can add the title and summary to the div, or any other structure you need
      headlineElement.innerHTML = `
        <h2>${item.title}</h2>
        <p>${item.summary}</p>
        <span>${item.date}</span>
        <a href="${item.source}" target="_blank">Source: ${item.source}</a>
      `;

      // Append the created element to the main section
      main_section.appendChild(headlineElement);
    });
  })
  .catch((error) => {
    console.error("Error fetching data:", error);
  });
