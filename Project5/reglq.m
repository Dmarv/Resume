function [w,nw,b,xi,nxi] = reglq(X,y)
%  Regression minimizing w and b
%  X is an m x n matrix, y a m x 1 colum vector
%  weight vector w, intercept b
%  Computes the least squares solution using the pseudo inverse
%
m = size(y,1);
n = size(X, 2);
B = ones(m, 1);
I = eye(m);
X1 = [X B];

A_plus = inv(X1'*X1)*X1';
w_b = A_plus*y; 
w = w_b(1:n);
b = w_b(n+1);
nw = Euclid_norm(w);
xi = y - X*w - b*B;
nxi = Euclid_norm(xi);
end

