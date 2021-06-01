import csv
import pandas as pd
import statistics

df = pd.read_csv("StudentsPerformance.csv")
math_data = df["math score"].tolist()
mean = statistics.mean(math_data)
print(mean)
sd = statistics.stdev(math_data)
print(sd)

math_first_std_deviation_start, math_first_std_deviation_end = mean-sd, mean+sd
math_second_std_deviation_start, math_second_std_deviation_end = mean-(2*sd), mean+(2*sd)
math_third_std_deviation_start, math_third_std_deviation_end = mean-(3*sd), mean+(3*sd)
print(math_first_std_deviation_start, math_first_std_deviation_end)
print(math_second_std_deviation_start, math_second_std_deviation_end)
print(math_third_std_deviation_start, math_third_std_deviation_end)