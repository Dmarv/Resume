
%a function that takes in one 2 x n matrix and returns its final out put
% after n iterations 

function [x, y] = subdiv_helper1a(bx, by, n)
a = size(bx);

%initialize output space and bx, by
size_3 = power(2, n);
final_output = zeros(2, a(2), size_3);

final_output(1, :, 1) = bx;

final_output(2, :, 1) = by;

for i=1:n
    round = power(2, i - 1);
    %make temp the size of this iteration
    temp_return = zeros(2, a(2), power(2, i));
    for j=1:round
        [tx, ty] = subdivstep1a(final_output(1, :, j), final_output(2, :, j));
        temp_return(:, :, 2*j -1) = tx;
        temp_return(:, :, 2*j) = ty;

    end
    %populate the next round
    for k=1:2*round
        final_output(:,:, k) = temp_return(:, :, k);
    end

end
 x_temp = [];
 y_temp = [];
for l=1:size_3
    x_temp = [x_temp final_output(1,:, l)];
    y_temp = [y_temp final_output(2,:, l)];

end

x = [];
y = [];
p = size(x_temp);
for m=1:p(2)-1
    if (x_temp(m) ~= x_temp(m+1)) || (y_temp(m) ~= y_temp(m+1))
        x = [x x_temp(m)];
        y = [y y_temp(m)];
    else
        if (x_temp(m) == x_temp(m+2)) && (y_temp(m) == y_temp(m+2))
            x = [x x_temp(m)];
            y = [y y_temp(m)];
        end

    end

end
x = [x x_temp(p(2))];
y = [y y_temp(p(2))];

x = x';
y = y';

end
