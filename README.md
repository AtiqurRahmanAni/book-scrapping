[api-docs.json](https://github.com/user-attachments/files/18140631/api-docs.json)
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
    ├── .env.example
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
## Environment Variables

The project requires specific environment variables to be configured. Follow these steps to set up your environment:

### Backend Configuration
- Navigate to **/backend** directory
- Create a `.env` file and copy everything from `.env.example`
- Configure the following variables in your `.env`

```bash
MONGO_URI=your_mongodb_connection_string
MONGO_DATABASE=your_database_name
API_KEY=your_secret_api_key
```

### Web Crawler Configuration
- Navigate to **/bookscraper/bookscraper** directory
- Create a `.env` file and copy everything from `.env.example`
- Configure the following variables in your `.env`

```bash
MONGO_URI=your_mongodb_connection_string
MONGO_DATABASE=your_database_name
API_KEY=your_secret_api_key
```

Please ensure that the values for `MONGO_URI` and `MONGO_DATABASE` are identical in both `.env` files.


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
## API Reference

#### Get all books

```http
  GET /api/v1/books
```

| Query Params | Type     | Description                         |
| :----------- | :------- | :-------------------------------------------------------|
| `category`   | `string` | Category of books (Optional)                            |
| `price_min`  | `float`  | Minimum price of books (Optional)                       |
| `price_max`  | `float`  | Maxmum price of books (Optional)                        |
| `order`      | `string` | Order of books `asc` or `desc` default `asc` (Optional) |
| `order_by`   | `string` | Order of books by a field, default **rating** (Optional)|
| `page_no`    | `int`    | Page number, default **1** (Optional)                   |
| `page_size`  | `int`    | Number of items in one page, default **20**             |



| Authorization   | Type     | Description                                                |
| :-------------- | :------- | :--------------------------------------------------------- |
| `API-Key`       | `string` | **Required**. Your API key assigned in `API_KEY` in `.env` file |

#### Get book details

```http
  GET /api/v1/books/${upc}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `upc`     | `string` | **Required**. Id of book to fetch |

| Authorization   | Type     | Description                                                |
| :-------------- | :------- | :--------------------------------------------------------- |
| `API-Key`       | `string` | **Required**. Your API key assigned in `API_KEY` in `.env` file |

You can upload this [file](https://drive.google.com/file/d/1UJ5ae58IL9d1_7AOcxz_tvW3yXUoRYmc/view?usp=sharing) to postman
