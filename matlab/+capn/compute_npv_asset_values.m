function valueTbl = compute_npv_asset_values(shadowTbl, discountRate)
%COMPUTE_NPV_ASSET_VALUES Compute period net benefits and natural capital values.
%   Asset value approximation: A_t = lambda_t * X_t

beta = 1 / (1 + discountRate);
valueTbl = shadowTbl;

valueTbl.current_period_net_benefit_usd = ...
    (valueTbl.recreation_value_per_elk_usd - valueTbl.damage_cost_per_elk_usd) ...
    .* valueTbl.population_estimate - valueTbl.management_cost_usd;

valueTbl.natural_capital_value_usd = ...
    valueTbl.shadow_price_usd_per_elk .* valueTbl.population_estimate;

valueTbl.discount_factor = nan(height(valueTbl),1);
for h = unique(valueTbl.herd)'
    idx = find(valueTbl.herd == h);
    years = valueTbl.year(idx);
    t0 = min(years);
    valueTbl.discount_factor(idx) = beta .^ (years - t0);
end

valueTbl.discounted_net_benefit_usd = valueTbl.discount_factor .* valueTbl.current_period_net_benefit_usd;
end
