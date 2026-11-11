# Mathematics API

A FastAPI application for adding two numbers.

## Setup (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

The server runs at http://127.0.0.1:8000. To change the host or port, edit the `uvicorn.run` call in `main.py`.

## Endpoints

- `POST /add` — accepts JSON `{"a":10,"b":20}` and returns `{"a":10.0,"b":20.0,"result":30.0}`.

Open http://127.0.0.1:8000/docs to try the endpoints interactively.

```powershell
Invoke-RestMethod -Method Post -Uri 'http://127.0.0.1:8000/add' -ContentType 'application/json' -Body '{"a":10,"b":20}'
```

Missing values, nonnumeric values, and nonfinite numbers return validation errors.

## Docker Compose

With Docker Desktop installed and running, execute these commands from this folder:

```powershell
docker compose up --build -d
docker compose ps
```

Open http://127.0.0.1:8123/docs to try POST `/add`, or run:

```powershell
Invoke-RestMethod -Method Post -Uri 'http://127.0.0.1:8123/add' -ContentType 'application/json' -Body '{"a":10,"b":20}'
```
The container runs Uvicorn on port 8123 without auto-reload. Rebuild after changing the code.

```powershell
docker compose logs -f api
docker compose down
```

## Docker without Compose

```powershell
docker build -t mathematics-api .
docker run --rm -p 127.0.0.1:8123:8123 mathematics-api
```

Use either Compose or the standalone container at a time so port 8123 is available.
