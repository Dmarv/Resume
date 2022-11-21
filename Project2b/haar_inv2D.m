%
%  Function to reconstruct a 2^m x 2^n matrix A from its
%  matrix of Haar coefficients. 
%  Converts all the columns and then all the rows
%
function A = haar_inv2D(U)
[a, b] = size(U);
row_transform = zeros(size(U'));
col_transform = zeros(size(U));

for i = 1:a
    row_transform(:, i) = haar_inv(U(i, :));


end

for j = 1:b
    col_transform(:, j) = haar_inv(row_transform(j, :));

end
A = col_transform;

end
