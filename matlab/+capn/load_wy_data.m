function dataTbl = load_wy_data(dataPath)
%LOAD_WY_DATA Load and validate WY elk herd panel.

dataTbl = readtable(dataPath, 'TextType', 'string');
required = ["herd","year","population_estimate","harvest", ...
    "management_cost_usd","recreation_value_per_elk_usd","damage_cost_per_elk_usd"];
missing = setdiff(required, dataTbl.Properties.VariableNames);
if ~isempty(missing)
    error('Missing required columns: %s', strjoin(missing, ', '));
end

dataTbl = sortrows(dataTbl, {'herd','year'});
dataTbl.growth_next = nan(height(dataTbl),1);
for h = unique(dataTbl.herd)'
    idx = find(dataTbl.herd == h);
    for k = 1:numel(idx)-1
        t = idx(k);
        t1 = idx(k+1);
        dataTbl.growth_next(t) = dataTbl.population_estimate(t1) - dataTbl.population_estimate(t);
    end
end
end
