function [norm] = Euclid_norm(data)
s = size(data);
current = 0;

for i=1:s
    current = current + data(i)^2;
end
norm = sqrt(current);

end

