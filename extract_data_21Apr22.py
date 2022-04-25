import pandas as pd

def extract_data_10ml():
    #10 ml @ 6.2 V

    df_10ml_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_1.csv")
    d = {'Voltage_1': df_10ml_1['Voltage_1'][0:11000], 'Voltage_2': df_10ml_1['Voltage_2'][0:11000]}
    df_10ml_1 = pd.DataFrame(data=d)
    df_10ml_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_2.csv")
    df_10ml_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_3.csv")
    df_10ml_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_4.csv")
    df_10ml_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_5.csv")
    df_10ml_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_6.csv")
    d6 = {'Voltage_1': df_10ml_6['Voltage_1'][150:11150], 'Voltage_2': df_10ml_6['Voltage_2'][150:11150]}
    df_10ml_6 = pd.DataFrame(data=d6)
    df_10ml_7 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_7.csv")
    df_10ml_8 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_8.csv")
    df_10ml_9 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_9.csv")
    df_10ml_10 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_10.csv")
    return df_10ml_1,df_10ml_2,df_10ml_3,df_10ml_4,df_10ml_5,df_10ml_6,df_10ml_7,df_10ml_8,df_10ml_9,df_10ml_10

def extract_data_15ml():
    #15 ml @ 6.2 V
    df_15ml_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_11.csv")
    df_15ml_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_12.csv")
    df_15ml_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_13.csv")
    df_15ml_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_14.csv")
    df_15ml_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_15.csv")
    d5 = {'Voltage_1': df_15ml_5['Voltage_1'][100:11100], 'Voltage_2': df_15ml_5['Voltage_2'][100:11100]}
    df_15ml_5 = pd.DataFrame(data=d5)
    df_15ml_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_16.csv")
    df_15ml_7 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_17.csv")
    df_15ml_8 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_18.csv")
    df_15ml_9 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_19.csv")
    df_15ml_10 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_20.csv")
    return df_15ml_1,df_15ml_2,df_15ml_3,df_15ml_4,df_15ml_5,df_15ml_6,df_15ml_7,df_15ml_8,df_15ml_9,df_15ml_10

def extract_data_20ml():
    #20 ml @ 6.2 V
    df_20ml_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_21.csv")
    df_20ml_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_22.csv")
    df_20ml_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_23.csv")
    df_20ml_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_24.csv")
    df_20ml_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_25.csv")
    d5 = {'Voltage_1': df_20ml_5['Voltage_1'][150:11150], 'Voltage_2': df_20ml_5['Voltage_2'][150:11150]}
    df_20ml_5 = pd.DataFrame(data=d5)    
    df_20ml_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_26.csv")
    df_20ml_7 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_27.csv")
    df_20ml_8 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_28.csv")
    df_20ml_9 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_29.csv")
    df_20ml_10 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_30.csv")
    d10 = {'Voltage_1': df_20ml_10['Voltage_1'][180:11180], 'Voltage_2': df_20ml_10['Voltage_2'][180:11180]}
    df_20ml_10 = pd.DataFrame(data=d10)
    return df_20ml_1,df_20ml_2,df_20ml_3,df_20ml_4,df_20ml_5,df_20ml_6,df_20ml_7,df_20ml_8,df_20ml_9,df_20ml_10

def extract_data_25ml():
    #25 ml @ 6.2 V
    df_25ml_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_31.csv")
    df_25ml_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_32.csv")
    df_25ml_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_33.csv")
    df_25ml_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_34.csv")
    df_25ml_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_35.csv")
    df_25ml_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_36.csv")
    df_25ml_7 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_37.csv")
    df_25ml_8 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_38.csv")
    df_25ml_9 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_39.csv")
    df_25ml_10 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_40.csv")
    return df_25ml_1,df_25ml_2,df_25ml_3,df_25ml_4,df_25ml_5,df_25ml_6,df_25ml_7,df_25ml_8,df_25ml_9,df_25ml_10

def extract_data_30ml():
    #30 ml @ 6.2 V
    df_30ml_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_41.csv")
    df_30ml_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_42.csv")
    df_30ml_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_43.csv")
    df_30ml_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_44.csv")
    df_30ml_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_45.csv")
    d5 = {'Voltage_1': df_30ml_5['Voltage_1'][100:11100], 'Voltage_2': df_30ml_5['Voltage_2'][100:11100]}
    df_30ml_5 = pd.DataFrame(data=d5)
    df_30ml_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_46.csv")
    df_30ml_7 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_47.csv")
    df_30ml_8 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_48.csv")
    df_30ml_9 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_49.csv")
    df_30ml_10 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_50.csv")
    return df_30ml_1,df_30ml_2,df_30ml_3,df_30ml_4,df_30ml_5,df_30ml_6,df_30ml_7,df_30ml_8,df_30ml_9,df_30ml_10


def extract_data_35ml():
    #35 ml @ 6.2 V
    df_35ml_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_51.csv")
    df_35ml_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_52.csv")
    df_35ml_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_53.csv")
    df_35ml_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_54.csv")
    df_35ml_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_55.csv")
    df_35ml_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_56.csv")
    df_35ml_7 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_57.csv")
    df_35ml_8 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_58.csv")
    df_35ml_9 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_59.csv")
    df_35ml_10 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_60.csv")
    return df_35ml_1,df_35ml_2,df_35ml_3,df_35ml_4,df_35ml_5,df_35ml_6,df_35ml_7,df_35ml_8,df_35ml_9,df_35ml_10


def extract_data_40ml():
    #40 ml @ 6.2 V
    df_40ml_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_61.csv")
    df_40ml_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_62.csv")
    df_40ml_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_63.csv")
    df_40ml_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_64.csv")
    df_40ml_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_65.csv")
    df_40ml_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_67.csv")
    df_40ml_7 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_68.csv")
    df_40ml_8 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_69.csv")
    df_40ml_9 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_70.csv")
    df_40ml_10 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_71.csv")
    return df_40ml_1,df_40ml_2,df_40ml_3,df_40ml_4,df_40ml_5,df_40ml_6,df_40ml_7,df_40ml_8,df_40ml_9,df_40ml_10

def extract_data_45ml():
    #45 ml @ 6.2 V
    df_45ml_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_74.csv")
    df_45ml_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_75.csv")
    df_45ml_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_76.csv")
    df_45ml_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_77.csv")
    df_45ml_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_78.csv")
    df_45ml_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_79.csv")
    df_45ml_7 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_80.csv")
    df_45ml_8 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_81.csv")
    df_45ml_9 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_82.csv")
    df_45ml_10 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_83.csv")
    return df_45ml_1,df_45ml_2,df_45ml_3,df_45ml_4,df_45ml_5,df_45ml_6,df_45ml_7,df_45ml_8,df_45ml_9,df_45ml_10

def extract_data_50ml():
    #50 ml @ 6.2 V
    df_50ml_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_84.csv")
    d1 = {'Voltage_1': df_50ml_1['Voltage_1'][300:11300], 'Voltage_2': df_50ml_1['Voltage_2'][300:11300]}
    df_50ml_1 = pd.DataFrame(data=d1)
    df_50ml_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_85.csv")
    d2 = {'Voltage_1': df_50ml_2['Voltage_1'][200:11200], 'Voltage_2': df_50ml_2['Voltage_2'][200:11200]}
    df_50ml_2 = pd.DataFrame(data=d2)
    df_50ml_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_86.csv")
    df_50ml_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_87.csv")
    df_50ml_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_88.csv")
    df_50ml_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_89.csv")
    df_50ml_7 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_90.csv")
    df_50ml_8 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_91.csv")
    df_50ml_9 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_92.csv")
    df_50ml_10 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_93.csv")
    d10 = {'Voltage_1': df_50ml_10['Voltage_1'][200:11200], 'Voltage_2': df_50ml_10['Voltage_2'][200:11200]}
    df_50ml_10 = pd.DataFrame(data=d10)
    return df_50ml_1,df_50ml_2,df_50ml_3,df_50ml_4,df_50ml_5,df_50ml_6,df_50ml_7,df_50ml_8,df_50ml_9,df_50ml_10

def extract_data_55ml():
    #55 ml @ 6.2 V
    df_55ml_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_94.csv")
    df_55ml_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_95.csv")
    df_55ml_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_96.csv")
    df_55ml_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_97.csv")
    df_55ml_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_98.csv")
    df_55ml_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_99.csv")
    df_55ml_7 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_100.csv")
    df_55ml_8 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_101.csv")
    df_55ml_9 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\backup_102.csv")
    df_55ml_10 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\exp21Apr22\csv\phantom.csv")
    return df_55ml_1,df_55ml_2,df_55ml_3,df_55ml_4,df_55ml_5,df_55ml_6,df_55ml_7,df_55ml_8,df_55ml_9,df_55ml_10

