/* ============================================================
   toggle.js — Theme Toggle Component
   Requires: an element with id="themeToggleInput" (checkbox)
             an element with id="toggleLabel" (text label)
             <html data-theme="dark|light"> on the root element
   ============================================================ */

(function () {
    const STORAGE_KEY = 'pdffusion-theme';
    const DEFAULT     = 'dark';

    const html  = document.documentElement;
    const input = document.getElementById('themeToggleInput');
    const label = document.getElementById('toggleLabel');

    if (!input || !label) {
        console.warn('[toggle.js] Could not find #themeToggleInput or #toggleLabel in the DOM.');
        return;
    }

    /* ── Apply on first load ── */
    const saved = localStorage.getItem(STORAGE_KEY) || DEFAULT;
    applyTheme(saved);

    /* ── Listen for toggle ── */
    input.addEventListener('change', () => {
        const next = input.checked ? 'light' : 'dark';
        applyTheme(next);
        localStorage.setItem(STORAGE_KEY, next);
    });

    /* ── Helper ── */
    function applyTheme(theme) {
        html.setAttribute('data-theme', theme);
        input.checked      = (theme === 'light');
        label.textContent  = theme === 'light' ? 'Light' : 'Dark';
    }
})();
