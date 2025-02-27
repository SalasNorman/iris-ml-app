# Steps to Create an ML Project with a Web Interface

## 📂 **Folder & File Structure**
```
iris_project/
│── app/
│   │── app.py  # Flask backend
│   │── static/
│   │── templates/
│   │   └── index.html  # Frontend UI
│── data/
│   │── iris.csv  # Dataset
│   │── model.pkl  # Trained ML model (Moved Here)
│── notebooks/
│   │── 01_data_exploration.ipynb  # Data Exploration Notebook
│   │── 02_model_training.ipynb  # Model Training Notebook
│── train.py  # Script to train the model
│── environment.yml  # Conda environment file
│── README.md  # Project documentation
```
## 📊 Dataset  
The dataset used in this project is from Kaggle and is licensed under **CC0 (Public Domain)**.  
- **Source**: [Kaggle - Iris Dataset](<https://www.kaggle.com/datasets/arshid/iris-flower-dataset>)  
- This means the dataset can be used freely without restrictions.  

## 1. **Setup Environment**
- Create a Conda environment:  
  ```bash
  conda create -n iris_project python=3.9 -y
  conda activate iris_project
  ```
- Install necessary libraries:  
  ```bash
  conda install numpy pandas scikit-learn flask jupyter -y
  ```
- Alternatively, create `environment.yml` and use:
  ```bash
  conda env create -f environment.yml
  ```

## 2. **Prepare the Dataset**
- Load the dataset (e.g., `iris.csv`)
- Check for missing values and clean the data
- Split data into **training** and **testing** sets

## 3. **Data Exploration (Notebook)**
- Open `01_data_exploration.ipynb`
- Visualize the dataset (histograms, scatter plots)
- Analyze feature relationships

## 4. **Train the Machine Learning Model**
- Open `02_model_training.ipynb`
- Choose a model (e.g., **RandomForestClassifier**)
- Train the model on the dataset
- Evaluate model accuracy
- Save the trained model as `data/model.pkl`
  ```python
  import pickle
  with open("data/model.pkl", "wb") as f:
      pickle.dump(model, f)
  ```

## 5. **Build the Flask Web App**
### Backend (Flask API)
- Create a `Flask` application (`app.py`)
- Load the trained `model.pkl`
- Define routes:
  - `/` - Home page (HTML form)
  - `/predict` - Receives form input, makes a prediction

### Frontend (HTML + CSS)
- Create `templates/index.html`
- Design a form with input fields for features
- Add a **table** with sample dataset records
- Use **JavaScript** to autofill inputs when clicking a row

## 6. **Test the Application**
- Run the Flask server:
  ```bash
  python app/app.py
  ```
- Open `http://127.0.0.1:5000/` in a browser
- Input test values and verify predictions

## 7. **Deploy the Application (Optional)**
- Deploy on **Heroku, Render, or AWS**
- Use `gunicorn` + `nginx` for production
- Set up a **domain name** for public access

## ✅ **Project Completion**
If everything works, the **ML web project is complete!** 🚀

