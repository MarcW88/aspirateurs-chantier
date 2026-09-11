(() => {
  const body = document.body;
  if (!body.classList.contains('design-v2')) return;

  const mobile = window.matchMedia('(max-width: 768px)');
  const articleLayout = window.matchMedia('(max-width: 1024px)');
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.site-nav');

  if (burger && nav && !body.classList.contains('comparison-page')) {
    if (!nav.id) nav.id = 'site-nav-v2';
    burger.setAttribute('aria-controls', nav.id);
    burger.setAttribute('aria-expanded', 'false');

    const setOpen = open => {
      body.classList.toggle('nav-open', open);
      burger.setAttribute('aria-expanded', String(open));
      if (open) requestAnimationFrame(() => nav.querySelector('a[href]')?.focus());
      else burger.focus();
    };

    burger.addEventListener('click', () => setOpen(!body.classList.contains('nav-open')));
    nav.addEventListener('click', event => {
      if (event.target.closest('a[href]') && mobile.matches) setOpen(false);
    });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && body.classList.contains('nav-open')) setOpen(false);
    });
    mobile.addEventListener('change', event => {
      if (!event.matches && body.classList.contains('nav-open')) setOpen(false);
    });
  }

  /* Guide/model pages: move the real TOC before the article on smaller screens. */
  if (!body.classList.contains('comparison-page')) {
    const layout = document.querySelector('.content-layout');
    const article = document.querySelector('.content-main');
    const sidebar = document.querySelector('.content-sidebar');
    const tocBox = sidebar?.querySelector('.sidebar-box');
    const tocHead = tocBox?.querySelector('.sidebar-box-head');
    const tocBody = tocBox?.querySelector('.sidebar-box-body');

    if (layout && article && sidebar && tocBox && tocHead && tocBody) {
      const collapse = collapsed => {
        tocBody.hidden = collapsed;
        tocHead.setAttribute('aria-expanded', String(!collapsed));
      };

      const toggle = () => {
        if (!articleLayout.matches) return;
        collapse(!tocBody.hidden);
      };

      tocHead.addEventListener('click', toggle);
      tocHead.addEventListener('keydown', event => {
        if (!articleLayout.matches || !['Enter', ' '].includes(event.key)) return;
        event.preventDefault();
        toggle();
      });

      const sync = () => {
        if (articleLayout.matches) {
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

      sync();
      articleLayout.addEventListener('change', sync);
    }
  }
})();
