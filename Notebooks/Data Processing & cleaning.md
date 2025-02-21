# 🧹 Data Cleaning, Exploratory Data Analysis (EDA) & Feature Selection for AQI Prediction

## 📌 Project Overview
This document explains the **data cleaning, exploratory data analysis (EDA), and feature selection** process for the **AQI Prediction Project**. The goal is to **clean raw AQI data**, handle missing values, detect outliers, explore key patterns, and select the most important features for training the prediction model.

## 📂 Dataset Information
- **Source:** Air Quality Index (AQI) datasets from government agencies, OpenAQ API, or Kaggle.
- **Format:** CSV file containing air pollution readings for different locations.
- **Key Features:**
  - `City`, `Country` → Location details
  - `lat`, `lng` → Geographical coordinates
  - `AQI Value` → Overall air quality index
  - `PM2.5 AQI Value`, `NO2 AQI Value`, `CO AQI Value`, `Ozone AQI Value` → Pollutant-specific AQI levels

---

## 🚀 Steps for Data Cleaning & EDA
### **1️⃣ Load & Inspect Dataset**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("AQI_Historical.csv")

# Check basic info
df.info()
df.head()
```
✅ **This step helps understand dataset size, missing values, and data types.**

---

### **2️⃣ Handle Missing Values**
```python
# Check missing values
print(df.isnull().sum())

# Fill missing values with column mean
df.fillna(df.mean(), inplace=True)

# Drop rows if too many missing values
df.dropna(thresh=5, inplace=True)
```
✅ **Ensures data completeness before analysis.**

---

### **3️⃣ Detect & Handle Outliers**
```python
# Visualize outliers with boxplots
plt.figure(figsize=(10,5))
sns.boxplot(data=df[['AQI Value', 'PM2.5 AQI Value', 'NO2 AQI Value']])
plt.show()

# Remove extreme outliers using IQR method
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

# Filter outliers
df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
```
✅ **Removes extreme AQI values that could distort predictions.**

---

### **4️⃣ Exploratory Data Analysis (EDA)**
#### 🔹 **4.1 Distribution of AQI Values**
```python
plt.figure(figsize=(8,5))
sns.histplot(df['AQI Value'], bins=30, kde=True)
plt.title("AQI Value Distribution")
plt.show()
```
✅ **Shows how AQI values are spread (normal/skewed distribution).**

#### 🔹 **4.2 Correlation Between Pollutants**
```python
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Between AQI Components")
plt.show()
```
✅ **Identifies which pollutants have the most impact on AQI.**

#### 🔹 **4.3 AQI Trends by Location**
```python
plt.figure(figsize=(12,5))
sns.barplot(x='City', y='AQI Value', data=df.sort_values('AQI Value', ascending=False).head(10))
plt.xticks(rotation=45)
plt.title("Top 10 Most Polluted Cities")
plt.show()
```
✅ **Highlights the most polluted locations.**

---

## 🔍 **Feature Selection for AQI Prediction**

### **5️⃣ Feature Importance using Random Forest**
```python
from sklearn.ensemble import RandomForestRegressor

# Define Features and Target
X = df[['PM2.5 AQI Value', 'NO2 AQI Value', 'CO AQI Value', 'Ozone AQI Value']]
y = df['AQI Value']

# Train Random Forest Model
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X, y)

# Get Feature Importances
feature_importance = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)
print(feature_importance)
```
✅ **Ranks the most influential pollutants for AQI prediction.**

### **6️⃣ Correlation-Based Feature Selection**
```python
# Remove features with high correlation
corr_matrix = df.corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

# Drop highly correlated features (threshold > 0.85)
to_drop = [column for column in upper.columns if any(upper[column] > 0.85)]
df_reduced = df.drop(columns=to_drop)

print("Features after correlation-based selection:", df_reduced.columns)
```
✅ **Removes redundant features, keeping only relevant ones.**

---

## 🔥 Next Steps: Preparing Data for Machine Learning
- **Scaling Data:** Normalize features to improve model accuracy.
- **Train-Test Split:** Prepare dataset for training ML models.
- **Hyperparameter Tuning:** Optimize model performance.

🔗 **Looking to contribute?** Fork the repo & help improve the data pipeline! 🚀

#MachineLearning #DataScience #EDA #DataCleaning #AQIPrediction #FeatureSelection

