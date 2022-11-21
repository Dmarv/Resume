%
% plots a piecewise linear function corresponding to 
% a vector u = (u_1, ..., u_n)
%

function drawplf(u)
m= size(u,2);
a = zeros(1,m*2);
b = zeros(1,m*2);
j = 1;
for i = 1:m
    if (i == 1)
        a(j)=0;
    else
        a(j) = (i-1)/m;
    end
    a(j+1) = i/m;
    b(j) = u(i);
    b(j+1) = u(i);
    j = j+2;
end

plot(a,b);
end
