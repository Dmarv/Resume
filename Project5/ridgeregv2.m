function [w,nw2,b,xi,nxi] = ridgeregv2(X,y,K)
%  Ridge regression minimizing w and b
%  b is penalized
%  X is an m x n matrix, y a m x 1 colum vector
%  weight vector w, intercept b
%  Solution in terms of the primal variables
%  And also in terms of the dual variable alpha
%
m = size(y,1);
n = size(X, 2);
B = ones(m, 1);
I = eye(m);

X1 = [X B];
alpha = inv(X1*X1' + K*I)*y;
w_b = X1'*alpha;
xi = K*alpha;
b = B'*alpha;
w = w_b(1:n);

nw2 = Euclid_norm(w);
nxi = Euclid_norm(xi);

end

