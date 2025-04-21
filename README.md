# salary_predictor
# 🧠📊💼 Data Visualization | ML Salary Predictor | SpaCy | TF-IDF | Python | Flask | Altair | Tableau | Scikit-learn | Render | Pandas | Data Cleaning | Preprocessing | Data Abstraction | Task Abstraction

## 📌 Project Title: **Job Market Insights & Salary Prediction through Data Visualization**

This project presents a complete **data pipeline** — from **data collection and cleaning** to **interactive storytelling dashboards** and a built-in **machine learning salary predictor model**.

It is built to give users and researchers a real-time understanding of the evolving job landscape and assist them in salary forecasting using AI.

---

## 🔍 Project Objectives

- Visualize **job market trends**, **skill demand**, and **experience requirements**
- Apply **data storytelling techniques** to communicate insights clearly
- Build and deploy a **salary prediction ML model**
- Use **Natural Language Processing (SpaCy + TF-IDF)** for job descriptions
- Emphasize **data abstraction**, **task abstraction**, and **user-driven insights**

---

## 🧱 Tech Stack

| Category | Tools & Frameworks |
|---------|---------------------|
| **Language** | Python |
| **Data Handling** | Pandas, NumPy |
| **Web Framework** | Flask |
| **ML/NLP** | Scikit-learn, SpaCy, TF-IDF |
| **Visualization** | Altair, Tableau |
| **Deployment** | Render |
| **Other** | Git, HTML/CSS, Jupyter Notebooks |

---

## 🛠️ Workflow

### 1. 📥 **Data Collection & Scraping**
- Collected job listings from sources like **Kaggle** and other public job APIs
- Fields include: *Job Title, Industry, Skills, Experience, Region, Salary*

### 2. 🧹 **Data Cleaning**
- Removed nulls, standardized strings (e.g., job titles, skill sets)
- Merged similar job roles (e.g., "Software Eng." → "Software Engineer")

### 3. 🔎 **Preprocessing**
- Tokenized job descriptions using **SpaCy**
- Applied **TF-IDF vectorization** to extract skill-based features
- Normalized experience and salary fields
- Removed outliers using z-score and IQR method

### 4. 🧠 **Salary Prediction Model**
- Used **Random Forest Regressor** for robust salary forecasting
- Input: `Job Title`, `Experience`, `Skills`
- Output: `Predicted Salary Range`
- Evaluation Metrics: MAE, RMSE, R² Score

### 5. 🗂 **Data Abstraction**
- Converted raw data into abstracted units:
  - Job Category
  - Experience Bands
  - Skill Clusters

### 6. 🎯 **Task Abstraction**
- Visual tasks mapped:
  - **Explore** → via interactive filters on dashboards
  - **Compare** → via bar/stacked charts for skill gaps
  - **Cluster** → via bubble/treemap for domain segmentation
  - **Predict** → ML-based salary forecasts

---

## 📊 Visualizations

### 📌 Charts & Why We Used Them

| Chart Type | Purpose | Reason for Use |
|------------|---------|----------------|
| Bar Chart | Skill frequency | Best for comparing categorical data |
| Stacked Bar | Skill vs Experience | Great for part-to-whole relationships |
| Tree Map | Domain segmentation | Visual hierarchy, scalable |
| Bubble Chart | Salary vs Experience | Good for multi-variable encoding |
| Line Chart | Time-based trend | Clear evolution of demand over time |
| Heatmap | Regional skill demand | Spatial + magnitude view |

> 📚 **Storytelling Approach**: Each dashboard was crafted to guide the user through a narrative — from *understanding the landscape* to *acting on insights* (e.g., targeting specific skills, estimating salaries, exploring roles).

---

## 🔮 ML Model Snapshot

```python
# Vectorization
tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(job_descriptions)

# Model
model = RandomForestRegressor()
model.fit(X_tfidf, salaries)
