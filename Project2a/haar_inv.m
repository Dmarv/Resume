%
%  Program to compute the coefficients of a sequence of length 2^n given its
%  coefficients over the Haar basis
%
function [u] = haar_inv(c)
c = c';
s = size(c);
n = s(1);
l_n = ceil(log2(n));
u = zeros(size(c));

for j=0:l_n -1
    for i=1:2^j
        u(2*i -1) = c(i) + c(2^j + i);
        u(2*i) = c(i) - c(2^j + i);
    end
    for k=2^(j+1) + 1:n
        u(k) = c(k);
    end

    c = u;
end
u = u';
end 
