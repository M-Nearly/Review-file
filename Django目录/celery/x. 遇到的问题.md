
- os windows
- celery 3.1.26
- redis 2.10.6

## 1.  pip install Celery

 > ImportError No module named pbr.pbr_json

`pip install --upgrade pbr`

## 2. Celery worker crashes 
> Unrecoverable error: AttributeError("'unicode' object has no attribute 'iteritems'",)
> 
```
Not a celery issue - Seems to be an issue with Redis 3.0.0.post1 installed via pip.

Solution: Roll back redis with pip: pip install redis==2.10.6

everything working again for me.
```