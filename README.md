# 🏨 Hotel Booking Cancellation Prediction

<p align="center">
  <b>Machine Learning | Python | Scikit-learn | Streamlit</b>
</p>

<p align="center">
  A Machine Learning project that predicts whether a hotel booking is likely to be cancelled using customer and reservation details.
</p>

---

## 📌 Project Overview

Hotel booking cancellations create challenges for hotel management, including revenue loss, room availability issues, and inefficient planning.

This project uses Machine Learning classification algorithms to predict hotel booking cancellations. It analyzes historical booking information and identifies patterns that can help hotels understand cancellation behaviour.

The project also includes an interactive **Streamlit web application** where users can enter booking details and receive cancellation predictions.

## 🎯 Problem Statement

To develop a Machine Learning classification model that predicts whether a hotel reservation will be cancelled or not based on booking-related information.

The objective is to identify potential cancellations and support better hotel resource and reservation management.

## 🎯 Project Objectives

- Perform Exploratory Data Analysis (EDA).
- Clean and preprocess the hotel booking dataset.
- Identify important patterns and relationships in booking data.
- Apply different Machine Learning classification algorithms.
- Evaluate and compare model performance.
- Perform hyperparameter tuning.
- Build an interactive Streamlit application for predictions.

## 📂 Project Structure

```text
Hotel-Booking-Cancellation/
│
├── Hotel_Booking_Cancellation.ipynb
├── app.py
├── hotel_cancellation_model.pkl
├── requirements.txt
└── README.md
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine Learning |
| Streamlit | Web application |
| Joblib | Model serialization |
| Jupyter Notebook | Model development |

## 📊 Project Workflow

### 1. Data Collection
- Used the Hotel Booking Demand dataset.
- Loaded the dataset using Pandas.

### 2. Exploratory Data Analysis (EDA)
- Analyzed dataset structure and statistical information.
- Examined missing values and duplicate records.
- Studied booking cancellation patterns.
- Created visualizations to understand relationships between features.

### 3. Data Cleaning
- Handled missing values.
- Removed duplicate records.
- Checked and handled invalid data.
- Prepared the dataset for Machine Learning.

### 4. Feature Engineering
Created additional features to improve the information available to the models:
- Total Nights
- Total Guests
- Is Family
- Is Weekend Arrival

### 5. Data Preprocessing
- Separated features and target variable.
- Removed data leakage columns.
- Applied One-Hot Encoding to categorical features.
- Applied Standard Scaling to numerical features.
- Split the data into training and testing sets.

### 6. Machine Learning Models

Implemented and compared five classification algorithms:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier
4. K-Nearest Neighbors (KNN)
5. Support Vector Machine (LinearSVC)

### 7. Model Evaluation

Evaluated the models using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Used RandomizedSearchCV for Random Forest hyperparameter tuning and compared the tuned model with the original model.

### 8. Streamlit Application

Developed an interactive web application that allows users to:
- Enter hotel booking information.
- Select numerical and categorical values.
- Predict booking cancellation.
- View the prediction result and cancellation probability when supported by the model.

## 📈 Model Evaluation

The models were compared based on their classification performance.

Special attention was given to **Recall and F1-score for the cancellation class (1)** because identifying potential cancellations is the main objective.

Random Forest was selected as the final model based on the comparison of the original and tuned versions.

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Hotel-Booking-Cancellation-Prediction.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Hotel-Booking-Cancellation-Prediction
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Application

```bash
python -m streamlit run app.py
```

### Step 5: Open in Browser

```text
http://localhost:8501
```

## 📦 Requirements

The project uses the following Python libraries:

```text
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
joblib
```

## 💡 Key Learnings

Through this project, I gained practical experience in:

- Exploratory Data Analysis.
- Data cleaning and preprocessing.
- Feature engineering.
- Encoding and scaling techniques.
- Classification algorithms.
- Model evaluation and comparison.
- Hyperparameter tuning using RandomizedSearchCV.
- Saving and loading Machine Learning models.
- Building interactive applications using Streamlit.

## 🔮 Future Improvements

- Improve model performance through additional feature engineering.
- Explore more advanced classification algorithms.
- Add interactive data visualizations.
- Deploy the Streamlit application online.
- Improve the user interface and user experience.

## 👩‍💻 Author

**Bidyashree Panda**

- GitHub: [Bidyashreepanda](https://github.com/Bidyashreepanda)
- LinkedIn: [Bidyashree Panda](https://www.linkedin.com/in/bidyashree-panda/)

---

<p align="center">
  ⭐ If you find this project interesting, consider giving it a star!
</p>

<p align="center">
  <b>Built with ❤️ using Python and Machine Learning</b>
</p>
