/**
 * HylianModding Showcase — v1.0.1
 * Main JavaScript
 */

(function () {
  'use strict';

  // === Mobile Menu ===
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const navLinks = document.getElementById('navLinks');

  if (mobileMenuBtn && navLinks) {
    mobileMenuBtn.addEventListener('click', function () {
      navLinks.classList.toggle('active');
      this.textContent = navLinks.classList.contains('active') ? '✕' : '☰';
    });

    // Close menu when clicking a link
    navLinks.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        navLinks.classList.remove('active');
        mobileMenuBtn.textContent = '☰';
      });
    });
  }

  // === Navbar Scroll Effect ===
  const navbar = document.getElementById('navbar');

  function handleScroll() {
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', handleScroll, { passive: true });

  // === Theme Toggle ===
  const themeToggle = document.getElementById('themeToggle');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');

  // Load saved theme or default to dark
  var savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      var current = document.documentElement.getAttribute('data-theme');
      var next = current === 'light' ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      updateThemeIcon(next);
    });
  }

  function updateThemeIcon(theme) {
    if (themeToggle) {
      themeToggle.textContent = theme === 'light' ? '🌙' : '☀️';
    }
  }

  // === Typewriter Effect ===
  var typewriter = document.getElementById('typewriter');
  var phrases = [
    'Building retro game mods with AI-powered tooling.',
    'N64 ROM hacking. Open toolchains. Community driven.',
    'Where classic gaming meets modern AI.',
  ];
  var phraseIndex = 0;
  var charIndex = 0;
  var isDeleting = false;
  var typeSpeed = 60;
  var deleteSpeed = 30;
  var pauseDelay = 2000;

  function type() {
    if (!typewriter) return;

    var currentPhrase = phrases[phraseIndex];

    if (isDeleting) {
      charIndex--;
      typeSpeed = deleteSpeed;
    } else {
      charIndex++;
      typeSpeed = 60;
    }

    typewriter.textContent = currentPhrase.substring(0, charIndex);

    if (!isDeleting && charIndex === currentPhrase.length) {
      isDeleting = true;
      typeSpeed = pauseDelay;
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      phraseIndex = (phraseIndex + 1) % phrases.length;
      typeSpeed = 300;
    }

    setTimeout(type, typeSpeed);
  }

  // Start typewriter after a short delay
  setTimeout(type, 1000);

  // === Smooth Scroll for Anchor Links ===
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var targetId = this.getAttribute('href');
      if (targetId === '#') return;

      var target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        var offset = 80;
        var targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  // === Intersection Observer for Animations ===
  var observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Observe project cards and about cards
  document.querySelectorAll('.project-card, .about-card, .step-card, .contribute-card').forEach(function (card) {
    observer.observe(card);
  });

  // === Stats Counter Animation ===
  function animateCounter(element, target) {
    var duration = 2000;
    var start = 0;
    var startTime = null;

    function animation(currentTime) {
      if (!startTime) startTime = currentTime;
      var elapsed = currentTime - startTime;
      var progress = Math.min(elapsed / duration, 1);

      // Ease out
      var eased = 1 - Math.pow(1 - progress, 3);
      var current = Math.floor(eased * target);

      element.textContent = current + (target >= 100 ? '+' : '');

      if (progress < 1) {
        requestAnimationFrame(animation);
      } else {
        element.textContent = target + (target >= 100 ? '+' : '');
      }
    }

    requestAnimationFrame(animation);
  }

  // Animate stats when hero section is visible
  var heroSection = document.getElementById('hero');
  if (heroSection) {
    var statsObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          document.querySelectorAll('.stat-number').forEach(function (stat) {
            var text = stat.textContent;
            var num = parseInt(text.replace(/\D/g, ''), 10);
            if (!isNaN(num) && num > 0) {
              stat.textContent = '0' + (text.includes('+') ? '+' : '');
              animateCounter(stat, num);
            }
          });
          statsObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });

    statsObserver.observe(heroSection);
  }

  // === Keyboard Navigation ===
  document.addEventListener('keydown', function (e) {
    // ESC closes mobile menu
    if (e.key === 'Escape' && navLinks && navLinks.classList.contains('active')) {
      navLinks.classList.remove('active');
      if (mobileMenuBtn) mobileMenuBtn.textContent = '☰';
    }
  });

  console.log('%c🎮 HylianModding v1.0.1', 'color: #58a6ff; font-size: 16px; font-weight: bold;');
  console.log('%cAutonomous Game Studio — Open Source N64 ROM Hacking', 'color: #8b949e; font-size: 12px;');

})();
