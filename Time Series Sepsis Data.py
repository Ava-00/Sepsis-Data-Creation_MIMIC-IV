#Merge sepsis_lab to create time series data 
import pandas as pd
sepsis_vitals = pd.read_csv(r"C:\Users\avant\Downloads\sepsis_data_lab.csv")
lab_events = pd.read_csv(r"C:\Users\avant\Downloads\labevents (1).csv")
d_labitems = pd.read_csv(r"C:\Users\avant\Downloads\physionet.org\files\mimiciv\3.1\hosp\d_labitems.csv.gz", compression='gzip')


# Merge lab data with D_ITEMS on 'itemid'
lab_data = pd.merge(lab_events,d_labitems[['itemid', 'label']], on='itemid', how='left')
lab_data.rename(columns={'label': 'vital_name'}, inplace=True)
lab_pivot = lab_data.pivot_table(index=['subject_id', 'hadm_id', 'charttime'], 
                                 columns='vital_name', 
                                 values='valuenum').reset_index()

print(lab_pivot)
lab_pivot.to_csv('lab_pivot.csv', index=False)
#Check file path
import os
file_path = os.path.abspath('lab_pivot.csv')
print(file_path)


                                
expanded_data = []

# For each row in the sepsis_vitals DataFrame
for index, row in sepsis_vitals.iterrows():
    # Create a time range based on the 'admittime' and 'dischtime'
    time_range = pd.date_range(start=row['admittime'], end=row['dischtime'], freq='h')

    # For each timestamp in the time range, expand the row to create a time series
    for t in time_range:
        expanded_row = {'subject_id': row['subject_id_x'],
                        'hadm_id': row['hadm_id'],
                        'timestamp': t}
        
        # Add all columns (including vitals and other columns) to the expanded row
        for column in sepsis_vitals.columns:
            # We include every column, not excluding anything
            expanded_row[column] = row[column]

        # Append the expanded row to the list
        expanded_data.append(expanded_row)

# Convert the expanded data to a DataFrame
expanded_df = pd.DataFrame(expanded_data)

print(expanded_df)

# Merge the expanded data with the lab events data on subject_id, hadm_id, and timestamp
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
admissions_merged_df.head()

#merge with updated lab data 
final_merged = pd.merge(admissions_merged_df, lab_pivot, on=('subject_id'), how='inner')
final_merged.to_csv('final_merged.csv', index=False)
import os
file_path = os.path.abspath('final_merged.csv')
print(file_path)
final_merged.shape


# Save the final merged data to a new Excel file
merged_data.to_excel('consolidated_sepsis_lab_data.xlsx', index=False)



