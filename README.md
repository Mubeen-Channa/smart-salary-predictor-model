# 💼 Salary Prediction Model

This project demonstrates a simple **Linear Regression** model built with **scikit-learn** to predict a person's salary based on their years of experience. The model is deployed using **Streamlit** for a clean and interactive web interface.

<br>

## 🌐 Live Demo
🔗 [Visit Website](https://smart-salary-predictor-model-mubeen.streamlit.app/ 
)

<br>

## 📸 Screenshot

![Smart Salary Prediction](SalaryPredictionMLModelScreenshot.png)

<br>

## 📊 Dataset

- Source: [Salary Dataset](https://github.com/Mubeen-Channa/smart-salary-predictor-model/blob/28a3307bf1be99e30dbea52fbf7f7798bab9ef92/salary.csv)
- Contains:
  - `Experience Years`
  - `Salary`

<br>

## 🔧 Technologies Used

- Python  
- Pandas & Matplotlib  
- Scikit-learn  
- Streamlit  
- Pickle (for model serialization)

<br>

## 🧠 Model Workflow

1. **Load Dataset** (online & offline options)
2. **Visualize** the relationship using a scatter plot
3. **Split** data into training and testing sets
4. **Train** a Linear Regression model
5. **Evaluate** model with R² Score and MSE
6. **Serialize** the trained model using `pickle`
7. **Deploy** using `Streamlit`

<br>

## 🚀 How to Run Locally

1. Clone the repository  
2. Install required packages:  
   ```bash
   1. pip install pandas matplotlib scikit-learn streamlit
   2. python -m streamlit run app.py / streamlit run app.py

