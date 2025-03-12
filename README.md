# House Price Prediction

This project consists of a **machine learning API** deployed on AWS and a **Streamlit frontend** running locally to interact with the API.

## **Project Structure**
- **API**: Hosted on AWS at `http://3.110.108.39:8000/predict`
- **Frontend**: A Streamlit app (`frontend.py`) that runs locally and interacts with the API
- **Model File**: The trained model (house_price_model.pkl) is stored on Google Drive and must be downloaded manually.
- https://drive.google.com/file/d/1eTuwz-_jeS7Q4h3bqhfQEXrV42HTdW7y/view?usp=drive_link

---
## **How to Run the Project**

### **1. Clone the Repository**
```sh
git clone <repository-url>
cd <repository-folder>
```

### **2. Running the API Locally (Optional)**
If you want to run the API locally instead of using the AWS-hosted version:

#### **Install Dependencies**
```sh
pip install -r requirements.txt
```

#### **Run the API**
```sh
uvicorn app:app --host 0.0.0.0 --port 8000
```
This will start the API locally at `http://127.0.0.1:8000/predict`.

---
## **3. Running the Streamlit Frontend Locally**
To interact with the AWS-hosted API, you need to run the frontend locally.

#### **Install Dependencies**
Run the following command to install necessary packages:
```sh
pip install -r requirements.txt
```

#### **Start the Frontend**
Run the Streamlit application with:
```sh
streamlit run frontend.py
```
This will open the web interface in your default browser.

---
## **4. Using the API (Hosted on AWS)**
The API is deployed on an AWS instance and can be accessed via:
```
http://3.110.108.39:8000/predict
```

### **How to Make Predictions Using the API**
Send a **POST request** with JSON data to `http://3.110.108.39:8000/predict`.

#### **Example Request (Using Postman or cURL)**
```json
{
    "MedInc": 0.0,
    "HouseAge": 0.0,
    "AveRooms": 0.0,
    "AveBedrms": 0.0,
    "Population": 0.0,
    "AveOccup": 0.0,
    "Latitude": 0.0,
    "Longitude": 0.0
}
```

#### **Example cURL Command**
```sh
curl -X POST "http://3.110.108.39:8000/predict" -H "Content-Type: application/json" -d '{
  "MedInc": 0.0,
  "HouseAge": 0.0,
  "AveRooms": 0.0,
  "AveBedrms": 0.0,
  "Population": 0.0,
  "AveOccup": 0.0,
  "Latitude": 0.0,
  "Longitude": 0.0
}'
```
---
## **6. License**
This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

