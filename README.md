# Hiking Zone - UK Hiking Map

A web application that shows 20 circular walking routes with real-time rain forecasts. Pick a date, see which spots will be dry, and find your next hike!

## What This App Does

- Shows 20 hiking spots on an interactive map (forests and coastal walks)
- Displays rain forecasts for the next 14 days
- Colour-coded weather overlay: green = dry, yellow = light rain, orange = moderate, pink = heavy
- Hourly rain breakdown for each location (9am-5pm walking hours)
- Links to AllTrails for route directions
- **Two modes**:
  - **Callum mode**: Hikes within 2 hours of East London
  - **Robert mode**: Hikes within 2 hours of Newton-le-Willows

---

## How to Run This App

### Step 1: Check if Python is Installed

Open **Terminal** on your Mac:
- Press `Cmd + Space`, type "Terminal", and press Enter

Then type this command and press Enter:
```
python3 --version
```

You should see something like `Python 3.11.5`. If you see an error like "command not found", you need to install Python first (see the "Installing Python" section below).

### Step 2: Clone the Repository

If you haven't got the code yet, you need to "clone" it from GitHub. This downloads a copy to your computer.

First, make sure you have Git installed by typing:
```
git --version
```

If you see a version number, you're good. If not, your Mac will prompt you to install the Command Line Tools - click "Install" and wait for it to finish.

Now clone the repository:
```
cd ~/Documents
git clone https://github.com/callum-saxon/hiking_map.git
```

This creates a folder called `hiking_map` in your Documents folder with all the code.

### Step 3: Open the App Folder

In your Terminal, navigate to the app folder:
```
cd ~/Documents/hiking_map
```

### Step 4: Set Up the App (First Time Only)

The first time you run the app, you need to set up a "virtual environment" and install the required packages. This keeps the app's files separate from other things on your computer.

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

You'll know the virtual environment is active when you see `(.venv)` at the start of your command line.

### Step 5: Run the App

With the virtual environment active (you should see `(.venv)` in your terminal), run:

```
uvicorn app.main:app --reload
```

You should see output like:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```

### Step 6: Open the App in Your Browser

Open your web browser (Chrome, Safari, Firefox, etc.) and go to:

```
http://localhost:8000
```

The hiking map should appear!

### Step 7: Using the App

1. **Choose who's hiking** - On the landing page, click your name (Callum or Robert)
2. **Pick a date** - Use the date picker to choose when you want to go hiking
3. **Check the weather** - The coloured overlay shows rain levels across the region
4. **Click on a marker** - Green dots are forest hikes, blue dots are coastal hikes
5. **See the forecast** - Each location shows hourly rain predictions for 9am-5pm
6. **Get directions** - Click "View Circular Walk Route" to open AllTrails
7. **Switch user** - Click "BACK" in the top left to return to the landing page

### Step 8: Stopping the App

When you're done, go back to Terminal and press `Ctrl + C` to stop the server.

---

## Running the App Again (After First Setup)

Once you've done the initial setup, running the app is simpler:

```
cd ~/Documents/hiking_map
source .venv/bin/activate
uvicorn app.main:app --reload
```

Then open http://localhost:8000 in your browser.

---

## Getting Updates

If I've made changes to the app and you want to get the latest version:

```
cd ~/Documents/hiking_map
git pull
```

If you have the virtual environment active, you may also need to install any new packages:
```
pip install -r requirements.txt
```

---

## Installing Python (If Needed)

The easiest way is to download from the official website:
1. Go to https://www.python.org/downloads/
2. Click the big yellow "Download Python" button
3. Open the downloaded file and follow the installer
4. Restart Terminal after installation

---

## Troubleshooting

### "command not found: python3"
Python isn't installed or isn't in your PATH. See "Installing Python" above.

### "No module named uvicorn"
The packages aren't installed. Make sure your virtual environment is active (you should see `(.venv)`) and run:
```
pip install -r requirements.txt
```

### "Address already in use"
Another app is using port 8000. Either close that app, or run on a different port:
```
uvicorn app.main:app --reload --port 8001
```
Then open http://localhost:8001 instead.

### The map doesn't load
Check your internet connection - the app needs to fetch map tiles and weather data online.

### Weather shows "Loading..."
The weather API might be slow. Wait a few seconds, or click "Update Forecast" to try again.

---

## Technical Details (For Reference)

- **Backend**: Python with FastAPI
- **Frontend**: HTML/CSS/JavaScript with Leaflet.js maps
- **Weather Data**: Open-Meteo API (free, no API key needed)
- **Map Tiles**: OpenStreetMap
