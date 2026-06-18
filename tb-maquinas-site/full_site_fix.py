import os
import re

base = r'C:\Users\Eduarda\Desktop\projeto Tb Máquinas\tb-maquinas-site'

# ==============================================================
# 1. REWRITE COMPLETE STYLE.CSS
# ==============================================================
css = r"""
@font-face {
  font-family: 'mbf-canno';
  src: url('../fonts/mbf-canno.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}

/* ═══════════════════════════════════════════════════════════
   TB MÁQUINAS — Design System
   Paleta: Preto, Cinza, Laranja | Layout Claro
   ═══════════════════════════════════════════════════════════ */

@import url('https://fonts.googleapis.com/css2?family=Titillium+Web:wght@300;400;600;700;900&family=Open+Sans:wght@300;400;500;600&display=swap');

/* ─── RESET ─────────────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; font-size: 15px; }

/* ─── VARIÁVEIS ─────────────────────────────────────────────── */
:root {
  --primary:       #000000;
  --primary-hover: #424449;
  --accent:        #FF7B00;
  --accent-hover:  #e66b00;
  --white:         #ffffff;
  --light-bg:      #F5F5F5;
  --body-text:     #4C4E52;
  --dark-text:     #000000;
  --border:        #E0E0E0;
  --topbar-bg:     #000000;
  --nav-bg:        #ffffff;
  --footer-bg:     #000000;
  --footer-text:   rgba(255,255,255,0.70);
  --radius:        4px;
  --radius-lg:     8px;
  --shadow:        0 4px 20px rgba(0,0,0,0.08);
  --shadow-hover:  0 8px 32px rgba(0,0,0,0.16);
  --transition:    all 0.3s ease;
  --font-heading:  'Titillium Web', sans-serif;
  --font-body:     'Open Sans', sans-serif;
  --container:     1200px;
  --section-pad:   90px 0;
  --section-pad-sm:50px 0;
}

/* ─── BASE ──────────────────────────────────────────────────── */
body {
  font-family: var(--font-body);
  font-size: 15px;
  color: var(--body-text);
  line-height: 1.7;
  background: var(--white);
  -webkit-font-smoothing: antialiased;
}
a { color: var(--accent); text-decoration: none; transition: var(--transition); }
a:hover { color: var(--accent-hover); }
img { max-width: 100%; height: auto; display: block; }
ul { list-style: none; }
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-heading);
  color: var(--dark-text);
  line-height: 1.25;
  font-weight: 700;
}
p { margin-bottom: 1rem; }
p:last-child { margin-bottom: 0; }

/* ─── CONTAINER ─────────────────────────────────────────────── */
.container { max-width: var(--container); margin: 0 auto; padding: 0 30px; }
@media (max-width: 768px) { .container { padding: 0 20px; } }

/* ─── UTILITIES ─────────────────────────────────────────────── */
.text-center { text-align: center; }
.text-left   { text-align: left; }
.d-flex      { display: flex; align-items: center; }
.section-padding    { padding: var(--section-pad); }
.section-padding-sm { padding: var(--section-pad-sm); }
.bg-light    { background: var(--light-bg); }
.bg-primary  { background: var(--primary); }
.bg-dark     { background: var(--footer-bg); }
.fade-up     { opacity: 0; transform: translateY(30px); transition: opacity 0.6s ease, transform 0.6s ease; }
.fade-up.visible { opacity: 1; transform: translateY(0); }
.fade-up-delay-1 { transition-delay: 0.1s; }
.fade-up-delay-2 { transition-delay: 0.2s; }
.fade-up-delay-3 { transition-delay: 0.3s; }

/* ─── SECTION HEADER ────────────────────────────────────────── */
.section-header { text-align: center; margin-bottom: 56px; }
.section-label {
  display: inline-block;
  font-family: var(--font-heading);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 12px;
}
.section-label::before { content: '//'; margin-right: 6px; color: var(--primary); }
.section-title {
  font-size: clamp(26px, 3.5vw, 40px);
  font-weight: 700;
  color: var(--dark-text);
  margin-bottom: 16px;
}
.section-title span { color: var(--accent); }
.section-title.left { text-align: left; }
.section-desc {
  font-size: 16px;
  color: var(--body-text);
  max-width: 640px;
  margin: 0 auto;
  line-height: 1.8;
}
.section-title-line::after {
  content: '';
  display: block;
  width: 50px;
  height: 3px;
  background: var(--accent);
  margin: 16px auto 0;
}
.section-title-line.left::after { margin-left: 0; }

/* ─── BUTTONS ───────────────────────────────────────────────── */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 14px 30px;
  font-family: var(--font-heading);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  border-radius: var(--radius);
  cursor: pointer;
  border: 2px solid transparent;
  transition: var(--transition);
  white-space: nowrap;
  text-decoration: none;
}
.btn-primary { background: var(--accent); color: var(--white); border-color: var(--accent); }
.btn-primary:hover {
  background: var(--accent-hover); border-color: var(--accent-hover); color: var(--white);
  transform: translateY(-2px); box-shadow: 0 6px 20px rgba(255,123,0,0.35);
}
.btn-outline { background: transparent; color: var(--dark-text); border-color: var(--dark-text); }
.btn-outline:hover { background: var(--dark-text); color: var(--white); transform: translateY(-2px); }
.btn-outline-white { background: transparent; color: var(--white); border-color: var(--white); }
.btn-outline-white:hover { background: var(--white); color: var(--dark-text); }
.btn-whatsapp { background: var(--accent); color: var(--white); border-color: var(--accent); }
.btn-whatsapp:hover { background: var(--accent-hover); border-color: var(--accent-hover); color: var(--white); transform: translateY(-2px); }
.btn-nav { background: var(--accent); color: var(--white); padding: 10px 22px; font-size: 12px; border-radius: var(--radius); }
.btn-nav:hover { background: var(--accent-hover); color: var(--white); }
.btn-lg { padding: 18px 38px; font-size: 14px; }
.btn-sm { padding: 9px 18px; font-size: 12px; }

/* ─── TOPBAR ────────────────────────────────────────────────── */
.topbar {
  background: var(--topbar-bg);
  padding: 0;
  font-size: 13px;
  position: relative;
  z-index: 101;
}
.topbar-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  min-height: 44px;
}
.topbar-contact { display: flex; align-items: center; gap: 24px; }
.topbar-contact a {
  color: rgba(255,255,255,0.75);
  display: flex; align-items: center; gap: 6px;
  font-size: 12px; letter-spacing: 0.3px;
  transition: var(--transition);
}
.topbar-contact a:hover { color: var(--accent); }
.topbar-contact a i { font-size: 11px; }
.topbar-right { display: flex; align-items: center; gap: 24px; }
.topbar-hours { font-size: 11px; color: rgba(255,255,255,0.65); text-align: right; line-height: 1.5; }
.topbar-social { display: flex; align-items: center; gap: 12px; }
.topbar-social a { color: rgba(255,255,255,0.65); font-size: 13px; transition: var(--transition); }
.topbar-social a:hover { color: var(--accent); }

/* ─── HEADER / NAVIGATION ───────────────────────────────────── */
.site-header {
  background: rgba(255,255,255,0.92);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  box-shadow: 0 1px 0 rgba(0,0,0,0.08), 0 4px 20px rgba(0,0,0,0.06);
  position: sticky;
  top: 0;
  z-index: 100;
  transition: var(--transition);
}
.site-header.scrolled {
  background: rgba(255,255,255,0.97);
  box-shadow: 0 2px 0 rgba(255,123,0,0.4), 0 4px 24px rgba(0,0,0,0.10);
}
.header-inner {
  display: flex; align-items: center; justify-content: space-between;
  min-height: 78px; gap: 20px;
}

/* Logo */
.logo { display: flex; align-items: center; gap: 12px; color: var(--dark-text); text-decoration: none; flex-shrink: 0; }
.logo img.site-logo-main { height: 52px; width: auto; object-fit: contain; }
.logo img.site-logo-icon { height: 40px; width: auto; object-fit: contain; }
.logo-text {
  font-family: var(--font-heading);
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--dark-text);
  line-height: 1.3;
}

/* Navigation */
.main-nav { display: flex; align-items: center; gap: 8px; }
.nav-menu { display: flex; align-items: center; gap: 0; }
.nav-item { position: relative; }
.nav-link {
  display: block;
  padding: 0 18px;
  line-height: 78px;
  font-family: var(--font-heading);
  font-size: 13px;
  font-weight: 600;
  color: var(--dark-text);
  letter-spacing: 0.8px;
  text-transform: uppercase;
  transition: var(--transition);
  white-space: nowrap;
  position: relative;
}
.nav-link:hover, .nav-link.active { color: var(--accent); }
.nav-link::after {
  content: '';
  display: block;
  height: 2px;
  background: var(--accent);
  transform: scaleX(0);
  transition: transform 0.3s ease;
  position: absolute;
  bottom: 0;
  left: 18px;
  right: 18px;
  border-radius: 2px;
}
.nav-link:hover::after, .nav-link.active::after { transform: scaleX(1); }
.nav-actions { display: flex; align-items: center; gap: 10px; margin-left: 12px; }

/* WhatsApp header btn */
.whatsapp-btn-header {
  display: flex; align-items: center; gap: 6px;
  padding: 8px 16px; background: var(--accent); color: var(--white);
  border-radius: var(--radius); font-family: var(--font-heading);
  font-size: 12px; font-weight: 700; letter-spacing: 1px;
  text-transform: uppercase; transition: var(--transition);
}
.whatsapp-btn-header:hover { background: var(--accent-hover); color: var(--white); transform: translateY(-1px); }

/* Hamburger */
.hamburger {
  display: none; flex-direction: column; gap: 5px;
  cursor: pointer; background: none; border: none;
  padding: 8px; border-radius: var(--radius);
}
.hamburger span { display: block; width: 24px; height: 2px; background: var(--dark-text); transition: var(--transition); border-radius: 2px; }

/* Mobile Nav */
@media (max-width: 900px) {
  .hamburger { display: flex; }
  .main-nav {
    display: none; position: absolute; top: 100%; left: 0; right: 0;
    background: rgba(255,255,255,0.98); backdrop-filter: blur(12px);
    flex-direction: column; align-items: stretch; padding: 16px 0;
    box-shadow: 0 10px 30px rgba(0,0,0,0.12);
    border-top: 3px solid var(--accent); z-index: 200;
  }
  .main-nav.open { display: flex; }
  .nav-menu { flex-direction: column; width: 100%; }
  .nav-link { line-height: 1; padding: 16px 24px; border-bottom: 1px solid var(--border); font-size: 14px; }
  .nav-link::after { display: none; }
  .nav-actions { flex-direction: column; padding: 16px 24px; margin-left: 0; align-items: flex-start; gap: 10px; }
  .topbar-contact { gap: 12px; }
  .topbar-contact a span { display: none; }
  .topbar-hours { display: none; }
}
@media (max-width: 480px) { .topbar-contact a:not(:first-child) { display: none; } }

/* ─── HERO ──────────────────────────────────────────────────── */
.hero {
  position: relative; min-height: 620px;
  display: flex; align-items: center; overflow: hidden;
  background: var(--primary);
}
.hero-bg { position: absolute; inset: 0; object-fit: cover; width: 100%; height: 100%; z-index: 0; }
.hero-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(110deg, rgba(0,0,0,0.88) 0%, rgba(0,0,0,0.68) 60%, rgba(0,0,0,0.28) 100%);
  z-index: 1;
}
.hero-content { position: relative; z-index: 2; max-width: 680px; padding: 80px 0; }
.hero-text { max-width: 640px; }
.hero-label {
  display: inline-flex; align-items: center; gap: 10px;
  font-family: var(--font-heading); font-size: 11px; font-weight: 700;
  letter-spacing: 3px; text-transform: uppercase;
  color: var(--accent); margin-bottom: 20px;
}
.hero-label::before { content: ''; display: block; width: 36px; height: 2px; background: var(--accent); }
.hero h1 {
  font-family: var(--font-heading); font-size: clamp(36px, 5.5vw, 64px);
  font-weight: 900; color: var(--white); line-height: 1.1; margin-bottom: 20px;
}
.hero h1 span { color: var(--accent); }
.hero-desc { font-size: 17px; color: rgba(255,255,255,0.82); line-height: 1.8; margin-bottom: 36px; max-width: 560px; }
.hero-actions { display: flex; flex-wrap: wrap; gap: 14px; align-items: center; }
.hero-stats {
  display: flex; gap: 36px; margin-top: 56px;
  padding-top: 36px; border-top: 1px solid rgba(255,255,255,0.2);
}
.hero-stat-number { font-family: var(--font-heading); font-size: 38px; font-weight: 900; color: var(--accent); line-height: 1; }
.hero-stat-label { font-size: 12px; color: rgba(255,255,255,0.65); text-transform: uppercase; letter-spacing: 1px; margin-top: 4px; }
@media (max-width: 768px) {
  .hero { min-height: 500px; }
  .hero-stats { gap: 24px; flex-wrap: wrap; }
  .hero-content { padding: 60px 0; }
}

/* ─── PAGE HERO ─────────────────────────────────────────────── */
.page-hero {
  background: var(--primary); padding: 60px 0;
  position: relative; overflow: hidden;
}
.page-hero::before {
  content: ''; position: absolute; right: -100px; top: 50%;
  transform: translateY(-50%); width: 500px; height: 500px;
  background: var(--accent); opacity: 0.05; border-radius: 50%;
}
.page-hero-content { position: relative; z-index: 1; }
.page-hero h1 {
  font-family: var(--font-heading); font-size: clamp(28px, 4vw, 48px);
  font-weight: 900; color: var(--white); margin-bottom: 14px;
}
.breadcrumb { display: flex; align-items: center; gap: 8px; font-size: 13px; }
.breadcrumb a { color: rgba(255,255,255,0.65); }
.breadcrumb a:hover { color: var(--accent); }
.breadcrumb-sep { color: rgba(255,255,255,0.4); font-size: 10px; }
.breadcrumb-current { color: var(--accent); font-weight: 600; }

/* ─── SERVICE CARDS ─────────────────────────────────────────── */
.services-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0; }
.service-card {
  padding: 48px 36px; border: 1px solid var(--border);
  transition: var(--transition); position: relative; overflow: hidden;
  background: var(--white);
}
.service-card::before {
  content: ''; position: absolute; bottom: 0; left: 0; right: 0;
  height: 4px; background: var(--accent); transform: scaleX(0); transition: transform 0.3s ease;
}
.service-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-hover); }
.service-card:hover::before { transform: scaleX(1); }
.service-icon {
  width: 64px; height: 64px; background: rgba(0,0,0,0.06);
  border-radius: var(--radius); display: flex; align-items: center;
  justify-content: center; font-size: 28px; color: var(--dark-text);
  margin-bottom: 20px; transition: var(--transition);
}
.service-card:hover .service-icon { background: var(--accent); color: var(--white); transform: scale(1.05); }
.service-card h3 { font-family: var(--font-heading); font-size: 18px; color: var(--dark-text); margin-bottom: 10px; }
.service-card p { font-size: 14px; color: var(--body-text); margin: 0; }
@media (max-width: 900px) { .services-grid { grid-template-columns: 1fr 1fr; } }
@media (max-width: 600px) { .services-grid { grid-template-columns: 1fr; } }

/* ─── PRODUCT CARDS ─────────────────────────────────────────── */
.products-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; }
.product-card {
  background: var(--white); border: 1px solid var(--border);
  border-radius: var(--radius-lg); overflow: hidden;
  transition: var(--transition); display: flex; flex-direction: column;
}
.product-card:hover { transform: translateY(-6px); box-shadow: var(--shadow-hover); border-color: var(--accent); }
.product-card-image { position: relative; height: 240px; overflow: hidden; background: var(--light-bg); }
.product-card-image img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; }
.product-card:hover .product-card-image img { transform: scale(1.05); }
.product-card-badge {
  position: absolute; top: 14px; left: 14px; background: var(--accent); color: var(--white);
  font-family: var(--font-heading); font-size: 10px; font-weight: 700;
  letter-spacing: 1.5px; text-transform: uppercase; padding: 4px 10px; border-radius: var(--radius);
}
.product-card-body { padding: 24px; flex: 1; display: flex; flex-direction: column; }
.product-card-category { font-size: 11px; font-weight: 700; color: var(--accent); text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 8px; }
.product-card h3 { font-size: 17px; color: var(--dark-text); margin-bottom: 10px; line-height: 1.3; }
.product-card p { font-size: 13px; color: var(--body-text); flex: 1; margin-bottom: 18px; }
@media (max-width: 900px) { .products-grid { grid-template-columns: 1fr 1fr; } }
@media (max-width: 600px) { .products-grid { grid-template-columns: 1fr; } }

/* ─── ABOUT SECTION ─────────────────────────────────────────── */
.about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 70px; align-items: center; }
.about-image { position: relative; }
.about-image-main { width: 100%; height: 480px; object-fit: cover; border-radius: var(--radius-lg); display: block; }
.about-image-badge {
  position: absolute; bottom: -20px; right: -20px;
  background: var(--accent); color: var(--white); width: 110px; height: 110px;
  border-radius: 50%; display: flex; flex-direction: column; align-items: center;
  justify-content: center; text-align: center; box-shadow: 0 8px 24px rgba(255,123,0,0.4);
}
.badge-number { font-family: var(--font-heading); font-size: 28px; font-weight: 900; line-height: 1; }
.badge-label { font-size: 11px; line-height: 1.3; margin-top: 2px; }
.about-content { max-width: 520px; }
.about-text { font-size: 15px; color: var(--body-text); line-height: 1.85; margin-bottom: 18px; }
@media (max-width: 900px) {
  .about-grid { grid-template-columns: 1fr; gap: 40px; }
  .about-image-main { height: 340px; }
  .about-image-badge { bottom: 10px; right: 10px; }
  .about-content { max-width: 100%; }
}

/* ─── STATS BAR ─────────────────────────────────────────────── */
.stats-bar { background: var(--primary); padding: 48px 0; }
.stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0; }
.stat-item { text-align: center; padding: 20px; border-right: 1px solid rgba(255,255,255,0.12); }
.stat-item:last-child { border-right: none; }
.stat-number { font-family: var(--font-heading); font-size: clamp(32px, 4vw, 48px); font-weight: 900; color: var(--accent); line-height: 1; margin-bottom: 8px; }
.stat-label { font-size: 12px; color: rgba(255,255,255,0.65); text-transform: uppercase; letter-spacing: 1.5px; }
@media (max-width: 768px) {
  .stats-grid { grid-template-columns: repeat(2, 1fr); }
  .stat-item { border-right: 1px solid rgba(255,255,255,0.12); border-bottom: 1px solid rgba(255,255,255,0.12); }
}

/* ─── CTA BANNER ────────────────────────────────────────────── */
.cta-banner { background: linear-gradient(135deg, var(--primary) 0%, #424449 100%); position: relative; overflow: hidden; }
.cta-banner::before {
  content: ''; position: absolute; right: -80px; top: -80px;
  width: 300px; height: 300px; background: var(--accent); opacity: 0.08; border-radius: 50%;
}
.cta-inner { display: flex; align-items: center; justify-content: space-between; gap: 40px; position: relative; z-index: 1; }
.cta-text h2 { font-family: var(--font-heading); font-size: clamp(22px, 3vw, 36px); color: var(--white); margin-bottom: 8px; }
.cta-text p { color: rgba(255,255,255,0.75); font-size: 16px; margin: 0; }
.cta-actions { display: flex; gap: 14px; flex-shrink: 0; flex-wrap: wrap; }
@media (max-width: 768px) { .cta-inner { flex-direction: column; text-align: center; } .cta-actions { justify-content: center; } }

/* ─── PARTNERS / CLIENTS ────────────────────────────────────── */
.partners-grid { display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; align-items: center; margin-top: 48px; }
.partner-logo { max-width: 120px; max-height: 60px; object-fit: contain; filter: grayscale(100%) opacity(55%); transition: var(--transition); }
.partner-logo:hover { filter: grayscale(0%) opacity(100%); transform: scale(1.08); }

/* ─── GALLERY ───────────────────────────────────────────────── */
.gallery-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 20px; }
.gallery-item { position: relative; border-radius: var(--radius-lg); overflow: hidden; aspect-ratio: 4/3; }
.gallery-item img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; display: block; }
.gallery-item:hover img { transform: scale(1.06); }
.gallery-item-overlay, .gallery-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.65) 0%, transparent 60%);
  opacity: 0; transition: var(--transition);
  display: flex; align-items: center; justify-content: center;
}
.gallery-item:hover .gallery-item-overlay,
.gallery-item:hover .gallery-overlay { opacity: 1; }
.gallery-item-overlay i, .gallery-overlay i { color: var(--white); font-size: 28px; }
@media (max-width: 768px) { .gallery-grid { grid-template-columns: 1fr 1fr; } }
@media (max-width: 480px) { .gallery-grid { grid-template-columns: 1fr; } }

/* ─── CONTACT ───────────────────────────────────────────────── */
.contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 70px; align-items: start; }
.contact-info-list { display: flex; flex-direction: column; gap: 0; }
.contact-info-item { display: flex; align-items: flex-start; gap: 16px; padding: 18px 0; border-bottom: 1px solid var(--border); }
.contact-info-item:first-child { padding-top: 0; }
.contact-info-item:last-child { border-bottom: none; }
.contact-info-icon {
  width: 44px; height: 44px; background: rgba(0,0,0,0.06);
  border-radius: var(--radius); display: flex; align-items: center;
  justify-content: center; font-size: 18px; color: var(--dark-text);
  flex-shrink: 0; transition: var(--transition);
}
.contact-info-item:hover .contact-info-icon { background: var(--accent); color: var(--white); }
.contact-info-text { display: flex; flex-direction: column; gap: 2px; }
.contact-info-text strong { font-size: 13px; font-weight: 700; color: var(--dark-text); text-transform: uppercase; letter-spacing: 0.5px; }
.contact-info-text a, .contact-info-text span { font-size: 14px; color: var(--body-text); transition: var(--transition); }
.contact-info-text a:hover { color: var(--accent); }

.contact-form-card {
  background: var(--white); border: 1px solid var(--border);
  border-radius: var(--radius-lg); padding: 40px; box-shadow: var(--shadow);
}
.contact-form-card h3 {
  font-family: var(--font-heading); font-size: 22px; color: var(--dark-text);
  margin-bottom: 28px; padding-bottom: 16px; border-bottom: 2px solid var(--accent); display: inline-block; width: 100%;
}
.form-group { margin-bottom: 20px; }
.form-label { display: block; font-size: 13px; font-weight: 600; color: var(--dark-text); margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px; }
.form-control {
  width: 100%; padding: 12px 16px; font-family: var(--font-body);
  font-size: 14px; color: var(--dark-text); background: var(--white);
  border: 1px solid var(--border); border-radius: var(--radius);
  transition: var(--transition); outline: none;
}
.form-control:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(255,123,0,0.12); }
.form-control::placeholder { color: #aaa; }
.form-control.error { border-color: #e74c3c; }
.form-error { font-size: 12px; color: #e74c3c; margin-top: 4px; display: none; }
.form-error.visible { display: block; }
textarea.form-control { resize: vertical; min-height: 120px; }
select.form-control { cursor: pointer; }
@media (max-width: 900px) { .contact-grid { grid-template-columns: 1fr; gap: 40px; } .contact-form-card { padding: 28px 20px; } }

/* ─── MAP ───────────────────────────────────────────────────── */
.map-wrap { border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow); margin-top: 48px; }
.map-wrap iframe { display: block; width: 100%; height: 400px; border: none; }

/* ─── PRODUCT PAGE ──────────────────────────────────────────── */
.product-detail-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: start; }
.product-detail-image { border-radius: var(--radius-lg); overflow: hidden; background: var(--light-bg); }
.product-detail-image img { width: 100%; height: auto; display: block; }
.product-detail-content h1 { font-size: clamp(24px, 3vw, 36px); color: var(--dark-text); margin-bottom: 16px; }
.product-detail-desc { font-size: 15px; color: var(--body-text); line-height: 1.8; margin-bottom: 28px; }
.product-features-title { font-family: var(--font-heading); font-size: 15px; font-weight: 700; color: var(--dark-text); margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.5px; }
.product-features-list { list-style: none; }
.product-features-list li { display: flex; align-items: flex-start; gap: 10px; padding: 8px 0; border-bottom: 1px solid var(--border); font-size: 14px; color: var(--body-text); }
.product-features-list li:last-child { border-bottom: none; }
.product-features-list li i { color: var(--accent); margin-top: 3px; flex-shrink: 0; }
.product-actions { display: flex; gap: 14px; margin-top: 32px; flex-wrap: wrap; }
@media (max-width: 768px) { .product-detail-grid { grid-template-columns: 1fr; gap: 32px; } }

/* Product gallery */
.product-gallery-main { border-radius: var(--radius-lg); overflow: hidden; margin-bottom: 12px; }
.product-gallery-main img { width: 100%; height: 380px; object-fit: contain; background: var(--light-bg); transition: opacity 0.2s ease; }
.product-thumbs { display: flex; gap: 10px; flex-wrap: wrap; }
.product-thumb {
  width: 72px; height: 72px; border-radius: var(--radius);
  overflow: hidden; cursor: pointer; border: 2px solid transparent;
  transition: var(--transition); background: var(--light-bg);
}
.product-thumb.active, .product-thumb:hover { border-color: var(--accent); }
.product-thumb img { width: 100%; height: 100%; object-fit: cover; }

/* ─── FINANCIAMENTOS ────────────────────────────────────────── */
.finance-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 20px; margin-top: 36px; }
.finance-card {
  text-align: center; padding: 28px 20px;
  border: 1px solid var(--border); border-radius: var(--radius-lg);
  transition: var(--transition);
}
.finance-card:hover { border-color: var(--accent); box-shadow: var(--shadow); }
.finance-card img { height: 50px; object-fit: contain; margin: 0 auto 16px; filter: grayscale(60%); transition: var(--transition); }
.finance-card:hover img { filter: grayscale(0%); }
.finance-card h4 { font-size: 15px; color: var(--dark-text); margin-bottom: 6px; }
.finance-card p { font-size: 13px; color: var(--body-text); margin: 0; }
@media (max-width: 768px) { .finance-grid { grid-template-columns: 1fr 1fr; } }

/* ─── FOOTER ────────────────────────────────────────────────── */
.site-footer { background: var(--footer-bg); color: var(--footer-text); padding: 60px 0 0; }
.footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 40px; padding-bottom: 48px; }
.footer-brand { max-width: 300px; }
.footer-logo-wrap { display: flex; align-items: center; margin-bottom: 20px; }
.footer-logo-img { height: 80px; width: auto; object-fit: contain; display: block; }
.footer-desc { font-size: 14px; color: var(--footer-text); line-height: 1.8; margin-bottom: 20px; }
.footer-social { display: flex; gap: 10px; }
.footer-social a {
  width: 36px; height: 36px; background: rgba(255,255,255,0.08);
  border-radius: var(--radius); display: flex; align-items: center;
  justify-content: center; color: rgba(255,255,255,0.65);
  font-size: 14px; transition: var(--transition); text-decoration: none;
}
.footer-social a:hover { background: var(--accent); color: var(--white); }
.footer-col h4, .footer-widget h4 {
  font-family: var(--font-heading); font-size: 12px; font-weight: 700;
  color: var(--white); text-transform: uppercase; letter-spacing: 1.5px;
  margin-bottom: 20px; padding-bottom: 10px;
  border-bottom: 2px solid var(--accent); display: inline-block;
}
.footer-links { display: flex; flex-direction: column; gap: 8px; }
.footer-links a {
  color: var(--footer-text); font-size: 14px; transition: var(--transition);
  display: flex; align-items: center; gap: 6px; text-decoration: none;
}
.footer-links a::before { content: '›'; color: var(--accent); font-size: 16px; }
.footer-links a:hover { color: var(--white); padding-left: 4px; }
.footer-contact-list { display: flex; flex-direction: column; gap: 12px; }
.footer-contact-item { display: flex; align-items: flex-start; gap: 10px; font-size: 13px; color: var(--footer-text); }
.footer-contact-item i { color: var(--accent); font-size: 14px; margin-top: 2px; flex-shrink: 0; }
.footer-contact-item a { color: var(--footer-text); transition: var(--transition); text-decoration: none; }
.footer-contact-item a:hover { color: var(--accent); }
.footer-bottom { border-top: 1px solid rgba(255,255,255,0.10); padding: 20px 0; }
.footer-bottom-inner { display: flex; justify-content: space-between; align-items: center; gap: 20px; flex-wrap: wrap; }
.footer-bottom p, .footer-copyright { font-size: 13px; color: rgba(255,255,255,0.45); margin: 0; }
.footer-bottom a { color: rgba(255,255,255,0.45); text-decoration: none; }
.footer-evolutor { font-size: 12px; color: rgba(255,255,255,0.35); display: flex; align-items: center; gap: 6px; }
.footer-evolutor a { color: var(--accent); font-family: 'mbf-canno', sans-serif; font-size: 14px; letter-spacing: 1px; transition: var(--transition); }
.footer-evolutor a:hover { color: var(--white); }
@media (max-width: 900px) { .footer-grid { grid-template-columns: 1fr 1fr; } .footer-brand { max-width: 100%; } }
@media (max-width: 580px) { .footer-grid { grid-template-columns: 1fr; } .footer-bottom-inner { flex-direction: column; text-align: center; } }

/* ─── FLOATING WHATSAPP BUTTON ──────────────────────────────── */
.float-whatsapp, .whatsapp-float {
  position: fixed; bottom: 28px; right: 28px;
  width: 56px; height: 56px; background: #25D366;
  border-radius: 50%; display: flex; align-items: center;
  justify-content: center; font-size: 26px; color: var(--white);
  box-shadow: 0 4px 20px rgba(37,211,102,0.45);
  z-index: 999; transition: var(--transition); text-decoration: none;
}
.float-whatsapp:hover, .whatsapp-float:hover {
  background: #1da851; color: var(--white);
  transform: scale(1.1); box-shadow: 0 6px 28px rgba(37,211,102,0.55);
}
.wa-tooltip {
  position: absolute; right: 70px; white-space: nowrap;
  background: var(--dark-text); color: var(--white);
  font-size: 12px; font-weight: 600; padding: 6px 12px;
  border-radius: var(--radius); opacity: 0; pointer-events: none;
  transition: var(--transition); font-family: var(--font-body);
}
.float-whatsapp:hover .wa-tooltip { opacity: 1; }

/* ─── SCROLL TO TOP ─────────────────────────────────────────── */
#scroll-top {
  position: fixed; bottom: 96px; right: 28px;
  width: 44px; height: 44px;
  background: var(--primary); color: var(--white);
  border: none; border-radius: var(--radius);
  display: flex; align-items: center; justify-content: center;
  font-size: 16px; cursor: pointer; z-index: 998;
  opacity: 0; transform: translateY(10px);
  transition: var(--transition); box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
#scroll-top.visible { opacity: 1; transform: translateY(0); }
#scroll-top:hover { background: var(--accent); }

/* ─── FEATURES LIST ─────────────────────────────────────────── */
.features-list { list-style: none; }
.features-list li {
  display: flex; align-items: flex-start; gap: 12px;
  padding: 10px 0; border-bottom: 1px solid var(--border);
  font-size: 14px; color: var(--body-text);
}
.features-list li:last-child { border-bottom: none; }
.features-list li i { color: var(--accent); font-size: 16px; margin-top: 2px; flex-shrink: 0; }

/* ─── ACCORDION ─────────────────────────────────────────────── */
.accordion-item { border: 1px solid var(--border); border-radius: var(--radius); margin-bottom: 8px; overflow: hidden; }
.accordion-header {
  width: 100%; background: var(--white); border: none; text-align: left;
  padding: 18px 20px; font-family: var(--font-heading); font-size: 15px;
  font-weight: 600; color: var(--dark-text); cursor: pointer;
  display: flex; justify-content: space-between; align-items: center; transition: var(--transition);
}
.accordion-header:hover { background: var(--light-bg); }
.accordion-header i { transition: transform 0.3s ease; color: var(--accent); }
.accordion-item.open .accordion-header i { transform: rotate(180deg); }
.accordion-body { max-height: 0; overflow: hidden; transition: max-height 0.4s ease; }
.accordion-body-inner { padding: 0 20px 20px; font-size: 14px; color: var(--body-text); line-height: 1.8; }

/* ─── ALERTS ────────────────────────────────────────────────── */
.alert { padding: 14px 20px; border-radius: var(--radius); font-size: 14px; margin-bottom: 16px; display: flex; align-items: center; gap: 10px; }
.alert-success { background: #f0fdf4; color: #166534; border: 1px solid #bbf7d0; }
.alert-error   { background: #fef2f2; color: #991b1b; border: 1px solid #fecaca; }
.alert-info    { background: #f0f9ff; color: #1e40af; border: 1px solid #bae6fd; }

/* ─── MISC ──────────────────────────────────────────────────── */
.divider { width: 50px; height: 3px; background: var(--accent); margin: 16px 0; }
.divider.center { margin: 16px auto; }
.highlight-text { color: var(--accent); font-weight: 700; }
.text-muted { color: var(--body-text); }
.text-white { color: var(--white); }
.related-section { background: var(--light-bg); }

/* ─── RESPONSIVE ────────────────────────────────────────────── */
@media (max-width: 768px) {
  .hide-mobile { display: none !important; }
  .section-header { margin-bottom: 36px; }
}
@media (min-width: 769px) { .hide-desktop { display: none !important; } }
"""

with open(os.path.join(base, 'css', 'style.css'), 'w', encoding='utf-8') as f:
    f.write(css)
print("style.css written ✓")

# ==============================================================
# 2. FOOTER SNIPPET — reusable
# ==============================================================
FOOTER = '''  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" style="display:block;margin-bottom:24px;">
            <img src="images/produtos/cropped-logomarca.png" alt="TB Máquinas" style="max-height:90px;width:auto;object-fit:contain;">
          </a>
          <p class="footer-desc">Trabalhamos com inovação de alto nível e as tecnologias mais modernas de produção de rotuladoras e peças de reposição.</p>
          <div class="footer-social">
            <a href="https://www.instagram.com/tbmaquinas_equipamentos/" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
            <a href="https://www.youtube.com/@TBMAQUINAS" target="_blank" rel="noopener" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
            <a href="https://wa.me/5554992425851?text=Ol%C3%A1!%20Gostaria%20de%20obter%20mais%20informa%C3%A7%C3%B5es%20sobre%20os%20produtos%20e%20servi%C3%A7os%20da%20TB%20M%C3%A1quinas." target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>
            <a href="mailto:tbmaquinas@tbmaquinas.com" aria-label="E-mail"><i class="fas fa-envelope"></i></a>
          </div>
        </div>
        <div class="footer-widget">
          <h4>Navegação</h4>
          <nav class="footer-links">
            <a href="index.html">Início</a>
            <a href="produtos.html">Produtos</a>
            <a href="servicos.html">Serviços</a>
            <a href="feiras.html">Feiras</a>
            <a href="sobre.html">Sobre</a>
            <a href="contato.html">Contato</a>
          </nav>
        </div>
        <div class="footer-widget">
          <h4>Produtos</h4>
          <nav class="footer-links">
            <a href="envolvedora-tb-evp-pre.html">Envolvedoras</a>
            <a href="mesa-acumulo-tb-ms.html">Mesas de Acúmulo</a>
            <a href="rotuladora-tb-raa.html">Rotuladora TB-RAA</a>
            <a href="rotuladora-tb-raa-cabine.html">TB-RAA c/ Cabine</a>
            <a href="rotuladora-master-label-bopp.html">Master Label BOPP</a>
            <a href="rotuladora-tb-rsa-1000.html">TB-RSA 1000</a>
          </nav>
        </div>
        <div class="footer-widget">
          <h4>Contato</h4>
          <div class="footer-contact-list">
            <div class="footer-contact-item"><i class="fas fa-map-marker-alt"></i><span>Rua Augusto Caprara, 382<br>Bairro Licorsul | CEP 95705-793</span></div>
            <div class="footer-contact-item"><i class="fas fa-phone"></i><a href="tel:+555436981050">+55 54 3698-1050</a></div>
            <div class="footer-contact-item"><i class="fab fa-whatsapp"></i><a href="https://wa.me/5554992425851?text=Ol%C3%A1!%20Gostaria%20de%20obter%20mais%20informa%C3%A7%C3%B5es%20sobre%20os%20produtos%20e%20servi%C3%A7os%20da%20TB%20M%C3%A1quinas." target="_blank" rel="noopener">+55 54 99242-5851</a></div>
            <div class="footer-contact-item" style="align-items:flex-start;"><i class="fas fa-envelope"></i><div style="display:flex;flex-direction:column;gap:2px;"><a href="mailto:tbmaquinas@tbmaquinas.com">tbmaquinas@tbmaquinas.com</a><a href="mailto:cassiano.comercial@tbmaquinas.com">cassiano.comercial@tbmaquinas.com</a></div></div>
            <div class="footer-contact-item"><i class="fas fa-clock"></i><span>07:30–11:30 | 13:30–17:00</span></div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container">
        <div class="footer-bottom-inner">
          <p class="footer-copyright">&copy; 2026 <strong>TB Máquinas</strong>. Todos os direitos reservados. | Desenvolvido por <a href="https://evolutor.com.br/" target="_blank" rel="noopener" style="font-family:'mbf-canno', sans-serif; color:var(--accent);">Evolutor</a></p>
        </div>
      </div>
    </div>
  </footer>

  <a href="https://wa.me/5554992425851?text=Ol%C3%A1!%20Gostaria%20de%20obter%20mais%20informa%C3%A7%C3%B5es%20sobre%20os%20produtos%20e%20servi%C3%A7os%20da%20TB%20M%C3%A1quinas." class="float-whatsapp" target="_blank" rel="noopener" aria-label="WhatsApp">
    <i class="fab fa-whatsapp"></i><span class="wa-tooltip">Fale conosco</span>
  </a>
  <button id="scroll-top" aria-label="Voltar ao topo"><i class="fas fa-chevron-up"></i></button>
  <script src="js/main.js"></script>'''

FOOTER_SUBDIR = '''  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" style="display:block;margin-bottom:24px;">
            <img src="images/produtos/cropped-logomarca.png" alt="TB Máquinas" style="max-height:90px;width:auto;object-fit:contain;">
          </a>
          <p class="footer-desc">Trabalhamos com inovação de alto nível e as tecnologias mais modernas de produção de rotuladoras e peças de reposição.</p>
          <div class="footer-social">
            <a href="https://www.instagram.com/tbmaquinas_equipamentos/" target="_blank" rel="noopener" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
            <a href="https://www.youtube.com/@TBMAQUINAS" target="_blank" rel="noopener" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
            <a href="https://wa.me/5554992425851?text=Ol%C3%A1!%20Gostaria%20de%20obter%20mais%20informa%C3%A7%C3%B5es%20sobre%20os%20produtos%20e%20servi%C3%A7os%20da%20TB%20M%C3%A1quinas." target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>
            <a href="mailto:tbmaquinas@tbmaquinas.com" aria-label="E-mail"><i class="fas fa-envelope"></i></a>
          </div>
        </div>
        <div class="footer-widget">
          <h4>Navegação</h4>
          <nav class="footer-links">
            <a href="index.html">Início</a>
            <a href="produtos.html">Produtos</a>
            <a href="servicos.html">Serviços</a>
            <a href="feiras.html">Feiras</a>
            <a href="sobre.html">Sobre</a>
            <a href="contato.html">Contato</a>
          </nav>
        </div>
        <div class="footer-widget">
          <h4>Produtos</h4>
          <nav class="footer-links">
            <a href="envolvedora-tb-evp-pre.html">Envolvedoras</a>
            <a href="mesa-acumulo-tb-ms.html">Mesas de Acúmulo</a>
            <a href="rotuladora-tb-raa.html">Rotuladora TB-RAA</a>
            <a href="rotuladora-tb-raa-cabine.html">TB-RAA c/ Cabine</a>
            <a href="rotuladora-master-label-bopp.html">Master Label BOPP</a>
            <a href="rotuladora-tb-rsa-1000.html">TB-RSA 1000</a>
          </nav>
        </div>
        <div class="footer-widget">
          <h4>Contato</h4>
          <div class="footer-contact-list">
            <div class="footer-contact-item"><i class="fas fa-map-marker-alt"></i><span>Rua Augusto Caprara, 382<br>Bairro Licorsul | CEP 95705-793</span></div>
            <div class="footer-contact-item"><i class="fas fa-phone"></i><a href="tel:+555436981050">+55 54 3698-1050</a></div>
            <div class="footer-contact-item"><i class="fab fa-whatsapp"></i><a href="https://wa.me/5554992425851?text=Ol%C3%A1!%20Gostaria%20de%20obter%20mais%20informa%C3%A7%C3%B5es%20sobre%20os%20produtos%20e%20servi%C3%A7os%20da%20TB%20M%C3%A1quinas." target="_blank" rel="noopener">+55 54 99242-5851</a></div>
            <div class="footer-contact-item" style="align-items:flex-start;"><i class="fas fa-envelope"></i><div style="display:flex;flex-direction:column;gap:2px;"><a href="mailto:tbmaquinas@tbmaquinas.com">tbmaquinas@tbmaquinas.com</a><a href="mailto:cassiano.comercial@tbmaquinas.com">cassiano.comercial@tbmaquinas.com</a></div></div>
            <div class="footer-contact-item"><i class="fas fa-clock"></i><span>07:30–11:30 | 13:30–17:00</span></div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container">
        <div class="footer-bottom-inner">
          <p class="footer-copyright">&copy; 2026 <strong>TB Máquinas</strong>. Todos os direitos reservados. | Desenvolvido por <a href="https://evolutor.com.br/" target="_blank" rel="noopener" style="font-family:'mbf-canno', sans-serif; color:var(--accent);">Evolutor</a></p>
        </div>
      </div>
    </div>
  </footer>

  <a href="https://wa.me/5554992425851?text=Ol%C3%A1!%20Gostaria%20de%20obter%20mais%20informa%C3%A7%C3%B5es%20sobre%20os%20produtos%20e%20servi%C3%A7os%20da%20TB%20M%C3%A1quinas." class="float-whatsapp" target="_blank" rel="noopener" aria-label="WhatsApp">
    <i class="fab fa-whatsapp"></i><span class="wa-tooltip">Fale conosco</span>
  </a>
  <button id="scroll-top" aria-label="Voltar ao topo"><i class="fas fa-chevron-up"></i></button>
  <script src="js/main.js"></script>'''

# ==============================================================
# 3. PROCESS ALL HTML FILES
# ==============================================================
html_files = [f for f in os.listdir(base) if f.endswith('.html')]

fixed_files = []
for fname in html_files:
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    original = html

    # Fix logo references: replace any old logomarca paths in footer with cropped-logomarca.png
    html = re.sub(
        r'(images/produtos/logo_topo_menor\.png|images/logomarca\.png)',
        'images/produtos/cropped-logomarca.png',
        html
    )

    # Fix footer logo specifically (ensure correct max-height and no distortion)
    html = re.sub(
        r'<img[^>]*src=["\']images/produtos/cropped-logomarca\.png["\'][^>]*>',
        '<img src="images/produtos/cropped-logomarca.png" alt="TB Máquinas" style="max-height:90px;width:auto;object-fit:contain;">',
        html
    )

    # Replace the entire footer block with our canonical footer
    # Match from <!-- FOOTER --> to </footer>
    html = re.sub(
        r'  <!-- FOOTER -->.*?</footer>',
        FOOTER.strip(),
        html,
        flags=re.DOTALL
    )

    # Replace float-whatsapp and scroll-top and script after </footer>
    # (already included in footer replacement above)
    # But clean up any duplicates that might be outside:
    html = re.sub(
        r'\n\s*<a href="https://wa\.me/[^"]*" class="float-whatsapp"[^>]*>.*?</a>\s*\n\s*<button id="scroll-top"[^>]*>.*?</button>\s*\n\s*<script src="js/main\.js"></script>',
        '',
        html,
        flags=re.DOTALL
    )

    # Fix the logo text color in header (color: var(--primary) -> color: var(--dark-text))
    html = html.replace(
        'color: var(--primary);\"',
        'color: var(--dark-text);\"'
    )

    # Fix .float-whatsapp inline background override — remove inline style that duplicates
    html = re.sub(r'(class="float-whatsapp"[^>]*) style="background:var\(--accent\);"', r'\1', html)
    html = re.sub(r'(class="float-whatsapp"[^>]*) style="[^"]*background[^"]*"', r'\1', html)

    # Fix btn-whatsapp inline style duplication in cta section
    html = re.sub(r'(class="btn btn-whatsapp"[^>]*) style="background:var\(--accent\);border-color:var\(--accent\);"', r'\1', html)

    if html != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        fixed_files.append(fname)

print(f"HTML files processed: {len(fixed_files)}")
for f in fixed_files:
    print(f"  - {f}")

# ==============================================================
# 4. VALIDATE CSS
# ==============================================================
with open(os.path.join(base, 'css', 'style.css'), 'r', encoding='utf-8') as f:
    css_content = f.read()
lines = css_content.count('\n')
opens = css_content.count('{')
closes = css_content.count('}')
print(f"\nCSS validation:")
print(f"  Lines: {lines}")
print(f"  Open braces: {opens}")
print(f"  Close braces: {closes}")
print(f"  Balanced: {opens == closes}")
print(f"  Bytes: {len(css_content.encode())}")
print("\nDone!")
