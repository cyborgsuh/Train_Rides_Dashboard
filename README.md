# Train Ticket Price Prediction 🚆💰

## Overview
This project is a **Train Ticket Price Prediction App** built using **TensorFlow/Keras** for Neural Network,**Streamlit** for UI, and **Plotly** for visualization. The app allows users to predict ticket prices based on various input features, leveraging a trained neural network with an embedding layer for categorical features. 

## Features ✨
- **Interactive Web Interface**: Built with Streamlit for easy access.
- **Data Visualization**: Helps understand price trends and customer behaviour insights.
- **Neural Network Model**: Uses TensorFlow to predict ticket prices.
- **Preprocessing Pipelines**: Handles missing values and encodes categorical data.
- **Multi-Page App**:
  - **Home**: Introduction and dataset overview.
  - **Visualization**: Graphical insights into the data.
  - **Model**: Ticket price prediction interface.

## Tech Stack 🛠️
- **Python** 🐍
- **TensorFlow/Keras** 🤖
- **Streamlit** 🌐
- **Pandas & NumPy** 📊
- **Plotly** 📈

## Installation ⚙️
Clone the repository and install the dependencies:

```bash
git clone https://github.com/cyborgsuh/Train_Rides_Dashboard.git
cd Train_Rides_Dashboard
pip install -r requirements.txt
```

## Running the App 🚀
```bash
streamlit run app.py
```

## Dataset 📂
The dataset includes:
- **Departure & Arrival Locations**
- **Travel Class**
- **Journey Date & Time**
- **Ticket Price (Target Variable)**

## Model Training 📡
1. **Preprocessing**: Missing values handled, categorical variables encoded.
2. **Neural Network**: Trained with **Embedding Layers** for categorical features.

## Deployment 🌍
The app is deployed on **Streamlit Cloud**. You can access it [here](https://train-rides-dashboard.streamlit.app/).

## Contributions 🤝
Feel free to fork and contribute! Create a pull request with your improvements.

## License 📜
This project is licensed under the **MIT License**.

---
🎯 **Author:** [Mohammed Suhaib](https://github.com/cyborgsuh)
