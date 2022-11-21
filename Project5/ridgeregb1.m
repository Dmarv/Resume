function [w,b,xi,nxi,alpha] = ridgeregb1(X,y,K)
%  Ridge regression 
%  b is not penalized
%  Uses the KKT equations
%  X is an m x n matrix, y a m x 1 colum vector
%  weight vector w, intercept b
%  Solution in terms of the dual variables
%  This version does not display the solution
%

m = size(y,1);
n = size(X, 2);
B = ones(m, 1);
X1= X*X' + K*eye(m);
X1_inv = inv(X1);
a = inv(B'*X1_inv*B);

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



mu = a*B'*X1_inv*y;
alpha = X1_inv*(y - mu*B);
w = X'*alpha;
b = mu;
xi = K*alpha;
%xi = y_hat - X_hat*w;

nxi = Euclid_norm(xi);

end
