function [Ximage] = image_short_cut(image)
clear X map;
load("", 'X');
Ximage = X(1:512, :);
Ximage(:, 510:512) = 50;
figure;
colormap(gray);
imagesc(Ximage);

end

