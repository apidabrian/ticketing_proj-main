// Dark/Light Mode Switch (Yin-Yang Icon)
const themeToggle = document.getElementById('theme-toggle');

// Check if the element exists to prevent errors on pages without the toggle
if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        const isDarkMode = document.body.classList.contains('dark-mode');
        localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
    });
}

// Apply saved theme on page load
window.addEventListener('load', () => {
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-mode');
    }
});

// Dynamic Navigation Bar (rawlab.co inspired)
const navBar = document.getElementById('main-nav');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navBar.classList.add('scrolled');
    } else {
        navBar.classList.remove('scrolled');
    }
});

// Hero Section Hover Effect
document.querySelectorAll('.hero-item').forEach(item => {
    item.addEventListener('mouseenter', () => {
        const preview = item.querySelector('.hero-preview');
        if (preview) {
            preview.style.display = 'block';
        }
    });

    item.addEventListener('mouseleave', () => {
        const preview = item.querySelector('.hero-preview');
        if (preview) {
            preview.style.display = 'none';
        }
    });
});


// JavaScript for horizontal scroll buttons (works for multiple sliders)
function scrollContainer(containerId, direction) {
    const container = document.getElementById(containerId);
    if (!container) return; // safety check

    const scrollAmount = 300; // pixels per click

    if (direction === 'left') {
        container.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    } else if (direction === 'right') {
        container.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    }
}


