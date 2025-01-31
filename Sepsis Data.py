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
labevents_path = r"C:\Users\avant\Downloads\labevents (1).csv"
labevents_df = pd.read_csv(labevents_path)
labevents_df.head()
labevents_df.shape

d_labitems_path = r"C:\Users\avant\Downloads\physionet.org\files\mimiciv\3.1\hosp\d_labitems.csv.gz"
d_labitems = pd.read_csv(d_labitems_path, compression='gzip')
icustays_path = r"C:\Users\avant\Downloads\icustays.csv.gz"
d_labitems = pd.read_csv(d_labitems_path, compression='gzip')
icustays = pd.read_csv(icustays_path, compression='gzip')

# Step 2: Ensure required columns in `d_labitems`
if "itemid" not in d_labitems.columns or "label" not in d_labitems.columns:
    raise ValueError("Missing required columns ('itemid' or 'label') in d_labitems!")

# Step 3: Create a mapping of item IDs to meaningful column names
itemid_mapping = {}
for _, row in d_labitems.iterrows():
    if isinstance(row["label"], str):  # Ensure the label is a string
        variable_name = row["label"].lower().replace(" ", "_").replace("-", "_")
        itemid_mapping[row["itemid"]] = variable_name

print("ItemID Mapping Sample:", list(itemid_mapping.items())[:10])  # Debugging: Print first 10 mappings

#Setting date-time effects
labevents_df["charttime"] = pd.to_datetime(labevents_df["charttime"])
icustays["intime"] = pd.to_datetime(icustays["intime"])
icustays["outtime"] = pd.to_datetime(icustays["outtime"])

# Merge labevents with admissions and ICU stays
labevents_patients = pd.merge(labevents_df,admissions_merged_df, on="subject_id")
labevents_filtered = pd.merge(labevents_patients,icustays, on="subject_id")
labevents_filtered.shape

# Filter based on time range
labevents_filtered = labevents_filtered[
    (labevents_filtered["charttime"] >= labevents_filtered["intime"]) & 
    (labevents_filtered["charttime"] <= labevents_filtered["outtime"])
]

# Step 5: Aggregation of lab results (e.g., using max and min for each `hadm_id`)
aggregated = labevents_filtered.pivot_table(
    index="hadm_id",
    columns="itemid",
    values="valuenum",
    aggfunc={"valuenum": [np.max, np.min]}
)

# Step 6: Flatten MultiIndex columns for easier access
flattened_columns = ['_'.join(map(str, col)).strip() for col in aggregated.columns]
aggregated.columns = flattened_columns

# Step 7: Replace item IDs with meaningful column names
aggregated.columns = [
    itemid_mapping.get(int(col.split('_')[1]), col) if col.split('_')[1].isdigit() else col
    for col in flattened_columns
]

# Step 8: Reset index (if needed)
aggregated.reset_index(inplace=True)

# Debugging: Output the final DataFrame
print("\nAggregated DataFrame with Renamed Columns:\n", aggregated.head())
