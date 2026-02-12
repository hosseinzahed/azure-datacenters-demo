## 🏗️ Project Architecture

### Data Model
Each datacenter record contains:
- `id` (GUID): Unique identifier
- `name` (String): Azure region name
- `country` (String): Country where datacenter is located
- `city` (String): City location

### Frontend
- **Technology**: HTML + JavaScript
- **Library**: `three-globe` for 3D visualization
- **Port**: Serves static files
- **Data Source**: Fetches from backend API on port `8000`

### Backend
- **Framework**: FastAPI (Python)
- **Port**: `8000`
- **Endpoint**: GET `/datacenters` - Returns JSON list of datacenters
- **Database**: Connects to PostgreSQL container
- **Configuration**: Environment variables loaded from `.env` file

### Database
- **Type**: PostgreSQL
- **Container Name**: `az-dc-db`
- **Port**: `5432`
- **Database Name**: `az-dc-db`
- **Table**: `datacenters`
- **Credentials**: 
  - User: `postgres`
  - Password: `postgres` (stored in `.env`)
