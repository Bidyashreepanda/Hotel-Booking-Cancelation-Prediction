
import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

# Load saved model
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "hotel_cancellation_model.pkl"

model_bundle = joblib.load(MODEL_PATH)

preprocessor = model_bundle["preprocessor"]
model = model_bundle["model"]

# Page configuration
st.set_page_config(
    page_title="Hotel Booking Cancellation Prediction",
    page_icon="🏨",
    layout="wide"
)

# Application title
st.title("🏨 Hotel Booking Cancellation Prediction")

st.write(
    "A Machine Learning application to predict "
    "whether a hotel booking is likely to be cancelled."
)

st.divider()

st.success("Machine Learning model loaded successfully!")

st.subheader("About this project")

st.write("""
This project uses Machine Learning classification algorithms
to predict hotel booking cancellations.

The final model is selected based on its performance,
especially the F1-score and recall for cancelled bookings.
""")

st.subheader("Enter Hotel Booking Details")

# Get column names from fitted preprocessor
numeric_cols = list(preprocessor.transformers_[0][2])
categorical_cols = list(preprocessor.transformers_[1][2])

# Get categories learned during training
cat_encoder = preprocessor.named_transformers_["cat"]
cat_categories = cat_encoder.categories_

# Create booking form
with st.form("booking_form"):

    input_data = {}

    st.write("### Numerical Details")

    for col in numeric_cols:
        default_value = 0.0

        # Use training mean as the initial value, if available
        scaler = preprocessor.named_transformers_["num"]
        if hasattr(scaler, "mean_"):
            idx = numeric_cols.index(col)
            default_value = float(scaler.mean_[idx])

        input_data[col] = st.number_input(
            col.replace("_", " ").title(),
            value=default_value
        )

    st.write("### Categorical Details")

    for col, categories in zip(categorical_cols, cat_categories):

        # Remove missing category values
        options = [
            value for value in categories
            if pd.notna(value)
        ]

        if options:
            input_data[col] = st.selectbox(
                col.replace("_", " ").title(),
                options=options
            )

    submitted = st.form_submit_button(
        "Predict Booking Cancellation"
    )

# Make prediction
if submitted:

    input_df = pd.DataFrame([input_data])

    processed_data = preprocessor.transform(input_df)

    prediction = model.predict(processed_data)[0]

    st.divider()
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("This booking is predicted to be CANCELLED.")
    else:
        st.success("This booking is predicted NOT to be cancelled.")

    # Display probability when supported
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(processed_data)[0]

        st.write(
            f"Cancellation probability: {probabilities[1] * 100:.2f}%"
        )
