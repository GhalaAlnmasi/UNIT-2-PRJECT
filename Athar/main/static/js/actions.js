document.addEventListener('DOMContentLoaded', () => {
  const langBtn = document.getElementById('lang-toggle');

    if(langBtn){
        langBtn.addEventListener('click', (e) => {
            e.preventDefault(); 
            
            const cookies = document.cookie.split(';').reduce((acc, c) => {
                const [key, value] = c.trim().split('=');
                acc[key] = value;
                return acc;
            }, {});
            const currentLang = cookies['django_language'] || 'ar';
            const nextLang = currentLang === 'en' ? 'ar' : 'en';

            // تحويل للـ URL الجديد بعد تأخير بسيط
            setTimeout(() => {
                window.location.href = `/set-language/${nextLang}/?HTTP_REFERER=${encodeURIComponent(window.location.href)}`;
            }, 150); // تأخير 0.15 ثانية
        });
    }


const themeBtn = document.getElementById('theme-toggle');
if(themeBtn){
  themeBtn.addEventListener('click', () => {
    const icon = themeBtn.querySelector('.material-icons');
    const mode = icon.textContent.trim() === 'dark_mode' ? 'light' : 'dark';
    window.location.href = `/set-theme/${mode}/?HTTP_REFERER=${encodeURIComponent(window.location.href)}`;
  });
}

});

// Dropdown Regions
document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('regions-btn');
  const menu = document.getElementById('regions-menu');
  const arrow = document.getElementById('arrow');
  let isOpen = false;

  
  btn.addEventListener('click', (e) => {
    e.stopPropagation();
    isOpen = !isOpen;

    if (isOpen) {
      menu.classList.remove('opacity-0', 'invisible', 'scale-95');
      menu.classList.add('opacity-100', 'visible', 'scale-100');
      arrow.classList.add('rotate-180');
    } else {
      menu.classList.add('opacity-0', 'invisible', 'scale-95');
      menu.classList.remove('opacity-100', 'visible', 'scale-100');
      arrow.classList.remove('rotate-180');
    }
  });

  
  document.addEventListener('click', (e) => {
    if (isOpen && !btn.contains(e.target) && !menu.contains(e.target)) {
      isOpen = false;
      menu.classList.add('opacity-0', 'invisible', 'scale-95');
      menu.classList.remove('opacity-100', 'visible', 'scale-100');
      arrow.classList.remove('rotate-180');
    }
  });
});


// Toggle mobile menu
document.addEventListener('DOMContentLoaded', () => {
  const menuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');

  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
    });

    document.addEventListener('click', (e) => {
      if (!menuBtn.contains(e.target) && !mobileMenu.contains(e.target)) {
        mobileMenu.classList.add('hidden');
      }
    });
  }
});


// Map link
document.addEventListener('DOMContentLoaded', () => {
  const mapObject = document.getElementById('saudi-map');
  const links = document.querySelectorAll('#map-links a');

  mapObject.addEventListener('load', () => {
    const svgDoc = mapObject.contentDocument;
    console.log("✅ SVG Loaded:", svgDoc);

    links.forEach(link => {
      const regionId = link.dataset.region;
      const href = link.getAttribute('href');
      const regionElement = svgDoc.getElementById(regionId);

      if (regionElement) {
        console.log(`Linked region: ${regionId} → ${href}`);
        regionElement.style.cursor = 'pointer';
        regionElement.addEventListener('click', () => window.location.href = href);
      } else {
        console.warn(`❌ Region not found in SVG: ${regionId}`);
      }
    });
  });
});



