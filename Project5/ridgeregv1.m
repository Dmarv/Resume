function [w,nw,b,xi,nxi] = ridgeregv1(X,y,K)
%  Ridge regression with centered data
%  b is not penalized
%  X is an m x n matrix, y a m x 1 colum vector
%  weight vector w, intercept b
%  Solution in terms of the primal variables
%

m = size(y,1);
n = size(X, 2);
B = ones(m, 1);
I = eye(m);

%solve for centered y-coordinates
[y_hat, y_bar] = column_mean_helper(y, m, B);

%solve for centered X-coordinates
X_hat = zeros(m, n);
X_bar = zeros(n, 1);
for i=1:n
    [X_hat_i, X_bar_i] = column_mean_helper(X(:,i), m, B);
    X_hat(:,i) = X_hat_i;
    X_bar(i) = X_bar_i;
end



X_inv = inv(X_hat*(X_hat') + K*I);
w = (X_hat')* X_inv * y_hat;
b = y_bar - (X_bar)'*w;

nw = Euclid_norm(w);
xi = y_hat - X_hat*w;
nxi = Euclid_norm(xi);
end
