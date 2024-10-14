const sideMenu = document.querySelector('aside');
const menuBtn = document.querySelector('#menu_bar');
const closeBtn = document.querySelector('#close_btn');
const themeToggler = document.querySelector('.theme-toggler');

// Show side menu
menuBtn.addEventListener('click', () => {
    sideMenu.style.display = "block";
});

// Hide side menu
closeBtn.addEventListener('click', () => {
    sideMenu.style.display = "none";
});

// Toggle theme
themeToggler.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme-variables');
    themeToggler.querySelector('span:nth-child(1)').classList.toggle('active');
    themeToggler.querySelector('span:nth-child(2)').classList.toggle('active');
});

// Fetch data from the backend
const fetchData = async () => {
    try {
        const response = await fetch('https://your-api-endpoint.com/data'); // Replace with your API endpoint
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        // Call a function to update the UI with the fetched data
        updateUI(data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
};

// Function to update the UI with fetched data
const updateUI = (data) => {
    // For example, you can populate elements on your dashboard with the data
    const salesElement = document.querySelector('.sales h1');
    const expensesElement = document.querySelector('.expenses h1');
    const incomeElement = document.querySelector('.income h1');

    salesElement.textContent = `$${data.sales}`;
    expensesElement.textContent = `$${data.expenses}`;
    incomeElement.textContent = `$${data.income}`;
};

// Call fetchData when the page loads
document.addEventListener('DOMContentLoaded', () => {
    fetchData();
});
setInterval(fetchData, 5000); 