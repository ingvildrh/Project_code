format long

B = readmatrix('execution_time.txt');
python_times = B
python_times = python_times(2:101)./1000000


f = figure("Name", "myfig");
plot(python_times);
hold on;
plot(tosave);
hold off;
legend('Python','Matlab')
title('Execution time');
ylabel('time [seconds]')
xlabel('step')
%ylim([0, 0.004])
grid
saveas(f,"python_vs_matlab.png")