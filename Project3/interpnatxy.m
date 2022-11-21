function [dx, dy, Bx, By] = interpnatxy(x,y, show_plot)
% This version uses the natural end condition
% Uses Matlab \ to solve linear systems
% Input points: two column vectors of x and y coordinates of dim N+1
%
%  This version uses x_0, x_1, ..., x_{N-1}, x_N to compute the Bezier
%  points and the subdivision version of the de Casteljau algorithm
%  to plot the Bezier segments (bspline2b and drawbezier_dc)
%
%  This version outputs the x and y coordinates dx and dy of the de Boor control
%  points d_{-1}, d_0, d_1, ..., d_{N+1} as column vectors
%  and the x and y coordinates of the Bezier control polygons
%  Bx and By
%
% Uses bspline2b from project 1b

 %%% COMPUTE dx, dy, Bx, By HERE %%%
 t = size(x);
 s = t(1);
 A = linear_sys_helper(s - 2);

 input_x = 6 * x(2:s-1);
 input_x(1) = input_x(1) - x(1);
 input_x(s-2) = input_x(s-2) - x(s);

 input_y = 6 * y(2:s-1);
 input_y(1) = input_y(1) - y(1);
 input_y(s-2) = input_y(s-2) - y(s);

 tx = A\input_x;
 ty = A\input_y;

 dx = zeros(1, s+2);
 dy = zeros(1, s+2);

 dx(3:s) = tx;
 dx(1) = x(1);
 dx(2) = 2/3*x(1) + 1/3*dx(3);
 dx(s+1) = 1/3*dx(s) + 2/3*x(s);
 dx(s+2) = x(s);

 dy(3:s) = ty;
 dy(1) = y(1);
 dy(2) = 2/3*y(1) + 1/3*dy(3);
 dy(s+1) = 1/3*dy(s) + 2/3*y(s);
 dy(s+2) = y(s);
 
 dx = dx';
 dy = dy';



% Plots the spline
if show_plot
  Nx = size(dx,1)-1;
  fprintf('Nx = %d \n', Nx)
  nn = 6; % subdivision level
  drawb = true;
  [Bx, By] = bspline2b(dx,dy,Nx,nn,true);
  hold on
  plot(x,y,'b+'); % Plot x's as blue +
  hold off;
end
end
