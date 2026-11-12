(() => {
  const button = document.querySelector('.menu-toggle');
  const nav = document.getElementById('site-nav');
  if (!button || !nav) return;
  document.body.classList.add('js-ready');
  button.addEventListener('click', () => {
    const expanded = button.getAttribute('aria-expanded') === 'true';
    button.setAttribute('aria-expanded', String(!expanded));
    nav.classList.toggle('open', !expanded);
    button.querySelector('.menu-label').textContent = expanded ? 'Menu' : 'Close';
  });
  nav.addEventListener('click', event => {
    if (event.target.closest('a')) {
      button.setAttribute('aria-expanded', 'false');
      nav.classList.remove('open');
      button.querySelector('.menu-label').textContent = 'Menu';
    }
  });
})();
