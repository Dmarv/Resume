%
% Function to convert a 2^m x 2^n matrix A to the matrix U 
% of its Haar coefficients. This is the standard method. 
% Converts all the rows and then all the columns
% This version uses the normalized coefficients. 
%

function U = haar2D_n(A)
[a, b] = size(A);
row_transform = zeros(size(A'));
col_transform = zeros(size(A));

for i = 1:a
    row_transform(:, i) = haar_n(A(i, :));

end

for j = 1:b
    col_transform(:, j) = haar_n(row_transform(j, :));

end

U = col_transform;

end
