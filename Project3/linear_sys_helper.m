%General solution where nxn is the size of our matrix
function [A] = linear_sys_helper(n)
middle = zeros(1, n);

peripheral = zeros(1,n - 1);


for i=1:n
    middle(i) = 4;
    if ~(i == n)
        peripheral(i) = 1;
    end
end
disp(middle);
disp(peripheral);
mid_matrix = diag(middle);
top_matrix = diag(peripheral, 1);
bot_matrix = diag(peripheral, -1);
A = mid_matrix + top_matrix + bot_matrix;

end


