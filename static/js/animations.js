// ========================================
// SCROLL ANIMATIONS & INTERACTIONS
// ========================================

document.addEventListener('DOMContentLoaded', function() {

    // ========================================
    // INTERSECTION OBSERVER FOR SCROLL ANIMATIONS
    // ========================================

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    // Animate elements on scroll
    const animateOnScroll = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
                entry.target.style.opacity = '1';
            }
        });
    }, observerOptions);

    // Select elements to animate
    const elementsToAnimate = document.querySelectorAll('.card, .display-5, .lead, h2, h3, .btn-lg');
    elementsToAnimate.forEach(el => {
        el.style.opacity = '0';
        animateOnScroll.observe(el);
    });

    // ========================================
    // STAGGER ANIMATIONS FOR PRODUCT CARDS
    // ========================================

    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';

        setTimeout(() => {
            card.style.transition = 'all 0.6s ease-out';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 150); // Stagger by 150ms
    });

    // ========================================
    // FEATURE CARDS ANIMATION
    // ========================================

    const featureCards = document.querySelectorAll('.col-md-6.col-lg-3 .card, .col-md-4 .card');
    featureCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'scale(0.8)';

        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.style.transition = 'all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'scale(1)';
                    }, index * 100);
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        observer.observe(card);
    });

    // ========================================
    // TESTIMONIAL CARDS SLIDE IN
    // ========================================

    const testimonials = document.querySelectorAll('.testimonial-card');
    testimonials.forEach((testimonial, index) => {
        testimonial.style.opacity = '0';
        testimonial.style.transform = 'translateX(-50px)';

        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.style.transition = 'all 0.6s ease-out';
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateX(0)';
                    }, index * 120);
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        observer.observe(testimonial);
    });

    // ========================================
    // HERO SECTION ANIMATION
    // ========================================

    const heroElements = {
        heading: document.querySelector('.hero-section h1'),
        paragraph: document.querySelector('.hero-section p.lead'),
        buttons: document.querySelector('.hero-section .d-flex'),
        image: document.querySelector('.hero-section img')
    };

    if (heroElements.heading) {
        heroElements.heading.style.opacity = '0';
        heroElements.heading.style.transform = 'translateY(-30px)';
        setTimeout(() => {
            heroElements.heading.style.transition = 'all 0.8s ease-out';
            heroElements.heading.style.opacity = '1';
            heroElements.heading.style.transform = 'translateY(0)';
        }, 200);
    }

    if (heroElements.paragraph) {
        heroElements.paragraph.style.opacity = '0';
        heroElements.paragraph.style.transform = 'translateY(-20px)';
        setTimeout(() => {
            heroElements.paragraph.style.transition = 'all 0.8s ease-out';
            heroElements.paragraph.style.opacity = '1';
            heroElements.paragraph.style.transform = 'translateY(0)';
        }, 400);
    }

    if (heroElements.buttons) {
        heroElements.buttons.style.opacity = '0';
        heroElements.buttons.style.transform = 'translateY(-10px)';
        setTimeout(() => {
            heroElements.buttons.style.transition = 'all 0.8s ease-out';
            heroElements.buttons.style.opacity = '1';
            heroElements.buttons.style.transform = 'translateY(0)';
        }, 600);
    }

    if (heroElements.image) {
        heroElements.image.style.opacity = '0';
        heroElements.image.style.transform = 'scale(0.8) rotate(-5deg)';
        setTimeout(() => {
            heroElements.image.style.transition = 'all 1s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
            heroElements.image.style.opacity = '1';
            heroElements.image.style.transform = 'scale(1) rotate(0)';
        }, 800);
    }

    // ========================================
    // COUNTER ANIMATION FOR NUMBERS
    // ========================================

    function animateCounter(element, target, duration = 2000) {
        let start = 0;
        const increment = target / (duration / 16);
        const timer = setInterval(() => {
            start += increment;
            if (start >= target) {
                element.textContent = target;
                clearInterval(timer);
            } else {
                element.textContent = Math.floor(start);
            }
        }, 16);
    }

    // ========================================
    // PARALLAX EFFECT ON SCROLL
    // ========================================

    let ticking = false;
    window.addEventListener('scroll', function() {
        if (!ticking) {
            window.requestAnimationFrame(function() {
                const scrolled = window.pageYOffset;

                // Parallax for hero section
                const hero = document.querySelector('.hero-section');
                if (hero) {
                    hero.style.transform = `translateY(${scrolled * 0.5}px)`;
                }

                // Parallax for product images
                const productImages = document.querySelectorAll('.product-card .card-img-top');
                productImages.forEach(img => {
                    const rect = img.getBoundingClientRect();
                    if (rect.top < window.innerHeight && rect.bottom > 0) {
                        const offset = (window.innerHeight - rect.top) * 0.1;
                        img.style.transform = `translateY(${offset}px)`;
                    }
                });

                ticking = false;
            });
            ticking = true;
        }
    });

    // ========================================
    // BUTTON RIPPLE EFFECT
    // ========================================

    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;

            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple-effect');

            this.appendChild(ripple);

            setTimeout(() => ripple.remove(), 600);
        });
    });

    // Add ripple styles
    const style = document.createElement('style');
    style.textContent = `
        .btn {
            position: relative;
            overflow: hidden;
        }
        .ripple-effect {
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.6);
            transform: scale(0);
            animation: ripple-animation 0.6s ease-out;
        }
        @keyframes ripple-animation {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);

    // ========================================
    // ICON ANIMATION ON HOVER
    // ========================================

    document.querySelectorAll('.feature-icon, .benefit-icon').forEach(icon => {
        icon.addEventListener('mouseenter', function() {
            this.style.animation = 'bounceIn 0.6s ease-out';
        });

        icon.addEventListener('animationend', function() {
            this.style.animation = '';
        });
    });

    // ========================================
    // BADGE PULSE ANIMATION
    // ========================================

    const badges = document.querySelectorAll('.badge.bg-danger');
    badges.forEach(badge => {
        setInterval(() => {
            badge.style.animation = 'pulse 0.5s ease-in-out';
            setTimeout(() => {
                badge.style.animation = '';
            }, 500);
        }, 3000);
    });

    // ========================================
    // SMOOTH SCROLL TO TOP BUTTON
    // ========================================

    const scrollButton = document.createElement('button');
    scrollButton.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollButton.className = 'scroll-to-top';
    scrollButton.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: var(--primary-color);
        color: white;
        border: none;
        cursor: pointer;
        opacity: 0;
        transition: all 0.3s ease;
        z-index: 1000;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    `;
    document.body.appendChild(scrollButton);

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            scrollButton.style.opacity = '1';
            scrollButton.style.transform = 'scale(1)';
        } else {
            scrollButton.style.opacity = '0';
            scrollButton.style.transform = 'scale(0.5)';
        }
    });

    scrollButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    scrollButton.addEventListener('mouseenter', function() {
        this.style.transform = 'scale(1.1)';
        this.style.background = 'var(--secondary-color)';
    });

    scrollButton.addEventListener('mouseleave', function() {
        this.style.transform = 'scale(1)';
        this.style.background = 'var(--primary-color)';
    });

    // ========================================
    // PRICE ANIMATION
    // ========================================

    const prices = document.querySelectorAll('.h4.text-primary, .h2.text-primary');
    prices.forEach(price => {
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.animation = 'scaleIn 0.6s ease-out';
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);
        observer.observe(price);
    });

    // ========================================
    // IMAGE LAZY LOAD WITH FADE IN
    // ========================================

    const images = document.querySelectorAll('img');
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.style.opacity = '0';
                img.style.transition = 'opacity 0.6s ease-in';

                if (img.complete) {
                    img.style.opacity = '1';
                } else {
                    img.addEventListener('load', () => {
                        img.style.opacity = '1';
                    });
                }

                imageObserver.unobserve(img);
            }
        });
    }, observerOptions);

    images.forEach(img => imageObserver.observe(img));

    // ========================================
    // TYPING EFFECT FOR HERO HEADING (OPTIONAL)
    // ========================================

    function typeWriter(element, text, speed = 50) {
        let i = 0;
        element.textContent = '';
        element.style.opacity = '1';

        function type() {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }
        type();
    }

    // Console message for developers
    console.log('%c✨ Intelpod Website - Animated by AI! ', 'background: #004b27; color: #fff; padding: 10px; font-size: 14px; border-radius: 5px;');

});
