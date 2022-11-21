%
% Function to convert a 2^m x 2^n matrix A to the matrix U 
% of its Haar coefficients. This is the standard method. 
% Converts all the rows and then all the columns
%

function U = haar2D(A)

[a, b] = size(A);
row_transform = zeros(size(A'));
col_transform = zeros(size(A));

for i = 1:a
    row_transform(:, i) = haar(A(i, :));

end

for j = 1:b
    col_transform(:, j) = haar(row_transform(j, :));

end

U = col_transform;
end
