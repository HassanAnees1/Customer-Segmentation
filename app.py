"""
Customer Segmentation Model Deployment with Gradio
This application uses a pre-trained K-Means clustering model to predict customer segments.
"""

import gradio as gr
import joblib
import numpy as np
import subprocess
import sys

def install_requirements():
    """Install required packages if not already installed."""
    try:
        import gradio
    except ImportError:
        print("Installing gradio...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "gradio"])
        import gradio as gr

# Install requirements
install_requirements()

# Load the scaler and KMeans model
try:
    scaler = joblib.load('scaler.pkl')
    kmeans = joblib.load('kmeans_model.pkl')
    print("Models loaded successfully!")
except FileNotFoundError as e:
    print(f"Error loading models: {e}")
    print("Please ensure 'scaler.pkl' and 'kmeans_model.pkl' are in the same directory as this script.")
    sys.exit(1)

# Define the five customer categories based on K-Means clustering results
categories = {
    0: "Standard (Avg. Income, Avg. Spending)",
    1: "Careful (Low Income, Low Spending)", 
    2: "Target (High Income, High Spending)",
    3: "Careless (High Income, Low Spending)",
    4: "Sensible (Low Income, High Spending)"
}

def predict_segment(age, annual_income, spending_score):
    """
    Predicts the customer segment based on input features.
    
    Args:
        age (float): Customer age
        annual_income (float): Annual income in thousands
        spending_score (float): Spending score (1-100)
    
    Returns:
        str: Predicted customer segment category
    """
    try:
        # Prepare input data
        input_data = np.array([[age, annual_income, spending_score]])
        
        # Scale the input data
        input_scaled = scaler.transform(input_data)
        
        # Predict the cluster
        cluster = kmeans.predict(input_scaled)[0]
        
        # Return the category description
        return categories[cluster]
    
    except Exception as e:
        return f"Error in prediction: {str(e)}"

def create_gradio_interface():
    """Create and configure the Gradio interface."""
    
    # Create the interface
    iface = gr.Interface(
        fn=predict_segment,
        inputs=[
            gr.Slider(
                minimum=18, 
                maximum=70, 
                value=30, 
                label="Age",
                info="Customer's age in years"
            ),
            gr.Slider(
                minimum=15, 
                maximum=137, 
                value=60, 
                label="Annual Income (k$)",
                info="Annual income in thousands of dollars"
            ),
            gr.Slider(
                minimum=1, 
                maximum=100, 
                value=50, 
                label="Spending Score (1-100)",
                info="Spending score based on customer behavior"
            )
        ],
        outputs=gr.Textbox(
            label="Predicted Customer Segment",
            info="AI-predicted customer category"
        ),
        title="🛍️ Customer Segmentation Predictor",
        description="""
        This tool predicts customer segments based on age, income, and spending patterns.
        
        **Five Categories:**
        - **Standard**: Average income and spending
        - **Careful**: Low income, low spending (budget-conscious)
        - **Target**: High income, high spending (premium customers)
        - **Careless**: High income, low spending (potential for growth)
        - **Sensible**: Low income, high spending (value-seekers)
        """,
        theme=gr.themes.Soft(),
        examples=[
            [25, 40, 80],  # Young, moderate income, high spending
            [45, 100, 30], # Middle-aged, high income, low spending
            [35, 60, 60],  # Middle-aged, moderate income and spending
            [55, 25, 85],  # Older, low income, high spending
            [30, 80, 75]   # Young adult, high income, high spending
        ]
    )
    
    return iface

def main():
    """Main function to launch the Gradio application."""
    print("Starting Customer Segmentation Predictor...")
    print("Categories available:")
    for key, value in categories.items():
        print(f"  {key}: {value}")
    
    # Create and launch the interface
    iface = create_gradio_interface()
    iface.launch(
        debug=True,
        share=False,  # Set to True if you want to create a public link
        server_name="0.0.0.0",  # Allow external access
        server_port=7860
    )

if __name__ == "__main__":
    main()