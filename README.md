# python-fastapi

- Use poetry to install dependencies
- Use the following commands to start server

  ```bash
  # Development mode with auto-reload
  uvicorn main:app --reload

  # Production mode with multiple workers
  uvicorn main:app --workers 5
  ```
