
%gets the ud and ld from a matrix of size 2 x n and returns 
% a ud and ld of size 1 x (2n -1)

function [rx, ry] = deboor_segments(dx, dy)

%get the number of control points, control segments and allocate space
my_sizes = size(dx);
my_size = my_sizes(1);
num_ctrl_segs = my_size - 3;
x = zeros(num_ctrl_segs - 1, 2);
y = zeros(num_ctrl_segs - 1, 2);

%get first and last midpoints and store just the first one
first_midpoint_x = (dx(2) + dx(3))/2;
last_midpoint_x = (dx(my_size - 1) + dx(my_size - 2))/2;
first_midpoint_y = (dy(2) + dy(3))/2;
last_midpoint_y = (dy(my_size - 1) + dy(my_size - 2))/2;
x(1,1) = first_midpoint_x ;
y(1,1) = first_midpoint_y;

% get the 1/3, 2/3 to get the middle section 
for i=3:my_size - 3
   one_thirds_x = dx(i) * 2/3 + dx(i+1) * 1/3;
   two_thirds_x = dx(i) * 1/3 + dx(i+1) * 2/3;
   one_thirds_y = dy(i) * 2/3 + dy(i+1) * 1/3;
   two_thirds_y = dy(i) * 1/3 + dy(i+1) * 2/3;
   x(i - 2, 2) = one_thirds_x;
   x(i - 1, 1) = two_thirds_x;
   y(i - 2, 2) = one_thirds_y;
   y(i - 1, 1) = two_thirds_y;

end
x(num_ctrl_segs - 1, 2) = last_midpoint_x;
y(num_ctrl_segs - 1, 2) = last_midpoint_y;


%get midpoints for the edges
size_of_x = size(x);
t = zeros(size_of_x(1), 1);
s = zeros(size_of_x(1), 1);
for i=1:size_of_x(1)
    t(i) = (x(i, 1) + x(i, 2))/2;
    s(i) = (y(i, 1) + y(i, 2))/2;
end


%allocate space to store our data
rx = zeros(num_ctrl_segs, 4);
ry = zeros(num_ctrl_segs, 4);

%store the copy past parts
rx(1, 1) = dx(1);
rx(1, 2) = dx(2);
rx(num_ctrl_segs, 3) = dx(my_size - 1);
rx(num_ctrl_segs, 4) = dx(my_size);

ry(1, 1) = dy(1);
ry(1, 2) = dy(2);
ry(num_ctrl_segs, 3) = dy(my_size - 1);
ry(num_ctrl_segs, 4) = dy(my_size);

for l=2:num_ctrl_segs
    rx(l - 1, 4) = t(l - 1);
    rx(l, 1) = t(l - 1);
    rx(l, 2) = x(l -1, 2);
    rx(l - 1, 3) = x(l - 1, 1);

    ry(l - 1, 4) = s(l - 1);
    ry(l, 1) = s(l - 1);
    ry(l, 2) = y(l -1, 2);
    ry(l - 1, 3) = y(l - 1, 1);
end







