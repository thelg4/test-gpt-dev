# CSV Analyzer API

A FastAPI-based service to upload and analyze CSV files. It provides endpoints for uploading files, summarizing data, detecting nulls, and understanding data types.

## Features
- Upload CSV files via API
- Retrieve summary statistics (mean, std, min, max, etc.)
- Get column data types and null value counts

## Endpoints
### POST `/upload`
Upload a CSV file.

**Form field:** `file`

### GET `/analyze/{filename}`
Run analysis on the uploaded CSV file.

## Project Structure
```
csv_analyzer/
├── app/
│   ├── api/routes.py        # API endpoints
│   ├── main.py              # FastAPI app entry
│   ├── services/analyzer.py# Core analysis logic
│   ├── models/schemas.py   # (Placeholder) for data models
│   └── utils/file_utils.py # (Placeholder) for file utilities
├── mock_data.csv            # Sample data file
└── README.md                # Project documentation
```

## Running Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 9000
```

Then visit `http://localhost:9000/docs` for the Swagger UI.

---
Feel free to contribute or extend the analysis logic!