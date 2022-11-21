function [h] = make_haar_matrix(N)
n = 2^N;

h = zeros(n, n);

for i=1:n
    h(i, 1) = 1;
end


counter = 1;
for j=0:N - 1
    for k=0: 2^j -1 
        counter = counter + 1;
        for i=1:n
            temp = 0;
            if i >= 1 && i <= k*2^(N-j)
                temp = 0;
            elseif i >= k*2^(N-j) + 1 && i <= k*2^(N-j) + 2^(N-j-1)
                temp = 1;
            elseif i >= k*2^(N-j) + 2^(N-j-1) + 1 && i <= (k+1)*2^(N-j)
                temp = -1;
            elseif i >= (k+1)*2^(N-j) + 1 && i < 2^N
                temp = 0;
            end
            h(i, counter) = temp;
        end
    end
end
end




