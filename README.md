This program follows specific steps for preparing and cleaning the dataset file, which aims to classify patients as either healthy or having Parkinson’s disease. It provides data on various tasks performed by different patients and their durations.

However, the data is quite noisy, with small inconsistencies, missing values, and outliers, making implementation challenging.

**Features**

- Handles missing data by identifying and removing entries with null values.
- Decodes task IDs into human readable descriptions.
- Normalizes and standardizes class labels (HOA and PD).
- Converts columns data types for further operations (string to integer).
- Exports the cleaned data to a new file.

**Steps**

**1. Load the dataset**

The dataset is loaded from a CSV file into a Pandas framework for inspection.

**2. Handle missing data**

- Missing values in the **duration** column are replaced with **NaN**.
- Rows with missing values are dropped, as the number of affected rows is insignificant compared to the total.

**3. Decode task description into human readable values**

Numeric task IDs in the **task** column are replaced with descriptive labels.

**4. Clean Class labels**

Class labels are normalized to either HOA (Healthy Older Adults) or PD (Parkinson’s Disease).

**5. Adjust column data types**
After checking each column's datatype, the **duration** column, initially stored as strings, is converted to integers for proper numerical operations.

**6. Export the cleaned dataset**
The cleaned data is saved as a new CSV file.
