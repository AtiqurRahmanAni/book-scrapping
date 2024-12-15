
# Project Title

A web crawler to crawl https://books.toscrape.com/ periodically and store all the information in database. 

## Features

- Periodically crawl all the books of the site.
- Update book information if changes
- Add new books if new books are added to the site.
- Backend for retrieving book information


## File Tree

```bash
backend/
├── .env.example
├── Dockerfile
├── main.py
├── requirements.txt
└── utils.py

bookscraper/
└── bookscraper/
    ├── spiders/
    │   ├── __init__.py
    │   └── bookspider.py
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    ├── Dockerfile
    ├── requirements.txt
    ├── run_spiders.py
    └── scrapy.cfg
├── .dockerignore
├── .gitignore
├── docker-compose.yml
└── requirements.txt
```
## Run Locally

Clone the project

```bash
  git clone https://github.com/AtiqurRahmanAni/book-scrapping.git
```

Go to the project directory

```bash
  cd book-scrapping
```

Create a new virtual environment (For windows)

```bash
  python -m venv venv
```

Activate the virtual environment (For windows)

```bash
  .\venv\Scripts\activate
```

Install dependencies

```bash
  pip install -r .\requirements.txt
```

To run the crawler

```bash
  cd bookscraper
  python .\run_spiders.py
```

To run the backend

```bash
  cd backend
  fastapi dev main.py
```

## Run in Docker Container

Go to the root directory and run

```bash
  docker compose up -d --build
```

To stop containers

```bash
  docker compose down
```
