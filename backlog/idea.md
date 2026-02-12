### Create an application that visualizes Azure datacenter locations on a 3D globe. The system includes:

- **Data model**: Each datacenter has `id` (GUID), `location` (Azure region name), `country`,`city`.
- **Frontend**: A single, self-contained HTML page using the `three-globe` JavaScript library to render a spherical 3D globe with datacenter markers at their locations. Datacenter data is retrieved from a Python backend running on port `8000`.
- **Backend**: A FastAPI service exposing a GET endpoint that returns datacenter data as a JSON list. Data is read from a PostgreSQL database running locally in Docker. The database name is `az-dc-db`, and the table is `datacenters`. The API is served via `Uvicorn` on port `8000`. All secrets and connection strings must be loaded from `.env`.
- **Database**: A PostgreSQL container named `az-dc-db` with a `datacenters` table. Schema includes `id`, `name`, `country`, and `city`.
- **Repository**: The target repository is located at: https://github.com/HosseinZahed/azure-data-centers-demo