# 🎨 Sports Blog Theme Switcher Guide

## Available Themes

### 1. **Classic Theme** (Original)
- **Location**: `templates/blog/base.html` & `static/css/style.css`
- **Style**: Professional blue/indigo theme with sidebar layout
- **Colors**: #1a237e (indigo), white backgrounds, clean design

### 2. **Next Gen Theme** (New)
- **Location**: `templates/blog/new_theme_base.html` & `templates/blog/new_theme_home.html`
- **Style**: Modern dark theme with neon accents
- **Colors**: Black background, neon green (#39ff14), sports orange (#ff6b35)
- **Features**: 
  - Hero section
  - Grid/masonry layout
  - Sport-themed icons
  - Hover animations
  - Modern typography (Orbitron font)

## How to Switch Themes

### Option 1: Quick Switch (For Testing)
```bash
# Backup current theme
cp templates/blog/base.html templates/blog/base_backup.html
cp templates/blog/home.html templates/blog/home_backup.html

# Apply new theme
cp templates/blog/new_theme_base.html templates/blog/base.html
cp templates/blog/new_theme_home.html templates/blog/home.html

# Revert to original
cp templates/blog/base_backup.html templates/blog/base.html
cp templates/blog/home_backup.html templates/blog/home.html
```

### Option 2: Using Python Script
```bash
python switch_theme.py nextgen  # Switch to new theme
python switch_theme.py classic  # Switch back to original
```

### Option 3: URL-Based Switching
Add this to your views.py for dynamic switching:
```python
def get_template_names(self):
    theme = self.request.GET.get('theme', 'classic')
    if theme == 'nextgen':
        return ['blog/new_theme_home.html']
    return ['blog/home.html']
```

## Theme Comparison

| Feature | Classic | Next Gen |
|---------|---------|----------|
| Layout | Sidebar + Main | Full-width Grid |
| Colors | Blue/Indigo | Black + Neon |
| Typography | Segoe UI | Orbitron + Roboto |
| Style | Professional | Modern/Sporty |
| Animations | Basic | Advanced |

## Quick Start Commands

```bash
# Test new theme
python manage.py runserver
# Visit: http://localhost:8000

# Switch themes
python switch_theme.py nextgen
```

## Customization
- Edit CSS variables in new theme files
- Modify colors, fonts, and animations
- Add new themes by creating new template files
