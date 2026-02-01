// Current mode (callum or robert)
let currentMode = 'callum';

// Map center coordinates for each mode
const mapSettings = {
    callum: { center: [51.3, 0.3], zoom: 8, subtitle: '20 CIRCULAR WALKS // 2HR DRIVE FROM EAST LONDON' },
    robert: { center: [53.5, -2.4], zoom: 8, subtitle: '20 CIRCULAR WALKS // 2HR DRIVE FROM NEWTON-LE-WILLOWS' }
};

// Initialize the map
const map = L.map('map').setView(mapSettings.callum.center, mapSettings.callum.zoom);

// Add OpenStreetMap tiles
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Layer groups for markers and rain overlay
let locationMarkers = L.layerGroup().addTo(map);
let rainOverlay = L.layerGroup().addTo(map);

// Store location data and weather data
let locations = [];
let weatherData = {};

// Neon color palette for vaporwave theme
function getRainColor(mm) {
    if (mm <= 0) return '#00ff88';      // Neon green - dry
    if (mm <= 2) return '#ffe66d';      // Neon yellow - light
    if (mm <= 5) return '#ff6b35';      // Sunset orange - moderate
    return '#ff2a6d';                    // Neon pink - heavy
}

// Format hour as 12-hour time
function formatHour(hour) {
    if (hour === 0) return '12am';
    if (hour === 12) return '12pm';
    if (hour < 12) return `${hour}am`;
    return `${hour - 12}pm`;
}

// Create custom marker icons with neon glow
function createMarkerIcon(type) {
    const color = type === 'forest' ? '#00ff88' : '#05d9e8';
    const glowColor = type === 'forest' ? 'rgba(0, 255, 136, 0.8)' : 'rgba(5, 217, 232, 0.8)';
    return L.divIcon({
        className: 'custom-marker',
        html: `<div style="
            background-color: ${color};
            width: 20px;
            height: 20px;
            border-radius: 50%;
            border: 3px solid white;
            box-shadow: 0 0 15px ${glowColor}, 0 0 30px ${glowColor};
            animation: pulse 2s ease-in-out infinite;
        "></div>
        <style>
            @keyframes pulse {
                0%, 100% { box-shadow: 0 0 15px ${glowColor}, 0 0 30px ${glowColor}; }
                50% { box-shadow: 0 0 20px ${glowColor}, 0 0 40px ${glowColor}; }
            }
        </style>`,
        iconSize: [20, 20],
        iconAnchor: [10, 10],
        popupAnchor: [0, -10]
    });
}

// Fetch and display locations
async function loadLocations() {
    try {
        const response = await fetch(`/api/locations?mode=${currentMode}`);
        const data = await response.json();
        locations = data.locations;

        // Clear existing markers
        locationMarkers.clearLayers();

        // Add markers for each location
        locations.forEach(loc => {
            const marker = L.marker([loc.latitude, loc.longitude], {
                icon: createMarkerIcon(loc.type)
            });

            marker.locationId = loc.id;
            marker.bindPopup(createPopupContent(loc, null));
            locationMarkers.addLayer(marker);
        });
    } catch (error) {
        console.error('Error loading locations:', error);
    }
}

// Create hourly forecast HTML
function createHourlyForecast(hourlyData) {
    if (!hourlyData || hourlyData.length === 0) return '';

    let html = '<div class="hourly-forecast">';
    html += '<div class="hourly-title">Hourly Forecast (9am-5pm)</div>';
    html += '<div class="hourly-grid">';

    hourlyData.forEach(h => {
        const color = getRainColor(h.precipitation_mm);
        const isRaining = h.precipitation_mm > 0;
        html += `
            <div class="hour-cell ${isRaining ? 'rainy' : 'dry'}">
                <div class="hour-time">${formatHour(h.hour)}</div>
                <div class="hour-bar" style="background: ${color};"></div>
                <div class="hour-mm">${h.precipitation_mm.toFixed(1)}</div>
            </div>
        `;
    });

    html += '</div></div>';
    return html;
}

// Create popup content for a location
function createPopupContent(location, locWeather) {
    let weatherHtml = '';
    if (locWeather) {
        const color = getRainColor(locWeather.total_mm);
        const rainyHours = locWeather.hourly.filter(h => h.precipitation_mm > 0);
        const dryHours = locWeather.hourly.length - rainyHours.length;

        let summaryText = '';
        if (rainyHours.length === 0) {
            summaryText = 'Dry all day!';
        } else if (dryHours === 0) {
            summaryText = 'Rain expected all day';
        } else {
            summaryText = `${dryHours} dry hours, ${rainyHours.length} rainy`;
        }

        weatherHtml = `
            <div class="popup-weather" style="border-left: 4px solid ${color}; padding-left: 8px; margin-top: 10px;">
                <div class="weather-summary">
                    <strong>${locWeather.total_mm.toFixed(1)}mm total</strong> - ${summaryText}
                </div>
                ${createHourlyForecast(locWeather.hourly)}
            </div>
        `;
    }

    return `
        <div class="popup-content">
            <h3>${location.name}</h3>
            <p class="popup-type">${location.type === 'forest' ? 'Forest Hike' : 'Coastal Hike'}</p>
            <p class="popup-drive">Drive time: ${location.drive_time}</p>
            <p class="popup-desc">${location.description}</p>
            <a href="${location.walk_url}" target="_blank" rel="noopener" class="walk-link">
                View Circular Walk Route
            </a>
            ${weatherHtml}
        </div>
    `;
}

// Fetch and display weather data
async function loadWeather(date) {
    showLoading(true);

    try {
        const response = await fetch(`/api/weather?date=${date}&mode=${currentMode}`);
        weatherData = await response.json();

        // Clear existing rain overlay
        rainOverlay.clearLayers();

        // Add rain overlay circles for grid points with neon effect
        weatherData.grid.forEach(point => {
            const color = getRainColor(point.precipitation_mm);
            // Outer glow
            const glow = L.circleMarker([point.latitude, point.longitude], {
                radius: 30,
                fillColor: color,
                fillOpacity: 0.15,
                stroke: false
            });
            // Inner circle
            const circle = L.circleMarker([point.latitude, point.longitude], {
                radius: 20,
                fillColor: color,
                fillOpacity: 0.35,
                stroke: true,
                color: color,
                weight: 1,
                opacity: 0.5
            });
            rainOverlay.addLayer(glow);
            rainOverlay.addLayer(circle);
        });

        // Update location popups with weather data
        updateLocationPopups();

    } catch (error) {
        console.error('Error loading weather:', error);
    } finally {
        showLoading(false);
    }
}

// Update location marker popups with weather data
function updateLocationPopups() {
    locationMarkers.eachLayer(marker => {
        const locationId = marker.locationId;
        const location = locations.find(l => l.id === locationId);
        const locWeather = weatherData.locations?.find(w => w.location_id === locationId);

        if (location) {
            marker.setPopupContent(createPopupContent(location, locWeather));
        }
    });
}

// Show/hide loading indicator
function showLoading(show) {
    const loading = document.getElementById('loading');
    if (show) {
        loading.classList.remove('hidden');
    } else {
        loading.classList.add('hidden');
    }
}

// Initialize date picker with today's date
function initDatePicker() {
    const datePicker = document.getElementById('date-picker');
    const today = new Date().toISOString().split('T')[0];
    datePicker.value = today;

    // Set min date to today
    datePicker.min = today;

    // Set max date to 14 days from now (Open-Meteo forecast limit)
    const maxDate = new Date();
    maxDate.setDate(maxDate.getDate() + 14);
    datePicker.max = maxDate.toISOString().split('T')[0];
}

// Switch mode (callum or robert)
async function switchMode(mode) {
    if (mode === currentMode) return;

    currentMode = mode;

    // Update button states
    document.querySelectorAll('.mode-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    document.querySelector(`[data-mode="${mode}"]`).classList.add('active');

    // Update subtitle
    document.getElementById('subtitle-text').textContent = mapSettings[mode].subtitle;

    // Pan map to new region
    map.setView(mapSettings[mode].center, mapSettings[mode].zoom);

    // Reload locations and weather for new mode
    await loadLocations();
    const date = document.getElementById('date-picker').value;
    await loadWeather(date);
}

// Event listeners
document.getElementById('refresh-btn').addEventListener('click', () => {
    const date = document.getElementById('date-picker').value;
    loadWeather(date);
});

document.getElementById('date-picker').addEventListener('change', (e) => {
    loadWeather(e.target.value);
});

// Mode button event listeners
document.querySelectorAll('.mode-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        const mode = e.target.dataset.mode;
        switchMode(mode);
    });
});

// Initialize the app
async function init() {
    initDatePicker();
    await loadLocations();
    const today = new Date().toISOString().split('T')[0];
    await loadWeather(today);
}

// Start the app
init();
