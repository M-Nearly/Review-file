```python
import os
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled15.settings")
    import django
    django.setup()

    from app01 import models

    books = models.Book.objects.all()
    print(books)
```

