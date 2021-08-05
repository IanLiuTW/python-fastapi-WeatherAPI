# python-fastapi

## Use poetry to install dependencies

```python
poetry install
```

## Use the following commands to start server

```bash
# Development mode with auto-reload
uvicorn main:app --reload

# Production mode with multiple workers
uvicorn main:app --workers 5
```

## Check out the API response

- [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Check out the API docs (in Swagger UI)

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Check out the API docs (in ReDoc UI)

- [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
