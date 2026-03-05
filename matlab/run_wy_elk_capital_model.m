function results = run_wy_elk_capital_model(varargin)
%RUN_WY_ELK_CAPITAL_MODEL Natural capital valuation model for WY elk herds.
%   RESULTS = RUN_WY_ELK_CAPITAL_MODEL() loads herd-level elk population
%   and harvest data, estimates herd-specific biological dynamics, computes
%   state-variable dependent shadow prices using a CAPN-style recursive
%   co-state equation, and reports NPV/asset values over time.
%
%   Optional name/value pairs:
%   - 'DataPath'       : Path to CSV panel data.
%   - 'DiscountRate'   : Annual discount rate (default 0.03).
%   - 'TerminalWeight' : Weight on terminal shadow value (default 1.0).
%
%   This script writes figures to matlab/output and returns a table-rich
%   struct suitable for further analysis.

p = inputParser;
addParameter(p, 'DataPath', fullfile(fileparts(mfilename('fullpath')), 'data', 'wy_elk_herd_timeseries.csv'));
addParameter(p, 'DiscountRate', 0.03);
addParameter(p, 'TerminalWeight', 1.0);
parse(p, varargin{:});
opts = p.Results;

dataTbl = capn.load_wy_data(opts.DataPath);
params = capn.estimate_bioeconomic_parameters(dataTbl);
shadowTbl = capn.compute_shadow_prices(dataTbl, params, opts.DiscountRate, opts.TerminalWeight);
valueTbl = capn.compute_npv_asset_values(shadowTbl, opts.DiscountRate);
capn.plot_results(valueTbl);

results = struct();
results.parameters = params;
results.shadow = shadowTbl;
results.values = valueTbl;

outDir = fullfile(fileparts(mfilename('fullpath')), 'output');
if ~exist(outDir, 'dir')
    mkdir(outDir);
end
writetable(params, fullfile(outDir, 'estimated_parameters.csv'));
writetable(valueTbl, fullfile(outDir, 'herd_level_capital_values.csv'));

statewide = groupsummary(valueTbl, 'year', 'sum', {'natural_capital_value_usd', 'current_period_net_benefit_usd'});
writetable(statewide, fullfile(outDir, 'statewide_capital_values.csv'));

fprintf('Model complete. Outputs written to %s\n', outDir);
end
