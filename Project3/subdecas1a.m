
%gets the ud and ld from a matrix of size 2 x n and returns 
% a ud and ld of size 1 x (2n -1)

function [ud, ld] = subdecas1a(bx, by)

%get the number of polynomials we will use
my_size = size(bx);
b_size = my_size(2);
ar_size = 2*b_size - 1;

%split the x and y coordinates
x = bx;
y = by;

%allocate space
temp_u1 = x;
temp_l1 = y;
temp_u2 = x;
temp_l2 = y;

%put in the edge cases
ud(1) = x(1);
ud(ar_size) = x(b_size);
ld(1) = y(1);
ld(ar_size) = y(b_size);

for i=1:b_size - 1
    for j=1:b_size - 1
        temp_u2(j) = (temp_u1(j) + temp_u1(j + 1))/2;
        temp_l2(j) = (temp_l1(j) + temp_l1(j + 1))/2;
        ud(i + 1) = temp_u2(1);
        ud(ar_size - i) = temp_u2(b_size - i);
        ld(i + 1) = temp_l2(1);
        ld(ar_size - i) = temp_l2(b_size - i);
        temp_u1 = temp_u2;
        temp_l1 = temp_l2;
    end
end

