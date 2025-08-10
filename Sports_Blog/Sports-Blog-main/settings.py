TEMPLATES = [
    {
        # ... existing code ...
        'OPTIONS': {
            'context_processors': [
                # ... existing code ...
                'blog.context_processors.categories_processor',
            ],
        },
    },
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'