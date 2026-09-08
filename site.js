(() => {
  const header = document.querySelector('.site-header');
  const nav = document.getElementById('site-navigation');
  const burger = document.querySelector('.burger');

  if (!header || !nav || !burger) return;

  const closeMenu = () => {
    nav.classList.remove('is-open');
    burger.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('menu-open');
  };

  const openMenu = () => {
    nav.classList.add('is-open');
    burger.setAttribute('aria-expanded', 'true');
    document.body.classList.add('menu-open');
  };

  burger.addEventListener('click', () => {
    const expanded = burger.getAttribute('aria-expanded') === 'true';
    expanded ? closeMenu() : openMenu();
  });

  nav.addEventListener('click', (event) => {
    if (event.target.closest('a') && window.matchMedia('(max-width: 768px)').matches) {
      closeMenu();
    }
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && nav.classList.contains('is-open')) {
      closeMenu();
      burger.focus();
    }
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 768) closeMenu();
  });
})();
