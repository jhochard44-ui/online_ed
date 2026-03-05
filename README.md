# Economics Learning Prototype

This repository contains a FastAPI prototype for an online education platform that
prioritizes foundational economics concepts and paid expert reinforcement sessions.

## Features

- Curated set of core economics concepts with learning modules and resources.
- Expert marketplace seeded with availability, pricing, and focus areas.
- Booking endpoint that validates concept alignment, availability windows, and
  calculates session pricing.

## Running the API

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start the development server:

   ```bash
   uvicorn app.api:app --reload
   ```

3. Explore the interactive documentation at `http://127.0.0.1:8000/docs`.

## Tests

Execute the unit test suite with:

```bash
pytest
```

## Wyoming elk natural capital MATLAB model

A full herd-level MATLAB natural capital valuation workflow is included under `matlab/`.
Run `run_wy_elk_capital_model` from MATLAB to estimate biological parameters, recover CAPN-style shadow prices, compute NPV/asset values, and generate herd/statewide figures.
