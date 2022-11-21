%
% Function to compute the coefficients of a sequence u of length 2^n
% over the Haar basis. Takes the number of averaging steps as parameter
% (level of recursion)
%  
%
function c = haar_step(u,numstep)



u = u';
s = size(u);
n = s(1);
l_n = ceil(log2(n));
c = zeros(size(u));
count = l_n - numstep;

for j=l_n - 1:-1:count
    for i=1:2^j
        c(i) = (u(2*i - 1) + u(2*i))/2;
        c(2^j + i) = (u(2*i - 1) - u(2*i))/2;  
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
