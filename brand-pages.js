(() => {
  const body = document.body;
  if (!body.classList.contains('brand-page')) return;

  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.site-nav');

  if (burger && nav) {
    if (!nav.id) nav.id = 'brand-site-nav';
    burger.setAttribute('aria-controls', nav.id);
    burger.setAttribute('aria-expanded', 'false');

    const setOpen = open => {
      body.classList.toggle('nav-open', open);
      burger.setAttribute('aria-expanded', String(open));
      if (open) {
        requestAnimationFrame(() => nav.querySelector('a[href]')?.focus());
      } else {
        burger.focus();
      }
    };

    burger.addEventListener('click', () => {
      setOpen(!body.classList.contains('nav-open'));
    });

    nav.addEventListener('click', event => {
      if (event.target.closest('a[href]') && window.matchMedia('(max-width: 768px)').matches) {
        setOpen(false);
      }
    });

    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && body.classList.contains('nav-open')) {
        setOpen(false);
      }
    });

    window.matchMedia('(min-width: 769px)').addEventListener('change', event => {
      if (event.matches && body.classList.contains('nav-open')) setOpen(false);
    });
  }

  const layout = document.querySelector('.content-layout');
  const article = document.querySelector('.content-main');
  const sidebar = document.querySelector('.content-sidebar');
  const tocBox = sidebar?.querySelector('.sidebar-box:first-child');
  const tocHead = tocBox?.querySelector('.sidebar-box-head');
  const tocBody = tocBox?.querySelector('.sidebar-box-body');
  const mobileQuery = window.matchMedia('(max-width: 1024px)');

  if (layout && article && sidebar && tocBox && tocHead && tocBody) {
    const collapse = collapsed => {
      tocBody.hidden = collapsed;
      tocHead.setAttribute('aria-expanded', String(!collapsed));
    };

    const toggleToc = () => {
      if (!mobileQuery.matches) return;
      collapse(!tocBody.hidden);
    };

    tocHead.addEventListener('click', toggleToc);
    tocHead.addEventListener('keydown', event => {
      if (!mobileQuery.matches) return;
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        toggleToc();
      }
    });

    const syncToc = () => {
      if (mobileQuery.matches) {
        tocBox.classList.add('mobile-toc-box');
        layout.insertBefore(tocBox, article);
        tocHead.setAttribute('role', 'button');
        tocHead.setAttribute('tabindex', '0');
        collapse(true);
      } else {
        tocBox.classList.remove('mobile-toc-box');
        sidebar.insertBefore(tocBox, sidebar.firstChild);
        tocHead.removeAttribute('role');
        tocHead.removeAttribute('tabindex');
        tocHead.removeAttribute('aria-expanded');
        tocBody.hidden = false;
      }
    };

    syncToc();
    mobileQuery.addEventListener('change', syncToc);
  }
})();
