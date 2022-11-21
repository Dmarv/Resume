%
% Function to compute the coefficients of a sequence u of length 2^n
% over the Haar basis. 
%
function [c] = haar_n(u)
u = u';
s = size(u);
n = s(1);
l_n = ceil(log2(n));
c = zeros(size(u));

for j=l_n - 1:-1:0
    for i=1:2^j
        c(i) = (u(2*i - 1) + u(2*i))/sqrt(2);
        c(2^j + i) = (u(2*i - 1) - u(2*i))/sqrt(2);  
    end
    if j < l_n -1
        for k = (2^(j + 1)) + 1: n
            c(k) = u(k);
        end
    end
    u = c;
end
c = c';
end
