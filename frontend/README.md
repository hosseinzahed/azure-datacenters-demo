# Azure Datacenters - Frontend

A single-page HTML application that visualizes Azure datacenter locations on an interactive 3D globe.

## Features

- **3D Globe Visualization**: Interactive Earth globe powered by three-globe and Three.js
- **Real-time Data**: Fetches datacenter information from the backend API
- **Interactive Markers**: Red markers indicating datacenter locations
- **Tooltips**: Hover over markers to see datacenter name, city, and country
- **Auto-rotation**: Globe automatically rotates for a dynamic view
- **Responsive Design**: Adapts to different screen sizes
- **Error Handling**: Graceful error messages if backend is unavailable
- **Loading States**: Visual feedback during data loading

## Technology Stack

- **Three.js**: 3D graphics library
- **three-globe**: Globe visualization component
- **Vanilla JavaScript**: No framework dependencies
- **HTML5/CSS3**: Modern web standards

## Usage

### Prerequisites

- Backend API must be running on `http://localhost:8000`
- Modern web browser with WebGL support

### Running the Application

1. Open `index.html` in a web browser:
   ```bash
   # On Windows
   start frontend\index.html
   
   # On macOS
   open frontend/index.html
   
   # On Linux
   xdg-open frontend/index.html
   ```

2. Or serve it with a local HTTP server:
   ```bash
   # Using Python
   cd frontend
   python -m http.server 3000
   
   # Using Node.js
   npx http-server frontend -p 3000
   ```

3. Navigate to `http://localhost:3000` in your browser

## File Structure

```
frontend/
├── index.html          # Main application file (self-contained)
└── README.md          # This file
```

## API Integration

The application fetches datacenter data from:
```
GET http://localhost:8000/datacenters
```

Expected response format:
```json
[
  {
    "id": "uuid",
    "name": "East US",
    "country": "United States",
    "city": "Virginia"
  }
]
```

## Features Implementation

### Geocoding
The application includes a built-in geocoding map for common Azure datacenter locations. If a location is not found in the map, it logs a warning and uses fallback coordinates.

### Interactive Controls
- **Rotate**: Click and drag to rotate the globe
- **Zoom**: Scroll to zoom in/out
- **Auto-rotate**: Globe rotates automatically (can be stopped by interacting)

### Error Handling
- Displays user-friendly error messages if the backend is unavailable
- Includes a retry button to reload the page
- Console logging for debugging

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge

Requires WebGL support.

## Customization

### Changing Marker Color
Edit line ~368 in `index.html`:
```javascript
.pointColor(() => '#ff6b6b')  // Change hex color
```

### Adjusting Auto-rotate Speed
Edit line ~424 in `index.html`:
```javascript
controls.autoRotateSpeed = 0.5;  // Increase for faster rotation
```

### Adding More Geocoding Locations
Edit the `geocodingMap` object (starting ~line 200) to add more city/country coordinates.

## Troubleshooting

**Issue**: Globe doesn't load
- **Solution**: Ensure backend API is running on port 8000
- Check browser console for errors
- Verify WebGL is enabled in your browser

**Issue**: Markers appear in wrong locations
- **Solution**: Add correct coordinates to the `geocodingMap` object

**Issue**: CORS errors
- **Solution**: Ensure backend has CORS enabled for localhost

## Future Enhancements

- [ ] Add filtering by region/country
- [ ] Show datacenter capacity/status
- [ ] Add search functionality
- [ ] Display connection lines between datacenters
- [ ] Add dark/light theme toggle
- [ ] Real-time status updates via WebSocket
