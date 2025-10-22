# 🗑️ Collect - Smart Waste Collection Tracking

A modern, intelligent waste management application with live tracking, real-time statistics, and interactive mapping. Built for the Hackathon with professional features.

## 🎯 Features

### Core Features
- 🗺️ **Live Map Tracking** - Real-time visualization of waste collection vehicles and bins
- 📍 **Location-Based Services** - Search any location and track nearby bins
- 🚚 **Vehicle Tracking** - Real-time monitoring of collection vehicles with routes and ETAs
- 🗑️ **Waste Bin Management** - View all available waste bins with capacity status
- 📊 **Live Statistics** - Real-time count of bins, vehicles, and efficiency metrics
- 🔐 **User Authentication** - Secure login/logout system
- 🌗 **Dynamic Theme Switching** - Dark mode and light mode with automatic color adjustments
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile devices
- ♻️ **Recycling Support** - Differentiate between regular and recycling bins
- 🎨 **Glassmorphism UI** - Modern, professional design with backdrop filters
- ⚡ **Smooth Animations** - Fluid transitions and interactive elements
- 🔄 **Vehicle Animation** - Live movement simulation of collection vehicles

### UI/UX Features
- Scrollable nearby bins panel with click-to-focus functionality
- Theme indicator showing current mode (Dark/Light)
- 3D map view with building extrusion
- Customizable search and location services
- Professional glassmorphic cards and panels
- Smooth color transitions between themes

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Edge, Safari)
- Mapbox API token (free account at mapbox.com)

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/collect-hackathon.git
cd collect-hackathon
```

### 2. Install Backend Dependencies

```bash
pip install fastapi uvicorn pydantic
```

Or install from requirements.txt (if provided):
```bash
pip install -r requirements.txt
```

### 3. Get Your Mapbox Token

1. Go to https://account.mapbox.com/access-tokens/
2. Copy your **PUBLIC** token (starts with `pk.`)
3. Add it to `collect-hackathon.html` at line 403:
   ```javascript
   const MAPBOX_TOKEN = 'pk.YOUR_TOKEN_HERE';
   ```

### 4. Run the Backend Server

Open a terminal and run:

```bash
python backend.py
```

You should see:
```
🗑️  TrashMap Backend Server
============================================================
✅ Server URL: http://localhost:8000
📚 API Docs: http://localhost:8000/docs
🔄 Keep this terminal running!
```

### 5. Open the Application

Open `collect-hackathon.html` in your web browser:
- Double-click the file, OR
- Right-click → Open with → Your Browser

## 🎮 How to Use

### Login
1. Launch the app
2. Enter your **name** and **email**
3. Click "Login to Collect"

### Main Dashboard
- **Left Panel**: Scroll through nearby trash bins
- **Top Left**: Search for any location
- **Top Right**: View live statistics
- **Right Side**: Map controls (zoom, theme toggle, location)
- **Bottom Right**: Theme indicator (Dark/Light mode)

### Map Features
- **Click on Bins/Vehicles**: See detailed information
- **Click Bin Cards**: Map flies to that location
- **Search Bar**: Search any address
- **Location Button**: Centers map on your location
- **Theme Button**: Toggle between dark and light modes
- **Zoom Controls**: Zoom in/out on the map
- **Crosshairs**: Center on your current location

### Logout
- Click the **Logout** button in the top right

## 📁 Project Structure

```
collect-hackathon/
│
├── collect-hackathon.html      # Main application (Frontend)
├── backend.py                   # Backend server (FastAPI)
├── README.md                    # This file
├── SETUP.md                     # Detailed setup guide
├── requirements.txt             # Python dependencies
└── .gitignore                   # Git ignore file
```

## 🔧 API Endpoints

The backend provides the following endpoints:

### Get All Trash Bins
```
GET /api/bins
Response: List of all trash bins with details
```

### Get Nearby Bins
```
GET /api/bins/nearby?lat=13.0827&lng=80.2707&radius=2.0
Response: Bins within specified radius (in km)
```

### Get All Active Vehicles
```
GET /api/vehicles
Response: List of all active collection vehicles
```

### Get System Statistics
```
GET /api/stats
Response: Total bins, active vehicles, reports, users
```

### Interactive API Docs
Visit: http://localhost:8000/docs

## 🛠️ Customization

### Change App Name
Replace "Collect" with your app name in:
- `collect-hackathon.html` (multiple locations)
- README.md
- Package metadata

### Modify Location (Default: Chennai)
Edit line 442 in `collect-hackathon.html`:
```javascript
center: [80.2707, 13.0827],  // [longitude, latitude]
```

### Add More Bins/Vehicles
Edit the initialization in `backend.py` (around line 45-65)

### Change Theme Colors
Modify CSS variables in `collect-hackathon.html`:
```css
:root {
    --bg-gradient-start: #1e3c72;
    --bg-gradient-mid: #2a5298;
    --bg-gradient-end: #7e22ce;
    /* ... other colors ... */
}
```

## 🚀 Deployment

### Deploy to GitHub Pages (Frontend)
1. Create a GitHub repository
2. Push your HTML file
3. Go to Settings → Pages
4. Select "Deploy from a branch"
5. Choose `main` branch and `/root` folder
6. Your app is live!

### Deploy Backend to Heroku
1. Create `Procfile`:
   ```
   web: uvicorn backend:app --host 0.0.0.0 --port $PORT
   ```

2. Create `requirements.txt`:
   ```
   fastapi
   uvicorn
   pydantic
   ```

3. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

## 📊 Performance Tips

- Use the **light theme** on bright displays
- **Zoom in** for better vehicle tracking
- **Scroll bins list** to find nearby locations
- **Click theme button** to adapt to ambient lighting

## 🐛 Troubleshooting

### Map not loading?
- Check browser console (F12)
- Verify Mapbox token is correct
- Ensure backend is running

### No bins/vehicles showing?
- Make sure backend is running
- Check network tab in DevTools
- Verify API endpoints return data

### Location not working?
- Check browser location permissions
- Allow access when prompted
- Use location button to request again

### Theme not changing?
- Hard refresh browser (Ctrl+F5)
- Clear browser cache
- Check if map style is loading

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👥 Contributors

- **Your Name** - Initial Development

## 📞 Support

For issues and questions:
- Open an GitHub Issue
- Check existing issues first
- Provide detailed error messages
