// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Auto-dismiss alerts after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
});

// Add to cart animation
document.querySelectorAll('form[action*="cart/add"]').forEach(form => {
    form.addEventListener('submit', function(e) {
        const button = this.querySelector('button[type="submit"]');
        if (button) {
            button.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Adding...';
            button.disabled = true;
        }
    });
});

// Form validation feedback
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
        if (!form.checkValidity()) {
            e.preventDefault();
            e.stopPropagation();
        }
        form.classList.add('was-validated');
    });
});

// Quantity input validation
document.querySelectorAll('input[type="number"]').forEach(input => {
    input.addEventListener('change', function() {
        const min = parseInt(this.getAttribute('min')) || 1;
        const max = parseInt(this.getAttribute('max')) || Infinity;
        let value = parseInt(this.value);

        if (isNaN(value) || value < min) {
            this.value = min;
        } else if (value > max) {
            this.value = max;
        }
    });
});

// Image lazy loading
if ('loading' in HTMLImageElement.prototype) {
    const images = document.querySelectorAll('img[loading="lazy"]');
    images.forEach(img => {
        img.src = img.dataset.src;
    });
} else {
    // Fallback for browsers that don't support lazy loading
    const script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.3.2/lazysizes.min.js';
    document.body.appendChild(script);
}

// Shopping cart counter update animation
function updateCartCounter(count) {
    const cartBadge = document.querySelector('.navbar .badge');
    if (cartBadge) {
        cartBadge.textContent = count;
        cartBadge.classList.add('animate-fade-in');
        setTimeout(() => {
            cartBadge.classList.remove('animate-fade-in');
        }, 600);
    }
}

// Navbar scroll effect
let lastScroll = 0;
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    const currentScroll = window.pageYOffset;

    if (currentScroll > 100) {
        navbar.style.boxShadow = '0 4px 6px rgba(0,0,0,0.1)';
    } else {
        navbar.style.boxShadow = '0 2px 4px rgba(0,0,0,0.1)';
    }

    lastScroll = currentScroll;
});

// Product image gallery
document.querySelectorAll('.product-image-section .row img').forEach(img => {
    img.addEventListener('click', function() {
        const mainImage = document.querySelector('.product-image-section > img');
        if (mainImage) {
            const temp = mainImage.src;
            mainImage.src = this.src;
            this.src = temp;
        }
    });
});

// Initialize tooltips
const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
});

// Initialize popovers
const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
const popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl);
});

// Contact form submission
const contactForm = document.querySelector('form[action*="contact"]');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        const submitBtn = this.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Sending...';
            submitBtn.disabled = true;
        }
    });
}

// Checkout form validation
const checkoutForm = document.querySelector('form[action*="checkout"]');
if (checkoutForm) {
    checkoutForm.addEventListener('submit', function(e) {
        const submitBtn = this.querySelector('button[type="submit"]');
        if (submitBtn && this.checkValidity()) {
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Processing...';
            submitBtn.disabled = true;
        }
    });
}

console.log('Intelpod website loaded successfully!');
