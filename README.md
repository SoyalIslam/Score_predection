# 📚 Student Score Prediction using Machine Learning

This project predicts a student's **exam score** based on:
- 🎯 Attendance  
- 🧠 Previous Score  
- ⏱️ Hours Studied  

It uses various ML models like **Linear Regression**, **Random Forest**, and **XGBoost**, and includes **hyperparameter tuning** and a **Streamlit web app** for easy interaction.

---

## 🚀 Features

- Train & compare multiple regression models  
- Evaluate using R², MAE, MSE  
- Visualizations: heatmap, pairplots, scatter plots, box plots  
- Hyperparameter tuning with GridSearchCV & RandomizedSearchCV  
- Streamlit web interface using `basemodel.pkl`

---

## 🛠️ Tech Stack

- Python
- Scikit-learn
- XGBoost
- Pandas, NumPy
- Seaborn, Matplotlib
- Streamlit
- Joblib

---

## 🧪 Model Training

### Models Used:
- `LinearRegression`
- `Ridge`
- `RandomForestRegressor`
- `DecisionTreeRegressor`
- `SVR`
- `XGBRegressor`

### Evaluation Metrics:
- R² Score  
- MAE (Mean Absolute Error)  
- MSE (Mean Squared Error)

---

## 📊 Visualizations

- Correlation Heatmap
- Pairplot
- Scatterplots (feature vs. target)
- Boxplots (outliers)

---

## 🌐 Streamlit Web App

### Run the App:

```bash
streamlit run streamlit_app.py
