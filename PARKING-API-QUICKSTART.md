# Parking Management API - Quick Start

## Project Location
```
src/ParkingManagementApi/
```

## Quick Start Commands

```bash
# Navigate to project
cd src/ParkingManagementApi

# Run the API
dotnet run

# Access Swagger UI
http://localhost:5000/swagger
```

## API Endpoints

- **GET** `/api/parking` - Get all parking spots
- **GET** `/api/parking/{id}` - Get specific spot
- **POST** `/api/parking` - Create new spot
- **PUT** `/api/parking/{id}` - Update spot
- **DELETE** `/api/parking/{id}` - Delete spot
- **POST** `/api/parking/{id}/occupy` - Occupy spot with vehicle
- **POST** `/api/parking/{id}/vacate` - Free up spot

## Documentation

- **Full Documentation**: `src/ParkingManagementApi/README.md`
- **Test Requests**: `src/ParkingManagementApi/ParkingManagementApi.http`
- **Implementation Summary**: `summaries/parking-management-api-implementation-2025-11-08.md`

## Architecture

```
Controller → Service → Repository → In-Memory Storage
```

## Features

✅ Complete CRUD operations
✅ Occupy/vacate parking spots
✅ Input validation
✅ Error handling
✅ Swagger documentation
✅ 10 pre-seeded test spots
✅ Thread-safe in-memory storage

## Example Usage

```bash
# Get all spots
curl http://localhost:5000/api/parking

# Create a new spot
curl -X POST http://localhost:5000/api/parking \
  -H "Content-Type: application/json" \
  -d '{"spotNumber":"D-401","floor":4,"section":"D"}'

# Occupy a spot
curl -X POST http://localhost:5000/api/parking/2/occupy \
  -H "Content-Type: application/json" \
  -d '{"vehicleLicensePlate":"ABC-123"}'
```

## Technology Stack

- ASP.NET Core 8.0
- C# 12.0
- Swagger/OpenAPI
- In-Memory Storage

## Project Status

✅ **COMPLETED** - All AgentTask requirements met
- 0 Build Warnings
- 0 Build Errors
- All endpoints tested and working
- Full documentation provided

---

For detailed information, see the full README in `src/ParkingManagementApi/README.md`
