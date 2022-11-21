% function to draw a Bezier segment
% using de Casteljau subdivision
% nn = level of subdivision
% used by bspline4_dc
% also plots the Bezier control polygons if drawb = 1
%
function drawbezier_dc(B,nn,drawb)
 % nn is the subdivision level

 %%% DRAW CURVE HERE %%% 
 [x, y] = subdiv_helper1a(B(1,:), B(2,:), 6);
 plot(x, y)
 plot(B(1,:), B(2, :), "r");
 plot(B(1,:), B(2, :), "r+");

 % Plot the curve segment as a random color
 if drawb == 1 
    %%% Plot the Bezier points and segments  as red + %%%
 else
    %%% Plot the Bezier points as red + %%%
 end
end

