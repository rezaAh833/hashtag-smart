// ==========================================
// API Configuration
// ==========================================
const API_URL = 'https://hashtag-smart-api.onrender.com';
// بعداً برای Render:
// const API_URL = 'https://hashtag-yar-api.onrender.com';

// ============ GLOBAL FUNCTIONS ============
function closeModal() {
  document.getElementById('comingSoonModal').classList.remove('active');
  // برگردون به فارسی
  document.getElementById('languageSelect').value = 'persian';
  location.reload(); // ریلود کن تا categories دوباره لود بشه
}

function showComingSoon() {
  document.getElementById('comingSoonModal').classList.add('active');
}

// ============ MAIN APPLICATION ============
(function () {
  // ============ DOM ELEMENTS ============
  const mainCatSelect = document.getElementById('mainCategorySelect');
  const subCatSelect = document.getElementById('subCategorySelect');
  const languageSelect = document.getElementById('languageSelect');
  const analyzeBtn = document.getElementById('analyzeBtn');
  const followerInput = document.getElementById('followerInput');
  const followerError = document.getElementById('followerError');
  const resultsContainer = document.getElementById('resultsContainer');
  const searchInput = document.getElementById('searchCategoryInput');
  const searchSuggestions = document.getElementById('searchSuggestions');

  let allCategories = [];
  let debounceTimer;
  let isSearchActive = false;

  // ============ API CALLS ============
  async function fetchCategories() {
    const lang = languageSelect.value;
    try {
      const response = await fetch(`${API_URL}/api/categories/?language=${lang === 'persian' ? 'fa' : 'en'}`);
      const data = await response.json();
      allCategories = data.categories;
      populateMainCategories();
    } catch (error) {
      console.error('Error loading categories:', error);
      mainCatSelect.innerHTML = '<option value="">خطا در بارگذاری</option>';
    }
  }

  async function fetchHashtags() {
    const lang = languageSelect.value;
    const category = mainCatSelect.value;
    const subcategory = subCatSelect.value;
    const followers = followerInput.value;

    const params = new URLSearchParams({
      language: lang === 'persian' ? 'fa' : 'en',
      category: category || '',
      subcategory: subcategory || '',
      followers: followers || '0'
    });

    try {
      const response = await fetch(`${API_URL}/api/hashtags/?${params.toString()}`);
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching hashtags:', error);
      return null;
    }
  }

  async function searchCategories(query) {
    const lang = languageSelect.value;
    try {
      const response = await fetch(
        `${API_URL}/api/search-categories/?q=${encodeURIComponent(query)}&language=${lang === 'persian' ? 'fa' : 'en'}`
      );
      const data = await response.json();
      return data.results;
    } catch (error) {
      console.error('Error searching:', error);
      return [];
    }
  }

  // ============ POPULATE CATEGORIES ============
  function populateMainCategories() {
    const lang = languageSelect.value;
    mainCatSelect.innerHTML = '<option value="">انتخاب کنید...</option>';

    allCategories.forEach(cat => {
      const option = document.createElement('option');
      option.value = cat.slug;
      option.textContent = cat.name;
      mainCatSelect.appendChild(option);
    });

    populateSubCategories();
  }

  function populateSubCategories() {
    const selectedSlug = mainCatSelect.value;
    subCatSelect.innerHTML = '<option value="">همه زیردسته‌ها</option>';

    const category = allCategories.find(c => c.slug === selectedSlug);
    if (category && category.subcategories) {
      category.subcategories.forEach(sub => {
        const option = document.createElement('option');
        option.value = sub.id;
        option.textContent = sub.name;
        subCatSelect.appendChild(option);
      });
    }
  }

  // ============ ERROR HANDLING ============
  function showError() {
    followerInput.classList.add('input-error');
    followerError.classList.add('show');
    followerInput.focus();
  }

  function hideError() {
    followerInput.classList.remove('input-error');
    followerError.classList.remove('show');
  }

  followerInput.addEventListener('input', function () {
    if (this.value.trim() !== '') {
      hideError();
    }
  });

  // ============ EVENT LISTENERS ============
  languageSelect.addEventListener('change', () => {
    if (languageSelect.value === 'english') {
      showComingSoon();
    } else {
      fetchCategories();
    }
  });

  mainCatSelect.addEventListener('change', () => {
    populateSubCategories();
  });

  // ============ RENDER RESULTS ============
  async function renderResults() {
    const followerValue = followerInput.value.trim();

    if (followerValue === '') {
      showError();
      return;
    }

    hideError();

    // Show loading
    resultsContainer.innerHTML = `
      <div class="card">
        <div class="loading-spinner">در حال تحلیل هشتگ‌ها...</div>
      </div>
    `;

    analyzeBtn.disabled = true;
    analyzeBtn.textContent = '⏳ در حال تحلیل...';

    const data = await fetchHashtags();

    analyzeBtn.disabled = false;
    analyzeBtn.textContent = '✨ تحلیل و پیشنهاد هشتگ';

    if (!data) {
      resultsContainer.innerHTML = `
        <div class="card">
          <div class="recommendation-message">❌ خطا در دریافت اطلاعات. لطفاً دوباره تلاش کنید.</div>
        </div>
      `;
      return;
    }

    const groupNames = {
      competitive: 'پررقابت 🚀',
      low_medium: 'کم‌رقابت و متوسط 🎯',
      specialized: 'تخصصی ⭐'
    };
    
    function createChips(tags) {
      if (!tags || tags.length === 0) {
        return '<p style="color: #94a3b8; font-size: 0.85rem;">هشتگی یافت نشد</p>';
      }
      return tags.map(t => `<span class="chip">${t}</span>`).join('');
    }

    function createGroupHTML(key, tags) {
      const isSpecial = key === 'specialized';
      return `
        <div class="group ${isSpecial ? 'special-recommendation' : ''}">
          <h3>
            ${isSpecial ? '<span class="highlight-badge">🏆 پیشنهاد ویژه</span>' : ''} 
            ${groupNames[key]}
          </h3>
          <div class="hashtag-chips">${createChips(tags)}</div>
          ${tags && tags.length > 0 ? `<button class="copy-btn" data-tags="${tags.join(',')}">📋 کپی هشتگ‌ها</button>` : ''}
        </div>
      `;
    }

    resultsContainer.innerHTML = `
      <div class="card">
        <div class="recommendation-message">💡 ${data.recommendation.message}</div>
        <div class="hashtag-groups">
          ${createGroupHTML('competitive', data.competitive)}
          ${createGroupHTML('low_medium', data.low_medium)}
          ${createGroupHTML('specialized', data.specialized)}
        </div>
      </div>
    `;

    // Add copy functionality
    document.querySelectorAll('.copy-btn').forEach(btn => {
      btn.addEventListener('click', function () {
        const tags = this.getAttribute('data-tags');
        navigator.clipboard.writeText(tags.replace(/,/g, ' ')).then(() => {
          this.textContent = '✅ کپی شد';
          setTimeout(() => { this.textContent = '📋 کپی هشتگ‌ها'; }, 2000);
        }).catch(() => {
          this.textContent = '❌ خطا';
          setTimeout(() => { this.textContent = '📋 کپی هشتگ‌ها'; }, 2000);
        });
      });
    });
  }

  analyzeBtn.addEventListener('click', renderResults);

  // ============ DARK MODE ============
  const darkBtn = document.getElementById('darkModeButton');
  darkBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark');
    darkBtn.innerHTML = document.body.classList.contains('dark') ? '☀️ حالت روشن' : '🌙 حالت تاریک';
  });

  // ============ SEARCH FUNCTIONALITY ============
  searchInput.addEventListener('input', function () {
    const query = this.value.trim().toLowerCase();

    clearTimeout(debounceTimer);

    if (query.length < 2) {
      searchSuggestions.style.display = 'none';
      if (query.length === 0 && isSearchActive) {
        isSearchActive = false;
        mainCatSelect.selectedIndex = 0;
        mainCatSelect.dispatchEvent(new Event('change'));
        subCatSelect.value = '';
        this.placeholder = 'جستجو کن یا از منوی زیر انتخاب کن...';
      }
      return;
    }

    searchSuggestions.innerHTML = `
      <div style="padding:1rem; text-align:center; color:#64748b;">
        ⏳ در حال جستجو...
      </div>
    `;
    searchSuggestions.style.display = 'block';

    debounceTimer = setTimeout(async () => {
      const results = await searchCategories(query);

      if (results.length > 0) {
        renderSearchResults(results);
        isSearchActive = true;
      } else {
        searchSuggestions.innerHTML = `
          <div style="padding:0.8rem 1rem; color:#94a3b8; font-size:0.85rem; text-align:center;">
            🔍 موردی یافت نشد
          </div>
        `;
      }
    }, 300);
  });

  function renderSearchResults(results) {
    searchSuggestions.innerHTML = '';

    results.forEach(result => {
      const item = document.createElement('div');
      item.style.cssText = `
        padding: 0.7rem 1rem;
        cursor: pointer;
        font-size: 0.9rem;
        transition: 0.15s;
        border-bottom: 1px solid #f1f5f9;
        display: flex;
        align-items: center;
        gap: 0.5rem;
      `;

      if (result.type === 'category') {
        item.innerHTML = `
          <span style="font-size:1.1rem;">📁</span>
          <span style="font-weight:600;">${result.name}</span>
          <span style="font-size:0.7rem; color:#7c3aed; background:#ede9fe; padding:0.15rem 0.5rem; border-radius:1rem; margin-right:auto;">دسته اصلی</span>
        `;
      } else {
        item.innerHTML = `
          <span style="font-size:1.1rem;">🏷️</span>
          <div style="flex:1;">
            <div style="font-weight:600;">${result.name}</div>
            <div style="font-size:0.75rem; color:#64748b;">در دسته ${result.category_name}</div>
          </div>
        `;
      }

      item.addEventListener('mouseover', () => {
        item.style.background = '#f1f5f9';
      });
      item.addEventListener('mouseout', () => {
        item.style.background = 'white';
      });

      item.addEventListener('mousedown', (e) => {
        e.preventDefault();
        selectSearchResult(result);
      });

      searchSuggestions.appendChild(item);
    });
  }

  function selectSearchResult(result) {
    mainCatSelect.value = result.slug;
    mainCatSelect.dispatchEvent(new Event('change'));

    if (result.subcategory_id) {
      setTimeout(() => {
        subCatSelect.value = result.subcategory_id;
      }, 100);
    } else {
      subCatSelect.value = '';
    }

    searchInput.value = result.name;
    searchSuggestions.style.display = 'none';
    isSearchActive = true;
  }

  // Close suggestions on click outside
  document.addEventListener('click', (e) => {
    if (!searchInput.contains(e.target) && !searchSuggestions.contains(e.target)) {
      searchSuggestions.style.display = 'none';
    }
  });

  // Clear on Escape
  searchInput.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      this.value = '';
      this.blur();
      searchSuggestions.style.display = 'none';
      isSearchActive = false;
      mainCatSelect.selectedIndex = 0;
      mainCatSelect.dispatchEvent(new Event('change'));
      subCatSelect.value = '';
    }
  });

  searchInput.addEventListener('focus', function () {
    if (isSearchActive) {
      this.select();
    }
  });

  searchInput.addEventListener('blur', function () {
    setTimeout(() => {
      if (this.value.trim() === '') {
        isSearchActive = false;
        this.placeholder = 'جستجو کن یا از منوی زیر انتخاب کن...';
        mainCatSelect.selectedIndex = 0;
        mainCatSelect.dispatchEvent(new Event('change'));
        subCatSelect.value = '';
      }
    }, 200);
  });

  // ============ INIT ============
  fetchCategories();
})();