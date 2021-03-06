import pandas as pd

def extract_data_18ml():
    #18 ml @ 6.2 V
    df_18_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_10.csv")
    df_18_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_11.csv")
    df_18_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_12.csv")
    df_18_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_13.csv")
    df_18_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_14.csv")
    return df_18_1,df_18_2,df_18_3,df_18_4,df_18_5

def extract_data_28ml():
    #28 ml @ 6.2 V
    df_28_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_25.csv")
    df_28_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_26.csv")
    df_28_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_27.csv")
    df_28_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_28.csv")
    df_28_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_29.csv")
    return df_28_1,df_28_2,df_28_3,df_28_4,df_28_5

def extract_data_38ml():
    #38 ml @ 6.2 V
    df_38_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_15.csv")
    df_38_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_16.csv")
    df_38_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_17.csv")
    df_38_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_18.csv")
    df_38_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_19.csv")
    return df_38_1,df_38_2,df_38_3,df_38_4,df_38_5

def extract_data_48ml():
    #48 ml @ 6.2 V
    df_48_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_20.csv")
    df_48_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_21.csv")
    df_48_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_22.csv")
    df_48_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_23.csv")
    df_48_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_24.csv")
    return df_48_1,df_48_2,df_48_3,df_48_4,df_48_5


def extract_data_7V2():
    # Changing Voltage
    #28 ml @ 7.2 V
    df_28_7_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_30.csv")
    df_28_7_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_31.csv")
    df_28_7_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_32.csv")
    df_28_7_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_33.csv")
    df_28_7_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_34.csv")
    df_28_7_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_35.csv")
    return df_28_7_1,df_28_7_2,df_28_7_3,df_28_7_4,df_28_7_5

def extract_data_5V2():
    #28 ml @ 5.2 V
    df_28_5_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_37.csv")
    df_28_5_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_38.csv")
    df_28_5_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_39.csv")
    df_28_5_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_40.csv")
    df_28_5_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_41.csv")
    return df_28_5_1,df_28_5_2,df_28_5_3[500:5500],df_28_5_4,df_28_5_5