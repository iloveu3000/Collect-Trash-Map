# TrashMap Backend API
# Run: python backend.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum

app = FastAPI(title="TrashMap API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Models
class BinStatus(str, Enum):
    AVAILABLE = "available"
    FULL = "full"
    MAINTENANCE = "maintenance"

class BinType(str, Enum):
    REGULAR = "regular"
    RECYCLING = "recycling"
    ORGANIC = "organic"

class TrashBin(BaseModel):
    id: Optional[str] = None
    name: str
    latitude: float
    longitude: float
    type: BinType
    status: BinStatus
    capacity: int = 100

class Vehicle(BaseModel):
    id: str
    latitude: float
    longitude: float
    route: str
    driver_name: Optional[str] = None
    status: str = "active"
    capacity: int = 100
    eta_minutes: Optional[int] = None

# In-memory database
trash_bins_db = {}
vehicles_db = {}
reports_db = {}
users_db = {}

# Initialize sample data for Chennai
def init_data():
    global trash_bins_db, vehicles_db

    bins = [
        {"name": "T. Nagar Central", "lat": 13.0427, "lng": 80.2340, "type": "regular"},
        {"name": "Anna Nagar Park", "lat": 13.0878, "lng": 80.2085, "type": "recycling"},
        {"name": "Marina Beach North", "lat": 13.0569, "lng": 80.2825, "type": "regular"},
        {"name": "Adyar Depot", "lat": 13.0067, "lng": 80.2571, "type": "organic"},
        {"name": "Mylapore Temple", "lat": 13.0339, "lng": 80.2619, "type": "regular"},
        {"name": "Velachery Main", "lat": 13.0106, "lng": 80.2289, "type": "recycling"},
        {"name": "Guindy Industrial", "lat": 13.0067, "lng": 80.2206, "type": "regular"},
        {"name": "Nungambakkam", "lat": 13.0632, "lng": 80.2317, "type": "regular"},
    ]

    for i, bin_data in enumerate(bins):
        bin_id = f"BIN_{i+1:03d}"
        trash_bins_db[bin_id] = {
            "id": bin_id,
            "name": bin_data["name"],
            "latitude": bin_data["lat"],
            "longitude": bin_data["lng"],
            "type": bin_data["type"],
            "status": "available",
            "capacity": 100 - (i * 12) % 100,
            "address": f"{bin_data['name']}, Chennai"
        }

    vehicles = [
        {"route": "T. Nagar Zone", "lat": 13.0427, "lng": 80.2340, "driver": "Rajesh Kumar"},
        {"route": "Anna Nagar Zone", "lat": 13.0878, "lng": 80.2085, "driver": "Priya Sharma"},
        {"route": "Beach Road", "lat": 13.0569, "lng": 80.2825, "driver": "Arjun Singh"},
    ]

    for i, v in enumerate(vehicles):
        vid = f"VEH_{i+1:03d}"
        vehicles_db[vid] = {
            "id": vid,
            "latitude": v["lat"],
            "longitude": v["lng"],
            "route": v["route"],
            "driver_name": v["driver"],
            "status": "active",
            "capacity": (i * 20) % 100,
            "eta_minutes": 10 + (i * 5)
        }

init_data()

# API Endpoints
@app.get("/")
async def root():
    return {"message": "TrashMap API v1.0", "status": "running"}

@app.get("/api/bins")
async def get_bins():
    return list(trash_bins_db.values())

@app.get("/api/bins/nearby")
async def get_nearby_bins(lat: float, lng: float, radius: float = 2.0):
    from math import radians, sin, cos, sqrt, atan2

    def distance(lat1, lon1, lat2, lon2):
        R = 6371
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        return R * c

    nearby = []
    for bin_data in trash_bins_db.values():
        dist = distance(lat, lng, bin_data["latitude"], bin_data["longitude"])
        if dist <= radius:
            bin_copy = bin_data.copy()
            bin_copy["distance_km"] = round(dist, 2)
            nearby.append(bin_copy)

    nearby.sort(key=lambda x: x["distance_km"])
    return nearby

@app.get("/api/vehicles")
async def get_vehicles():
    return list(vehicles_db.values())

@app.get("/api/stats")
async def get_stats():
    return {
        "total_bins": len(trash_bins_db),
        "available_bins": len([b for b in trash_bins_db.values() if b["status"] == "available"]),
        "active_vehicles": len([v for v in vehicles_db.values() if v["status"] == "active"]),
        "total_reports": len(reports_db),
        "total_users": len(users_db)
    }

if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*60)
    print("🗑️  TrashMap Backend Server")
    print("="*60)
    print("✅ Server starting on http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs")
    print("🔄 Keep this terminal running!")
    print("="*60 + "\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)
