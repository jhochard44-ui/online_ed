# Wyoming Elk Natural Capital Valuation (MATLAB)

This module implements a herd-level natural capital valuation model for Wyoming elk using a CAPN-style co-state (shadow price) recursion inspired by Fenichel et al.

## Run

```matlab
results = run_wy_elk_capital_model();
```

Outputs are written to `matlab/output`:
- `estimated_parameters.csv`
- `herd_level_capital_values.csv`
- `statewide_capital_values.csv`
- `herd_asset_values.png`
- `statewide_trends.png`

## Model structure

For herd `h` in year `t`:

- State variable: elk population `X_{h,t}`
- Control proxy: harvest `H_{h,t}` (observed management outcome)
- Biological process:
  `X_{h,t+1} = X_{h,t} + r_h X_{h,t}(1 - X_{h,t}/K_h) - H_{h,t}`
- Period net benefit:
  `NB_{h,t} = (\alpha^R_h - \alpha^D_h)X_{h,t} - C_{h,t}`

Shadow price recursion (current-value co-state approximation):

`\lambda_{h,t} = \partial NB/\partial X + \beta \lambda_{h,t+1} \partial F/\partial X`

with `\beta = 1/(1+\rho)`.

Asset value approximation:

`A_{h,t} = \lambda_{h,t} X_{h,t}`

## Data notes

`matlab/data/wy_elk_herd_timeseries.csv` contains a 2019-2023 panel for 4 Wyoming herds.
This dataset is an operational starter panel intended for reproducible code execution.
Before policy use, replace these entries with official herd-unit level time series from Wyoming Game and Fish Department annual job completion reports and herd-unit dashboards, plus inflation-adjusted valuation inputs.

## Why this is CAPN-aligned

The implementation uses:
- Dynamic state transition with biologically grounded density dependence.
- Explicit marginal-value recursion to recover state-dependent shadow prices.
- Asset valuation via state and co-state trajectories.

These are core CAPN mechanics used in Fenichel-style natural capital accounting workflows.
