import pandas as pd

# Load CSV from a subdirectory
acc_16 = pd.read_csv('US Traffic Acc Project/acc_16.csv')
acc_17 = pd.read_csv('US Traffic Acc Project/acc_17.csv')
acc_18 = pd.read_csv('US Traffic Acc Project/acc_18.csv')
acc_19 = pd.read_csv('US Traffic Acc Project/acc_19.csv')
acc_20 = pd.read_csv('US Traffic Acc Project/acc_20.csv')
pers_16 = pd.read_csv('US Traffic Acc Project/pers_16.csv')
pers_17 = pd.read_csv('US Traffic Acc Project/pers_17.csv')
pers_18 = pd.read_csv('US Traffic Acc Project/pers_18.csv')
pers_19 = pd.read_csv('US Traffic Acc Project/pers_19.csv', encoding='ISO-8859-1')
pers_20 = pd.read_csv('US Traffic Acc Project/pers_20.csv')
veh_16 = pd.read_csv('US Traffic Acc Project/veh_16.csv')
veh_17 = pd.read_csv('US Traffic Acc Project/veh_17.csv')
veh_18 = pd.read_csv('US Traffic Acc Project/veh_18.csv')
veh_19 = pd.read_csv('US Traffic Acc Project/veh_19.csv')
veh_20 = pd.read_csv('US Traffic Acc Project/veh_20.csv')

# Print the first few rows
print(acc_16.head())
print(acc_17.head())
print(acc_18.head())
print(acc_19.head())
print(acc_20.head())
print(veh_16.head())
print(veh_17.head())
print(veh_18.head())
print(veh_19.head())
print(veh_20.head())
print(pers_16.head())
print(pers_17.head())
print(pers_18.head())
print(pers_19.head())
print(pers_20.head())



