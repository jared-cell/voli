// dashboard.js - controla menú hamburguesa y toggle de tema (light/dark)
document.addEventListener('DOMContentLoaded', function(){
  const btn = document.getElementById('btn-hamburger');
  const sidebar = document.getElementById('sidebar');
  if(btn && sidebar){
    btn.addEventListener('click', ()=> sidebar.classList.toggle('open'));
  }

  const themeToggle = document.getElementById('theme-toggle');
  const root = document.documentElement;
  const preferred = localStorage.getItem('voley_theme') || 'light';
  if(preferred === 'dark') root.setAttribute('data-theme','dark');
  if(themeToggle){
    themeToggle.addEventListener('click', ()=>{
      const now = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', now);
      localStorage.setItem('voley_theme', now);
      themeToggle.setAttribute('aria-pressed', now === 'dark');
      themeToggle.textContent = now === 'dark' ? '☀️' : '🌙';
    });
  }
  // Logout modal control
  const btnLogout = document.getElementById('btn-logout');
  const logoutModal = document.getElementById('logout-modal');
  const cancelLogout = document.getElementById('cancel-logout');
  const confirmLogout = document.getElementById('confirm-logout');
  const logoutForm = document.getElementById('logout-form');
  if(btnLogout && logoutModal){
    btnLogout.addEventListener('click', ()=>{
      logoutModal.setAttribute('aria-hidden','false');
      logoutModal.classList.add('open');
    });
  }
  if(cancelLogout){
    cancelLogout.addEventListener('click', ()=>{
      logoutModal.setAttribute('aria-hidden','true');
      logoutModal.classList.remove('open');
    });
  }
  if(confirmLogout && logoutForm){
    confirmLogout.addEventListener('click', ()=>{
      // submit the form as POST
      logoutForm.querySelector('button[type="submit"]')?.click();
      // if submit button isn't present, submit the form directly
      logoutForm.submit();
    });
  }
});
document.addEventListener('DOMContentLoaded', function(){
  const btn = document.getElementById('btn-hamburger');
  const sidebar = document.getElementById('sidebar');
  if(btn && sidebar){
    btn.addEventListener('click', ()=>{
      sidebar.classList.toggle('open');
    })
  }
});
