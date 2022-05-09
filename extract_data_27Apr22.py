import pandas as pd

def extract_data_6V():
    #10 ml @ 6.2 V

    df_6V_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup.csv")
    # d = {'Voltage_1': df_6V_1['Voltage_1'][0:11000], 'Voltage_2': df_6V_1['Voltage_2'][0:11000]}
    # df_6V_1 = pd.DataFrame(data=d)
    df_6V_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_1.csv")
    df_6V_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_2.csv")
    df_6V_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_3.csv")
    df_6V_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_4.csv")
    df_6V_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_5.csv")
    # d6 = {'Voltage_1': df_6V_6['Voltage_1'][150:11150], 'Voltage_2': df_6V_6['Voltage_2'][150:11150]}
    # df_6V_6 = pd.DataFrame(data=d6)
    df_6V_7 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_6.csv")
    df_6V_8 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_7.csv")
    df_6V_9 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_8.csv")
    df_6V_10 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_9.csv")
    return df_6V_1,df_6V_2,df_6V_3,df_6V_4,df_6V_5,df_6V_6,df_6V_7,df_6V_8,df_6V_9,df_6V_10

def extract_data_7V():
    #15 ml @ 6.2 V
    df_7V_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_10.csv")
    df_7V_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_11.csv")
    df_7V_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_12.csv")
    df_7V_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_13.csv")
    df_7V_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_14.csv")
    # d5 = {'Voltage_1': df_7V_5['Voltage_1'][100:11100], 'Voltage_2': df_7V_5['Voltage_2'][100:11100]}
    # df_7V_5 = pd.DataFrame(data=d5)
    df_7V_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_15.csv")
    df_7V_7 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_16.csv")
    df_7V_8 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_17.csv")
    df_7V_9 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_18.csv")
    df_7V_10 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_19.csv")
    # d10 = {'Voltage_1': df_7V_10['Voltage_1'][150:11100], 'Voltage_2': df_7V_10['Voltage_2'][150:11100]}
    # df_7V_10 = pd.DataFrame(data=d10)
    return df_7V_1,df_7V_2,df_7V_3,df_7V_4,df_7V_5,df_7V_6,df_7V_7,df_7V_8,df_7V_9,df_7V_10

def extract_data_8V():
    #20 ml @ 6.2 V
    df_8V_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_20.csv")
    # d1 = {'Voltage_1': df_8V_1['Voltage_1'][750:11150], 'Voltage_2': df_8V_1['Voltage_2'][750:11150]}
    # df_8V_1 = pd.DataFrame(data=d1)   
    df_8V_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_21.csv")
    df_8V_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_22.csv")
    df_8V_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_23.csv")
    df_8V_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_24.csv")
    # d5 = {'Voltage_1': df_8V_5['Voltage_1'][620:11150], 'Voltage_2': df_8V_5['Voltage_2'][620:11150]}
    # df_8V_5 = pd.DataFrame(data=d5)        
    df_8V_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_25.csv")
    df_8V_7 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_26.csv")
    df_8V_8 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_27.csv")
    df_8V_9 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_28.csv")
    d9 = {'Voltage_1': df_8V_9['Voltage_1'][150:11000], 'Voltage_2': df_8V_9['Voltage_2'][150:11000]}
    df_8V_9 = pd.DataFrame(data=d9)
    df_8V_10 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_29.csv")
    # d10 = {'Voltage_1': df_8V_10['Voltage_1'][180:11180], 'Voltage_2': df_8V_10['Voltage_2'][180:11180]}
    # df_8V_10 = pd.DataFrame(data=d10)
    return df_8V_1,df_8V_2,df_8V_3,df_8V_4,df_8V_5,df_8V_6,df_8V_7,df_8V_8,df_8V_9,df_8V_10

def extract_data_9V():
    #25 ml @ 6.2 V
    df_9V_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_30.csv")
    d1 = {'Voltage_1': df_9V_1['Voltage_1'][180:11000], 'Voltage_2': df_9V_1['Voltage_2'][180:11000]}
    df_9V_1 = pd.DataFrame(data=d1)
    df_9V_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_31.csv")
    df_9V_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_32.csv")
    df_9V_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_33.csv")
    df_9V_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_34.csv")
    df_9V_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_35.csv")
    df_9V_7 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_36.csv")
    df_9V_8 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_37.csv")
    df_9V_9 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_38.csv")
    d9 = {'Voltage_1': df_9V_9['Voltage_1'][170:11000], 'Voltage_2': df_9V_9['Voltage_2'][170:11000]}
    df_9V_9 = pd.DataFrame(data=d9)
    df_9V_10 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_39.csv")
    return df_9V_1,df_9V_2,df_9V_3,df_9V_4,df_9V_5,df_9V_6,df_9V_7,df_9V_8,df_9V_9,df_9V_10

def extract_data_10V():
    #30 ml @ 6.2 V
    df_10V_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_40.csv")
    df_10V_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_41.csv")
    df_10V_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_42.csv")
    df_10V_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_43.csv")
    df_10V_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_44.csv")
    df_10V_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_45.csv")
    # d6 = {'Voltage_1': df_10V_6['Voltage_1'][600:11000], 'Voltage_2': df_10V_6['Voltage_2'][600:11000]}
    # df_10V_6 = pd.DataFrame(data=d6)
    df_10V_7 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_46.csv")
    df_10V_8 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_47.csv")
    # d8 = {'Voltage_1': df_10V_8['Voltage_1'][130:11000], 'Voltage_2': df_10V_8['Voltage_2'][130:11000]}
    # df_10V_8 = pd.DataFrame(data=d8)
    df_10V_9 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_48.csv")
    df_10V_10 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_49.csv")
    return df_10V_1,df_10V_2,df_10V_3,df_10V_4,df_10V_5,df_10V_6,df_10V_7,df_10V_8,df_10V_9,df_10V_10


def extract_data_11V():
    #35 ml @ 6.2 V
    df_11V_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_50.csv")
    df_11V_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_51.csv")
    df_11V_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_52.csv")
    df_11V_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_53.csv")
    df_11V_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_54.csv")
    df_11V_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_55.csv")
    df_11V_7 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_56.csv")
    df_11V_8 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_57.csv")
    df_11V_9 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_58.csv")
    d9 = {'Voltage_1': df_11V_9['Voltage_1'][120:11000], 'Voltage_2': df_11V_9['Voltage_2'][120:11000]}
    df_11V_9 = pd.DataFrame(data=d9)
    df_11V_10 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_59.csv")
    return df_11V_1,df_11V_2,df_11V_3,df_11V_4,df_11V_5,df_11V_6,df_11V_7,df_11V_8,df_11V_9,df_11V_10


def extract_data_12V():
    #40 ml @ 6.2 V
    df_12V_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_60.csv")
    df_12V_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_61.csv")
    df_12V_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_62.csv")
    df_12V_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_63.csv")
    df_12V_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_64.csv")
    df_12V_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_65.csv")
    df_12V_7 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_66.csv")
    df_12V_8 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_67.csv")
    # d8 = {'Voltage_1': df_12V_8['Voltage_1'][180:11000], 'Voltage_2': df_12V_8['Voltage_2'][180:11000]}
    # df_12V_8 = pd.DataFrame(data=d8)
    df_12V_9 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_68.csv")
    df_12V_10 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp27Apr22\csv\backup_69.csv")
    return df_12V_1,df_12V_2,df_12V_3,df_12V_4,df_12V_5,df_12V_6,df_12V_7,df_12V_8,df_12V_9,df_12V_10
