# Rank Vision

**Keepa API · Pandas · NumPy · Transformers · OpenAI**

Boost analysis accuracy and deliver actionable insights for Amazon sellers. Rank Vision fetches and cleans Keepa data, forecasts sales-rank trends, and generates tailored growth recommendations using an OpenAI wrapper.

## Features
- **Data ingestion**: Wrapper for Keepa Product API.
- **Processing**: Robust preprocessing & feature engineering.
- **Forecasting**: Simple baseline + slot-in Transformers.
- **Reporting**: Summary stats and trend charts.
- **AI feedback**: OpenAI-powered recommendations + feedback loop to tailor advice to your business context.
- **Pipeline**: One command to run end-to-end.

## Quickstart
1. Create a virtualenv and install deps:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
