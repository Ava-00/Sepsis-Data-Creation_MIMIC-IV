import pandas as pd
file_path = r"C:\Users\avant\Downloads\physionet.org\files\mimiciv\3.1\hosp\d_icd_diagnoses.csv.gz"

# Read the compressed CSV file
df = pd.read_csv(file_path, compression='gzip')

# Display the first few rows of the DataFrame
print(df.head())
df.shape

#Obtain data with sepsis only 
filtered_df = df[df.apply(lambda row: row.astype(str).str.contains('sepsis', case=False, na=False).any(), axis=1)]
filtered_df.shape

#Use dataframe with subject IDs and sepsis ICD codes 
admit_file_path = r"C:\Users\avant\Downloads\physionet.org\files\mimiciv\3.1\hosp\diagnoses_icd.csv.gz"
admit_df = pd.read_csv(admit_file_path, compression='gzip')
admit_df.head()
merged_df = pd.merge(admit_df, filtered_df, on=('icd_code', 'icd_version'), how='inner')
merged_df.shape
merged_df.head() 

#Import additional patient data 
patients_file_path = r"C:\Users\avant\Downloads\patients (1).csv.gz"
patients_df = pd.read_csv(patients_file_path, compression='gzip')
patients_df.head()
patients_df.shape
patient_merged_df = pd.merge(merged_df, patients_df, on='subject_id', how='inner')
patient_merged_df.shape

#Import admission data 
admissions_file_path = r"C:\Users\avant\Downloads\admissions.csv.gz"
admissions_df = pd.read_csv(admissions_file_path, compression='gzip')
admissions_df.head()
admissions_df.shape
admissions_merged_df = pd.merge(patient_merged_df, admissions_df, on='subject_id', how='inner')
admissions_merged_df.shape

#Import lab events 
labevents_path = r"C:\Users\avant\Downloads\labevents.csv.gz"
labevents_df = pd.read_csv(labevents_path, compression='gzip')
labevents_df.head()
labevents_df.shape
labevents_merged_df = pd.merge(labevents_df, patient_merged_df, on='subject_id', how='inner')
labevents_merged_df.shape


# #Import additional columns 
# drg_codes_path = r"C:\Users\avant\Downloads\drgcodes.csv.gz"
# drg_df = pd.read_csv(drg_codes_path, compression='gzip')
# drg_df.head()
# merged_v1_df = pd.merge(drg_df, merged_df, on='subject_id', how='inner')
# merged_v1_df.shape
# #visualize this data in a table 
# merged_v1_df.head()

# #Import additional columns
# transfers_path = r"C:\Users\avant\Downloads\transfers.csv.gz"
# transfers_df = pd.read_csv(transfers_path, compression='gzip')
# transfers_df.head()
# merged_v2_df = pd.merge(transfers_df, patient_merged_df, on='subject_id', how='inner')
# merged_v2_df.shape
# #visualize this data in a table
# merged_v2_df.head()

# #Import additional columns
# microbiologyevents_path = r"C:\Users\avant\Downloads\microbiologyevents.csv.gz"
# microbiologyevents_df = pd.read_csv(microbiologyevents_path, compression='gzip')
# microbiologyevents_df.head()
# merged_v3_df = pd.merge(microbiologyevents_df, patient_merged_df, on='subject_id', how='inner')  
# merged_v3_df.shape
# #visualize this data in a table 
# merged_v3_df.head()
# merged_v3_df.to_csv(r"C:\Users\avant\Downloads\sepsis_data.csv", index=False)

# #Import additional columns 
# icustays_path = r"C:\Users\avant\Downloads\icustays.csv.gz"
# icustays_df = pd.read_csv(icustays_path, compression='gzip')
# icustays_df.head()
# merged_v4_df = pd.merge(icustays_df, patient_merged_df, on='subject_id', how='inner')
# merged_v4_df.shape
# #visualize this data in a table
# merged_v4_df.head()
# merged_v4_df.to_csv(r"C:\Users\avant\Downloads\sepsis_data_icu.csv", index=False)

# #Import additional columns
# emar_path = r"C:\Users\avant\Downloads\emar.csv.gz"
# emar_df = pd.read_csv(emar_path, compression='gzip')
# emar_df.head()
# merged_v5_df = pd.merge(emar_df, patient_merged_df, on='subject_id', how='inner')
# merged_v5_df.shape
# #visualize this data in a table
# merged_v5_df.head()
# merged_v5_df.to_csv(r"C:\Users\avant\Downloads\sepsis_data_emar.csv", index=False)

# #Import additional columns
# proceddureevents_path = r"C:\Users\avant\Downloads\procedureevents.csv.gz"
# proceddureevents_df = pd.read_csv(proceddureevents_path, compression='gzip')
# proceddureevents_df.head()
# merged_v6_df = pd.merge(proceddureevents_df, patient_merged_df, on='subject_id', how='inner')
# merged_v6_df.shape  
# #visualize this data in a table
# merged_v6_df.head()
# merged_v6_df.to_csv(r"C:\Users\avant\Downloads\sepsis_data_procedure.csv", index=False)
