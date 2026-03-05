function paramTbl = estimate_bioeconomic_parameters(dataTbl)
%ESTIMATE_BIOECONOMIC_PARAMETERS Estimate herd-level logistic growth terms.
%   Growth law: X_{t+1}=X_t + r X_t (1-X_t/K) - H_t

herds = unique(dataTbl.herd);
out = table('Size',[numel(herds),6], ...
    'VariableTypes',{'string','double','double','double','double','double'}, ...
    'VariableNames',{'herd','r','K','alpha_recreation','alpha_damage','mean_management_cost'});

for i = 1:numel(herds)
    h = herds(i);
    sub = dataTbl(dataTbl.herd==h,:);
    valid = ~isnan(sub.growth_next);

    X = sub.population_estimate(valid);
    H = sub.harvest(valid);
    G = sub.growth_next(valid) + H;

    % Linearized logistic regression: G/X = r - (r/K) X
    Y = G ./ X;
    Xreg = [ones(size(X)), X];
    b = Xreg \ Y;

    r = max(b(1), 1e-4);
    slope = b(2);
    if slope >= 0
        K = max(1.1 * max(X), 1000);
    else
        K = max(-r / slope, 1000);
    end

    out.herd(i) = h;
    out.r(i) = r;
    out.K(i) = K;
    out.alpha_recreation(i) = mean(sub.recreation_value_per_elk_usd);
    out.alpha_damage(i) = mean(sub.damage_cost_per_elk_usd);
    out.mean_management_cost(i) = mean(sub.management_cost_usd);
end

paramTbl = out;
end
