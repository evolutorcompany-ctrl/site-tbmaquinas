/* ════════════════════════════════════════════════════
   TB Máquinas – main.js
   ════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', function () {

  /* ── HAMBURGER MENU ─────────────────────────────── */
  const hamburger = document.getElementById('hamburger');
  const mainNav   = document.getElementById('main-nav');

  if (hamburger && mainNav) {
    hamburger.addEventListener('click', function () {
      const isOpen = mainNav.classList.toggle('open');
      hamburger.setAttribute('aria-expanded', isOpen);
      hamburger.classList.toggle('active', isOpen);

      // Animate hamburger spans
      const spans = hamburger.querySelectorAll('span');
      if (isOpen) {
        spans[0].style.transform = 'translateY(7px) rotate(45deg)';
        spans[1].style.opacity   = '0';
        spans[2].style.transform = 'translateY(-7px) rotate(-45deg)';
      } else {
        spans[0].style.transform = '';
        spans[1].style.opacity   = '';
        spans[2].style.transform = '';
      }
    });

    // Close nav when clicking a link
    mainNav.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        mainNav.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
        hamburger.classList.remove('active');
        const spans = hamburger.querySelectorAll('span');
        spans.forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
      });
    });

    // Close on outside click
    document.addEventListener('click', function (e) {
      if (!hamburger.contains(e.target) && !mainNav.contains(e.target)) {
        mainNav.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
        hamburger.classList.remove('active');
        const spans = hamburger.querySelectorAll('span');
        spans.forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
      }
    });
  }

  /* ── STICKY HEADER ──────────────────────────────── */
  const siteHeader = document.getElementById('site-header');
  if (siteHeader) {
    window.addEventListener('scroll', function () {
      siteHeader.classList.toggle('scrolled', window.scrollY > 50);
    });
  }

  /* ── SCROLL TO TOP ──────────────────────────────── */
  const scrollTop = document.getElementById('scroll-top');
  if (scrollTop) {
    window.addEventListener('scroll', function () {
      scrollTop.classList.toggle('visible', window.scrollY > 400);
    });
    scrollTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ── FADE-UP ANIMATION (Intersection Observer) ── */
  const fadeElements = document.querySelectorAll('.fade-up');
  if (fadeElements.length > 0) {
    const observer = new IntersectionObserver(function (entries) {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    fadeElements.forEach(el => observer.observe(el));
  }

  /* ── ACTIVE NAV LINK ────────────────────────────── */
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });

  /* ── COUNTER ANIMATION ──────────────────────────── */
  function animateCounter(el, target, duration) {
    const start = 0;
    const step  = target / (duration / 16);
    let current = start;
    const isPlus = el.dataset.suffix === '+';

    const timer = setInterval(() => {
      current += step;
      if (current >= target) {
        current = target;
        clearInterval(timer);
      }
      el.textContent = Math.floor(current) + (isPlus ? '+' : '');
    }, 16);
  }

  const statNumbers = document.querySelectorAll('.stat-number[data-count]');
  if (statNumbers.length > 0) {
    const counterObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el  = entry.target;
          const val = parseInt(el.dataset.count, 10);
          animateCounter(el, val, 1500);
          counterObserver.unobserve(el);
        }
      });
    }, { threshold: 0.5 });
    statNumbers.forEach(el => counterObserver.observe(el));
  }

  /* ── PRODUCT GALLERY THUMBS ─────────────────────── */
  const thumbs = document.querySelectorAll('.product-thumb');
  const mainImg = document.querySelector('.product-gallery-main img');
  if (thumbs.length > 0 && mainImg) {
    thumbs.forEach(thumb => {
      thumb.addEventListener('click', function () {
        thumbs.forEach(t => t.classList.remove('active'));
        this.classList.add('active');
        const src = this.querySelector('img').src;
        mainImg.style.opacity = '0';
        setTimeout(() => {
          mainImg.src = src;
          mainImg.style.opacity = '1';
        }, 200);
        mainImg.style.transition = 'opacity 0.2s ease';
      });
    });
  }

  /* ── CONTACT FORM ───────────────────────────────── */
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const nome     = document.getElementById('nome')?.value.trim();
      const email    = document.getElementById('email')?.value.trim();
      const mensagem = document.getElementById('mensagem')?.value.trim();

      if (!nome || !email || !mensagem) {
        alert('Por favor, preencha os campos obrigatórios: Nome, E-mail e Mensagem.');
        return;
      }

      // Build WhatsApp message as fallback
      const produto   = document.getElementById('produto')?.value || '';
      const telefone  = document.getElementById('telefone')?.value || '';
      const empresa   = document.getElementById('empresa')?.value || '';

      let msg = `Olá! Gostaria de solicitar um orçamento.\n\n`;
      msg += `*Nome:* ${nome}\n`;
      if (empresa)   msg += `*Empresa:* ${empresa}\n`;
      msg += `*E-mail:* ${email}\n`;
      if (telefone)  msg += `*Telefone:* ${telefone}\n`;
      if (produto)   msg += `*Produto:* ${produto}\n`;
      msg += `*Mensagem:* ${mensagem}`;

      const waUrl = `https://wa.me/5554992425851?text=${encodeURIComponent(msg)}`;

      const submitBtn = contactForm.querySelector('[type="submit"]');
      const originalText = submitBtn.innerHTML;
      submitBtn.innerHTML = '<i class="fas fa-check-circle"></i> Redirecionando para WhatsApp...';
      submitBtn.disabled = true;

      setTimeout(() => {
        window.open(waUrl, '_blank');
        submitBtn.innerHTML = originalText;
        submitBtn.disabled  = false;
        contactForm.reset();
      }, 800);
    });
  }

  /* ── SMOOTH SCROLL FOR ANCHOR LINKS ─────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const headerHeight = siteHeader ? siteHeader.offsetHeight : 0;
        const targetPos    = target.getBoundingClientRect().top + window.scrollY - headerHeight - 20;
        window.scrollTo({ top: targetPos, behavior: 'smooth' });
      }
    });
  });

});
