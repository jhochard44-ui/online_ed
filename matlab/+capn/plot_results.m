function plot_results(valueTbl)
%PLOT_RESULTS Create herd-level and statewide trend figures.

outDir = fullfile(fileparts(fileparts(mfilename('fullpath'))), 'output');
if ~exist(outDir, 'dir')
    mkdir(outDir);
end

% Herd-level natural capital
f1 = figure('Visible','off');
tiledlayout(2,2,'TileSpacing','compact');
herds = unique(valueTbl.herd);
for i = 1:numel(herds)
    nexttile;
    sub = valueTbl(valueTbl.herd==herds(i),:);
    plot(sub.year, sub.natural_capital_value_usd/1e6, '-o','LineWidth',1.5);
    grid on;
    xlabel('Year'); ylabel('Asset value (million USD)');
    title(sprintf('%s Herd', herds(i)));
end
exportgraphics(f1, fullfile(outDir,'herd_asset_values.png'), 'Resolution', 200);
close(f1);

% Statewide aggregate trends
statewide = groupsummary(valueTbl, 'year', 'sum', {'natural_capital_value_usd','current_period_net_benefit_usd'});
f2 = figure('Visible','off');
yyaxis left;
plot(statewide.year, statewide.sum_natural_capital_value_usd/1e9, '-s', 'LineWidth',1.8);
ylabel('Natural capital value (billion USD)');
yyaxis right;
plot(statewide.year, statewide.sum_current_period_net_benefit_usd/1e6, '-d', 'LineWidth',1.8);
ylabel('Current net benefit (million USD)');
xlabel('Year');
grid on;
title('Wyoming Elk: Statewide Natural Capital and Net Benefits');
exportgraphics(f2, fullfile(outDir,'statewide_trends.png'), 'Resolution', 200);
close(f2);
end
