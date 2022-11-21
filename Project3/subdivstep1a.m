
%splits the return from subdecas into two 2 x n matrices

function [rx, ry] = subdivstep1a(x, y)
%allocate space
a = size(x);
b = a(2);
c = 2*b - 1;
tx = x;
ty = y;

%get the u and l
[u, l] = subdecas1a(tx, ty);

%break them up into two x
u1 = u(1:b);
l1 = l(1:b);
u2 = u(b:c);
l2 = l(b:c);
%store them in the return
rx = [u1; l1];
ry = [u2; l2];
end
