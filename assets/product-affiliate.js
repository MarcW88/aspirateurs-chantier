(() => {
  document.addEventListener('click', (event) => {
    const link = event.target.closest('a[data-affiliate-link="amazon"]');
    if (!link) return;
    const detail = {
      event: 'affiliate_click',
      provider: 'amazon',
      product_id: link.dataset.productKey || '',
      placement: link.dataset.placement || '',
      page_path: window.location.pathname,
      destination_host: (() => {
        try { return new URL(link.href).hostname; } catch { return ''; }
      })()
    };
    if (Array.isArray(window.dataLayer)) window.dataLayer.push(detail);
    window.dispatchEvent(new CustomEvent('affiliate:click', { detail }));
  }, { capture: true });
})();
