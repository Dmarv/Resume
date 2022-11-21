function [data_hat, data_bar] = column_mean_helper(data, m, B)
%solve for centered X-coordinates
data_bar = 0;
for i=1:m
    data_bar = data_bar + data(i);
end
data_bar = data_bar/m;
data_hat = data - data_bar*B;
end

