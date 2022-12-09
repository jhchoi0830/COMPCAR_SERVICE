# compcar_service

Backend requirements:
* python version : 3.9.13
* pip
* fastapi : 0.85.2
* uvicorn : 0.19.0
* motor : 3.1.1
* mongodb

# Install & Setup

### 1. Install required packages

```bash
pip install -r requirements.txt
```

### 2. Setting with venv

1. Virtual environment setup
```bash
py -3.9 -m venv venv

# if you have not setup alias, run:
python3 -m venv venv
```

2. Activate virtual environment
```bash
# for Windows
venv\Scripts\activate

# For Mac
source venv/bin/activate

# deactivate: 
deactivate
```

# Usage

### Start fastAPI server

```bash
uvicorn app.server:app --reload
```

### Run server with Docker

1. Build Docker: `docker build -t fastapi .`
2. Running container: `docker-compose up`

### API Document

* http://localhost:8000/docs
* http://localhost:8000/redoc

## Test

#### Run test cases
```bash
python -m pytest -v

# if you have not setup alias python3, run:
python3 -m pytest -v
```
