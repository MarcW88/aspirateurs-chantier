#!/usr/bin/env python3
"""Apply the site-design-review decisions without splitting the visual source of truth.

The script is intentionally idempotent. It updates style.css, the main generator and
all currently rendered index.html files so the design can be reviewed immediately.
"""
from pathlib import Path
import re

BASE = Path(__file__).resolve().parent
START = "/* SITE DESIGN REVIEW V1 START */"
END = "/* SITE DESIGN REVIEW V1 END */"

DESIGN_CSS = r'''/* SITE DESIGN REVIEW V1 START */

/* Editorial technical direction — DESIGN.md is the reference. */
:root {
  --color-bg: #F5F3EE;
  --color-bg-alt: #EAE7E0;
  --color-bg-dark: #172029;
  --color-white: #FFFFFF;
  --color-text: #1B252C;
  --color-text-muted: #5D676D;
  --color-text-light: #7E8589;
  --color-primary: #25516B;
  --color-primary-dk: #193C52;
  --color-accent: #D36A2D;
  --color-accent-dk: #B6531F;
  --color-border: #D4D0C8;
  --color-border-dk: #BEB9B0;
  --font-display: 'Source Serif 4', Georgia, serif;
  --radius-sm: 3px;
  --radius-md: 6px;
  --radius-lg: 8px;
  --shadow-xs: 0 1px 2px rgba(23,32,41,0.04);
  --shadow-sm: 0 2px 7px rgba(23,32,41,0.06);
  --shadow-md: 0 8px 24px rgba(23,32,41,0.10);
  --header-h: 64px;
}

html { scroll-padding-top: calc(var(--header-h) + 20px); }
body {
  font-size: 16px;
  line-height: 1.7;
  background: var(--color-bg);
}
body.menu-open { overflow: hidden; }

a:focus-visible,
button:focus-visible {
  outline: 3px solid var(--color-accent);
  outline-offset: 3px;
}

.skip-link {
  position: fixed;
  top: 8px;
  left: 8px;
  z-index: 1000;
  padding: 10px 14px;
  background: var(--color-bg-dark);
  color: #fff;
  font-weight: 700;
  transform: translateY(-150%);
  transition: transform 0.15s ease;
}
.skip-link:focus { transform: translateY(0); }

h1, h2, h3 {
  font-family: var(--font-display);
  font-weight: 650;
  letter-spacing: -0.025em;
}
h4, h5 { font-family: var(--font-sans); }
h1 { font-size: clamp(2rem, 4vw, 3.15rem); }
h2 { font-size: clamp(1.55rem, 2.7vw, 2.15rem); }
h3 { font-size: clamp(1.18rem, 1.8vw, 1.45rem); }
p { font-size: 1rem; line-height: 1.75; }
.lead { font-size: clamp(1.05rem, 1.4vw, 1.17rem); line-height: 1.72; }

.site-header {
  background: rgba(245,243,238,0.98);
  box-shadow: none;
}
.header-inner { gap: 28px; }
.logo-line1 { font-size: 0.94rem; }
.logo-line2 { color: var(--color-accent); }
.nav-link { color: var(--color-text); font-size: 0.84rem; }
.nav-item:hover > .nav-link,
.nav-item:focus-within > .nav-link {
  color: var(--color-primary);
  background: transparent;
}
.nav-item:hover > .dropdown,
.nav-item:focus-within > .dropdown {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}
.dropdown { border-radius: var(--radius-sm); padding: 8px; }
.dropdown a { border-radius: 2px; }
.header-cta { border-radius: 3px; padding: 9px 15px; }

.btn { border-radius: 3px; }
.btn-outline { background: rgba(255,255,255,0.35); }

.hero {
  background: var(--color-bg);
  padding: 72px 0 62px;
}
.hero-inner {
  grid-template-columns: minmax(0, 1fr) 390px;
  gap: 72px;
}
.hero-title { max-width: 760px; }
.hero-desc { max-width: 720px; }
.hero-eyebrow {
  background: transparent;
  border: 0;
  border-left: 3px solid var(--color-accent);
  border-radius: 0;
  padding: 2px 0 2px 10px;
  color: var(--color-text-muted);
}
.hero-stats {
  background: transparent;
  border: 0;
  border-top: 2px solid var(--color-text);
  border-bottom: 1px solid var(--color-border-dk);
  border-radius: 0;
  padding: 0;
}
.hero-stat-header { padding: 12px 0 10px; }
.hero-stat-row { padding: 11px 0; }
.stat-bar-wrap { display: none; }
.stat-label { font-size: 0.86rem; }
.stat-value { font-size: 0.82rem; text-align: right; }

.section { padding: 72px 0; }
.section-head { margin-bottom: 30px; }
.section-head .eyebrow {
  color: var(--color-accent-dk);
  font-size: 0.68rem;
}
.section-head p { max-width: 720px; font-size: 0.95rem; }
.section-head--center { text-align: left; margin-left: 0; margin-right: 0; max-width: 720px; }

/* Avoid turning every homepage section into the same card grid. */
.usage-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0 36px;
  border-bottom: 1px solid var(--color-border);
}
.usage-card {
  display: grid;
  grid-template-columns: 42px minmax(0, 1fr);
  grid-template-rows: auto auto;
  column-gap: 14px;
  row-gap: 2px;
  background: transparent;
  border: 0;
  border-top: 1px solid var(--color-border);
  border-radius: 0;
  padding: 18px 0;
  box-shadow: none;
}
.usage-card:hover { border-color: var(--color-border-dk); box-shadow: none; }
.usage-card-icon {
  grid-row: 1 / 3;
  width: 38px;
  height: 38px;
  border: 1px solid var(--color-border);
  border-radius: 3px;
  background: rgba(255,255,255,0.42);
}
.usage-card h3 { grid-column: 2; font-family: var(--font-sans); font-size: 0.94rem; }
.usage-card p { grid-column: 2; font-size: 0.84rem; }

.guide-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0 36px;
  border-bottom: 1px solid var(--color-border);
}
.guide-card {
  background: transparent;
  border: 0;
  border-top: 1px solid var(--color-border);
  border-radius: 0;
  padding: 18px 0;
}
.guide-card:hover { border-color: var(--color-border-dk); }
.guide-card .guide-q { font-size: 0.94rem; }
.guide-card .guide-arrow { color: var(--color-accent-dk); }

.brand-grid {
  gap: 0 24px;
  border-bottom: 1px solid var(--color-border);
}
.brand-card {
  background: transparent;
  border: 0;
  border-top: 1px solid var(--color-border);
  border-radius: 0;
  padding: 18px 0;
}
.brand-card:hover { border-color: var(--color-border-dk); }
.brand-tier { color: var(--color-accent-dk); }

.hub-grid { gap: 0 28px; }
.hub-link {
  background: transparent;
  border: 0;
  border-bottom: 1px solid var(--color-border);
  border-radius: 0;
  padding: 16px 2px;
}
.hub-link:hover {
  border-color: var(--color-border-dk);
  background: transparent;
  color: var(--color-primary);
}

.product-card {
  border-radius: 4px;
  box-shadow: none;
}
.product-card:hover { box-shadow: var(--shadow-xs); }
.product-card-top,
.product-card-img { background: #EFEEE9; }

.page-hero {
  background: var(--color-bg);
  padding: 46px 0 38px;
}
.page-hero h1 { max-width: 940px; }
.page-hero .lead { max-width: 820px; }
.ctype {
  background: transparent !important;
  color: var(--color-primary) !important;
  border-left: 3px solid var(--color-accent);
  border-radius: 0;
  padding: 1px 0 1px 8px;
}
.meta-tag {
  padding: 0;
  background: transparent;
  border: 0;
  border-radius: 0;
  color: var(--color-text-light);
}

.content-layout {
  grid-template-columns: minmax(0, 760px) 280px;
  justify-content: space-between;
  gap: 56px;
  padding: 52px 0 88px;
}
.content-main { max-width: 760px; }
.content-main h2 {
  margin: 48px 0 15px;
  padding-top: 6px;
}
.content-main h3 { margin: 30px 0 10px; }
.content-main p { margin-bottom: 17px; }
.content-main ul,
.content-main ol { margin: 0 0 20px; }
.content-main ul li,
.content-main ol li { font-size: 0.97rem; line-height: 1.65; padding: 4px 0; }
.content-main p a,
.content-main li a {
  color: var(--color-primary);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 3px;
}
.content-main p a:hover,
.content-main li a:hover { color: var(--color-primary-dk); }
.content-main small { color: var(--color-text-muted); line-height: 1.6; }

.answer-box {
  background: #F0ECE4;
  border: 1px solid #DDD5C8;
  border-left: 4px solid var(--color-accent);
  border-radius: 0;
  padding: 20px 22px;
  margin: 8px 0 34px;
}
.answer-box p { font-size: 1rem; line-height: 1.7; }
.answer-box strong { color: var(--color-text); }

.content-sidebar { gap: 14px; }
.sidebar-box { border-radius: 3px; }
.sidebar-box-head {
  background: transparent;
  border-bottom: 1px solid var(--color-border);
  color: var(--color-text);
}
.toc-list a { font-size: 0.81rem; border-radius: 0; }
.toc-list a:hover,
.toc-list a:focus-visible {
  background: transparent;
  border-color: var(--color-accent);
}
.affil-note { font-size: 0.76rem; }

.related-box {
  background: transparent;
  border: 0;
  border-top: 1px solid var(--color-border-dk);
  border-bottom: 1px solid var(--color-border);
  border-radius: 0;
  padding: 18px 0;
  margin: 36px 0 10px;
}
.related-links { display: grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap: 5px 24px; }
.related-links a { font-size: 0.84rem; color: var(--color-primary); }

/* Generated comparison and brand tables. */
.content-main .table-wrap {
  width: 100%;
  overflow-x: auto;
  margin: 22px 0 30px;
  border: 1px solid var(--color-border);
  border-radius: 3px;
  background: var(--color-white);
  scrollbar-width: thin;
  scrollbar-color: var(--color-border-dk) transparent;
}
.content-main .table-wrap table {
  width: 100%;
  min-width: 680px;
  border-collapse: collapse;
  font-size: 0.88rem;
}
.content-main .table-wrap th {
  background: var(--color-bg-dark);
  color: rgba(255,255,255,0.88);
  padding: 12px 14px;
  text-align: left;
  font-family: var(--font-sans);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.02em;
  vertical-align: bottom;
}
.content-main .table-wrap td {
  padding: 13px 14px;
  border-bottom: 1px solid var(--color-border);
  vertical-align: top;
  line-height: 1.55;
}
.content-main .table-wrap tbody tr:last-child td { border-bottom: 0; }
.content-main .table-wrap tbody tr:nth-child(even) td { background: #FAF9F6; }
.content-main .table-wrap td:first-child { min-width: 190px; }
.content-main .table-wrap code {
  font-family: var(--font-mono);
  font-size: 0.74rem;
  color: var(--color-primary-dk);
  background: #EEF0EC;
  border: 1px solid #DADDD5;
  padding: 2px 5px;
  border-radius: 2px;
}

.data-table-wrap { border-radius: 3px; }
.data-table thead th { background: var(--color-bg-dark); }
.verdict-pill { border-radius: 2px; background: var(--color-primary); }

.content-main h2#sources + p + ul {
  background: #EFEEE9;
  border-left: 3px solid var(--color-primary);
  padding: 15px 18px 15px 34px;
}

.site-footer { background: var(--color-bg-dark); }
.footer-brand .logo-line2 { color: var(--color-accent); }
.footer-tagline { color: rgba(255,255,255,0.55); }
.footer-col a { color: rgba(255,255,255,0.62); }
.footer-bottom { color: rgba(255,255,255,0.42); }
.footer-bottom a { color: rgba(255,255,255,0.52); }

@media (max-width: 1024px) {
  .hero-inner { grid-template-columns: 1fr; gap: 44px; }
  .hero-stats { max-width: 680px; }
  .content-layout { grid-template-columns: 1fr; gap: 34px; }
  .content-main { max-width: 800px; }
  .content-sidebar { max-width: 800px; }
}

@media (max-width: 768px) {
  .site-header { min-height: var(--header-h); height: var(--header-h); }
  .header-inner { position: relative; padding: 0 18px; }
  .burger {
    display: flex;
    min-width: 44px;
    min-height: 44px;
    align-items: center;
    justify-content: center;
  }
  .burger span { transition: transform 0.15s ease, opacity 0.15s ease; }
  .burger[aria-expanded="true"] span:first-child { transform: translateY(6px) rotate(45deg); }
  .burger[aria-expanded="true"] span:nth-child(2) { opacity: 0; }
  .burger[aria-expanded="true"] span:last-child { transform: translateY(-6px) rotate(-45deg); }
  .site-nav {
    display: none;
    position: fixed;
    top: var(--header-h);
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 190;
    overflow-y: auto;
    flex-direction: column;
    align-items: stretch;
    gap: 0;
    padding: 12px 18px 32px;
    background: var(--color-bg);
    border-top: 1px solid var(--color-border);
  }
  .site-nav.is-open { display: flex; }
  .nav-item { width: 100%; border-bottom: 1px solid var(--color-border); }
  .nav-link {
    width: 100%;
    justify-content: space-between;
    padding: 14px 2px 10px;
    font-size: 0.98rem;
  }
  .nav-link .chev { display: none; }
  .dropdown {
    position: static;
    min-width: 0;
    width: 100%;
    opacity: 1;
    visibility: visible;
    transform: none;
    box-shadow: none;
    border: 0;
    background: transparent;
    padding: 0 0 10px 12px;
  }
  .dropdown a { padding: 7px 2px; font-size: 0.86rem; }
  .dd-label { padding-left: 2px; }
  .header-cta { display: none; }

  .container { padding-left: 18px; padding-right: 18px; }
  .hero { padding: 52px 0 46px; }
  .hero-actions .btn { width: 100%; justify-content: center; }
  .section { padding: 52px 0; }
  .usage-grid,
  .guide-grid { grid-template-columns: 1fr; gap: 0; }
  .brand-grid { grid-template-columns: repeat(2, minmax(0,1fr)); gap: 0 20px; }
  .page-hero { padding: 36px 0 30px; }
  .content-layout { padding: 34px 0 64px; }
  .content-main h2 { margin-top: 40px; }
  .content-main .table-wrap { margin-left: -2px; margin-right: -2px; }
  .content-main .table-wrap table { min-width: 620px; font-size: 0.84rem; }
  .related-links { grid-template-columns: 1fr; }
  .footer-main { padding-top: 42px; }
}

@media (max-width: 540px) {
  .brand-grid { grid-template-columns: 1fr; }
  .hero-stat-row { align-items: flex-start; }
  .stat-value { max-width: 45%; }
}

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after {
    scroll-behavior: auto !important;
    transition-duration: 0.01ms !important;
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
  }
}

/* SITE DESIGN REVIEW V1 END */'''


def replace_design_block(css: str) -> str:
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    css = pattern.sub("", css).rstrip() + "\n\n"
    return css + DESIGN_CSS + "\n"


def update_generator() -> None:
    path = BASE / "_generate.py"
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap",
        "family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Source+Serif+4:opsz,wght@8..60,500;8..60,600;8..60,700&display=swap",
    )
    text = text.replace('<nav class="site-nav">', '<nav class="site-nav" id="site-navigation" aria-label="Navigation principale">')
    text = text.replace(
        '<button class="burger" aria-label="Menu"><span></span><span></span><span></span></button>',
        '<button class="burger" type="button" aria-label="Ouvrir le menu" aria-controls="site-navigation" aria-expanded="false"><span></span><span></span><span></span></button>',
    )
    text = text.replace(
        '<body>\n{HEADER_HTML}\n<main>',
        '<body>\n<a class="skip-link" href="#main-content">Aller au contenu</a>\n{HEADER_HTML}\n<main id="main-content">',
    )
    text = text.replace(
        '{FOOTER_HTML}\n</body>',
        '{FOOTER_HTML}\n<script src="/site.js" defer></script>\n</body>',
    )
    text = text.replace('© 2025 aspirateurs-chantier.fr', '© 2026 aspirateurs-chantier.fr')
    text = text.replace('#1B4FD8', '#25516B').replace('#E05E1A', '#D36A2D')
    text = text.replace(
        'Base de données spécialisée — Tests &amp; comparatifs indépendants',
        'Média technique spécialisé — Comparatifs documentés',
    )
    text = text.replace(
        'Tests approfondis, fiches techniques normalisées et comparatifs indépendants. Pour choisir le bon aspirateur selon le chantier, pas selon la commission.',
        'Comparatifs documentés, fiches techniques normalisées et guides pratiques. Pour choisir selon le chantier, la poussière et l’usage réel — pas selon la commission.',
    )
    path.write_text(text, encoding="utf-8")


def update_html(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    text = text.replace('<nav class="site-nav">', '<nav class="site-nav" id="site-navigation" aria-label="Navigation principale">')
    text = text.replace(
        '<button class="burger" aria-label="Menu"><span></span><span></span><span></span></button>',
        '<button class="burger" type="button" aria-label="Ouvrir le menu" aria-controls="site-navigation" aria-expanded="false"><span></span><span></span><span></span></button>',
    )
    if 'class="skip-link"' not in text:
        text = text.replace('<body>', '<body>\n<a class="skip-link" href="#main-content">Aller au contenu</a>', 1)
    text = text.replace('<main>', '<main id="main-content">', 1)
    if '/site.js' not in text:
        text = text.replace('</body>', '<script src="/site.js" defer></script>\n</body>', 1)
    text = text.replace('© 2025 aspirateurs-chantier.fr', '© 2026 aspirateurs-chantier.fr')
    text = text.replace('#1B4FD8', '#25516B').replace('#E05E1A', '#D36A2D')
    text = text.replace(
        'Base de données spécialisée — Tests &amp; comparatifs indépendants',
        'Média technique spécialisé — Comparatifs documentés',
    )
    text = text.replace(
        'Tests approfondis, fiches techniques normalisées et comparatifs indépendants. Pour choisir le bon aspirateur selon le chantier, pas selon la commission.',
        'Comparatifs documentés, fiches techniques normalisées et guides pratiques. Pour choisir selon le chantier, la poussière et l’usage réel — pas selon la commission.',
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    style = BASE / "style.css"
    css = style.read_text(encoding="utf-8")
    css = css.replace(
        "family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap",
        "family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Source+Serif+4:opsz,wght@8..60,500;8..60,600;8..60,700&display=swap",
    )
    style.write_text(replace_design_block(css), encoding="utf-8")

    update_generator()
    for html in BASE.rglob("index.html"):
        update_html(html)

    print("Applied site-design-review system to style.css, generator and rendered pages.")


if __name__ == "__main__":
    main()
