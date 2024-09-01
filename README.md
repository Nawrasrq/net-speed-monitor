# Net Speed Monitor

A Python-based project for periodically measuring and monitoring internet speed using the `speedtest-cli` tool. The project stores speed test results in a SQLite database and provides a web interface to visualize the data using charts.

## Features

- Periodically performs speed tests (download and upload speeds).
- Stores results in a SQLite database.
- Provides a REST API to fetch speed test data.
- Displays speed test results in a web interface with charts.

## Project Structure
```
net-speed-monitor/
│
├── scripts/
│   ├── run_speedtest.py        # Script to run the speed test and store results
│   └── scheduler.py            # Script to schedule periodic speed tests
│
├── db_manager.py               # Handles database schema and operations
├── speedtest_service.py        # Manages speed test operations
├── __init__.py                 # Package initialization (optional)
└── requirements.txt            # Python dependencies
```
## Setup
### Prerequisites
- Python 3.7 or higher
- pip for installing Python packages
### Installation
Clone the repository:

```bash
git clone https://github.com/yourusername/net-speed-monitor.git
cd net-speed-monitor
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```
The database will be initialized automatically the first time you run the run_speedtest.py script.

### Usage
To manually run a speed test and store the results:

```bash
python scripts/run_speedtest.py
```

To schedule the speed test to run every 3 hours, execute:

```bash
python scripts/scheduler.py
```

Navigate to the web directory and install dependencies:

```bash
cd web
npm install
```
Start the server:

```bash
npm start
```
Open your browser and go to http://localhost:3000 to view the speed test results on a chart.

## API

The project includes a REST API to fetch speed test data.

- Endpoint: /api/speedtest
- Method: GET
- Response: JSON object containing an array of speed test records.

Example Request
```bash
curl http://localhost:3000/api/speedtest
```

Example Response
```javascript
{
  "data": [
    {
      "id": 1,
      "download_speed": 50.5,
      "upload_speed": 10.2,
      "timestamp": "2024-09-01T12:00:00"
    },
    ...
  ]
}
```