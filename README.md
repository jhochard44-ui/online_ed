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

## Running the ELK valuation model in Stata

If you want to run the valuation logic entirely in Stata (without the API), use:

```stata
do stata/elk_valuation_model.do
```

The script defines an `elk_valuation_model` program that computes session valuation
from `rate_per_hour`, `duration_minutes`, `group_size`, and `group_discount`, then
shows an example output table.
