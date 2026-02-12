# Azure Datacenters API

FastAPI backend service that provides datacenter location data for the Azure Datacenters globe visualization.

## Features

- GET `/datacenters` endpoint returning JSON list of Azure datacenters
- PostgreSQL database integration with environment-based configuration
- CORS enabled for frontend integration
- Health check endpoint
- Comprehensive API tests

## Prerequisites

- Python 3.8 or higher
- PostgreSQL database (running locally or in a container)
- pip or pipenv for dependency management

## Setup

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```

2. **Configure environment variables:**

Copy the example environment file and update with your database credentials:

```bash
cp .env.example .env
```

Edit `.env` with your PostgreSQL settings:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=az_dc_db
DB_USER=postgres
DB_PASSWORD=postgres
```

3. **Ensure PostgreSQL database is running:**

Make sure your PostgreSQL database is accessible and contains the `datacenters` table with the schema:

```sql
CREATE TABLE datacenters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL
);
```

## Running the Application

### Development Server

Run the application on port 8000:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Or using Python directly:

```bash
python main.py
```

The API will be available at:
- Root: http://localhost:8000/
- Datacenters endpoint: http://localhost:8000/datacenters
- API docs: http://localhost:8000/docs
- Health check: http://localhost:8000/health

### Production

For production, run without the `--reload` flag:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

### GET /datacenters

Returns a JSON array of datacenter objects.

**Response:**

```json
[
  {
    "id": 1,
    "name": "East US",
    "country": "United States",
    "city": "Virginia"
  },
  {
    "id": 2,
    "name": "West Europe",
    "country": "Netherlands",
    "city": "Amsterdam"
  }
]
```

**Status Codes:**
- `200 OK`: Successful response
- `503 Service Unavailable`: Database connection error
- `500 Internal Server Error`: Server error

### GET /health

Health check endpoint.

**Response:**

```json
{
  "status": "healthy"
}
```

## Testing

Run the test suite:

```bash
pytest test_main.py -v
```

Run tests with coverage:

```bash
pytest test_main.py --cov=. --cov-report=html
```

## Project Structure

```
backend/
├── main.py              # FastAPI application and endpoints
├── config.py            # Environment configuration settings
├── database.py          # Database connection and queries
├── models.py            # Pydantic data models
├── test_main.py         # API tests
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment variables
└── README.md            # This file
```

## Development

### Adding New Endpoints

1. Define your Pydantic model in `models.py`
2. Add database query functions in `database.py`
3. Create endpoint in `main.py`
4. Write tests in `test_main.py`

### Code Style

This project follows PEP 8 guidelines. Use tools like `black` and `flake8` for formatting:

```bash
black .
flake8 .
```

## Troubleshooting

### Database Connection Issues

If you get connection errors:

1. Verify PostgreSQL is running: `psql -h localhost -U postgres`
2. Check your `.env` file has correct credentials
3. Ensure the database `az_dc_db` exists
4. Verify the `datacenters` table is created

### Port Already in Use

If port 8000 is already in use, specify a different port:

```bash
uvicorn main:app --reload --port 8001
```

## License

See the LICENSE file in the root directory.
