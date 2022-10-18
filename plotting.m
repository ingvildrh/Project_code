

fileID = fopen('execution_time.txt', 'r');
formatSpec = '%c';
A = fscanf(fileID,formatSpec);
B = readmatrix('execution_time.txt');
python_times = B
python_times = python_times(2:101)./1000000


f = figure("Name", "myfig")
plot(python_times);
hold on;
plot(tosave);
hold off;
legend('python','matlab')
title('Execution time');
ylabel('time [seconds]')
xlabel('step')
%ylim([0, 0.004])
grid
saveas(f,"python_vs_matlab.png")