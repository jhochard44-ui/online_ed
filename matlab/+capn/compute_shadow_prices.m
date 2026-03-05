function shadowTbl = compute_shadow_prices(dataTbl, paramTbl, discountRate, terminalWeight)
%COMPUTE_SHADOW_PRICES Recover CAPN-style shadow values via co-state recursion.
%   Current-value Hamiltonian ingredients by herd and year:
%   NetBenefit(X,H) = alpha_r * X - alpha_d * X - c_m
%   dNetBenefit/dX = alpha_r - alpha_d
%   State transition F(X,H) = X + rX(1-X/K)-H
%   dF/dX = 1 + r(1 - 2X/K)
%
%   Backward recursion approximation of co-state (shadow price):
%   lambda_t = dNB/dX_t + beta * lambda_{t+1} * dF/dX_t,
%   where beta = 1/(1+discountRate).

beta = 1 / (1 + discountRate);
shadowTbl = dataTbl;
shadowTbl.shadow_price_usd_per_elk = nan(height(dataTbl),1);
shadowTbl.marginal_net_benefit_usd_per_elk = nan(height(dataTbl),1);
shadowTbl.transition_derivative = nan(height(dataTbl),1);

for h = unique(dataTbl.herd)'
    idx = find(dataTbl.herd == h);
    sub = dataTbl(idx,:);
    p = paramTbl(paramTbl.herd==h,:);

    dNB = p.alpha_recreation - p.alpha_damage;
    dF = 1 + p.r .* (1 - 2 .* sub.population_estimate ./ p.K);

    lambda = nan(height(sub),1);
    lambda(end) = terminalWeight * dNB;

    for t = height(sub)-1:-1:1
        lambda(t) = dNB + beta * lambda(t+1) * dF(t);
    end

    shadowTbl.shadow_price_usd_per_elk(idx) = lambda;
    shadowTbl.marginal_net_benefit_usd_per_elk(idx) = dNB;
    shadowTbl.transition_derivative(idx) = dF;
end
end
