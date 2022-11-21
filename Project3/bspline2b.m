%
%  To display a cubic B-sline given by de Boor control points
%   d_0, ..., d_N  
%
% Input points: left click for the d's then press enter (or return, or right click)  
%
%  Performs a loop from 1 to N - 2 to compute the Bezier
%  points using de Casteljau subdivision
%  nn is the subdivision level
%
%  This version also outputs the x-coodinates and the y-coordinates
%  of all the control points of the Bezier segments stored in
%  Bx(N-2,4) and By(N-2,4)
%

function [Bx, By] = bspline2b(dx,dy,N,nn,drawb)
% Works if N >= 4.

 %%% COMPUTE Bx AND By HERE %%%

 [Bx, By] = deboor_segments(dx, dy);

% nn is the subdivision level
% fprintf('numpt = %d \n', numpt)
figure;
dim_data = 2;
B = zeros(dim_data,4);
plot(dx,dy,'or-');   % plots d's as red circles
hold on;
for i = 1:N-2       
    B(1,:) = Bx(i,:); B(2,:) = By(i,:);
    drawbezier_dc(B,nn,drawb);
end
hold off;
end

