async function sendQuery() {
  const query = document.getElementById("query").value;
  console.log("Sending query:", query); // Debug log
  const response = await fetch("/query", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ query }),
  });
  const data = await response.json();
  console.log("Received response:", data); // Debug log
  document.getElementById("response").innerText = data.response;
}

async function sendOpen() {
  const item = document.getElementById("query").value;
  console.log("Sending open request for:", item); // Debug log
  const response = await fetch("/open", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ item }),
  });
  const data = await response.json();
  console.log("Received response:", data); // Debug log
  document.getElementById("response").innerText = data.response;
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("query").addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
      e.preventDefault(); // Prevent default form submission
      const query = document.getElementById("query").value.toLowerCase();
      if (query.startsWith("open ")) {
        sendOpen();
      } else {
        sendQuery();
      }
    }
  });
});
