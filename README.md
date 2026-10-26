# AgriGuide-AI
<<<<<<< HEAD
Crop recommendation → management guide → monitoring & risk alerts → yield prediction → dashboard → history.

## Run
```
pip install -r requirements.txt
# put crop_recommendation.csv and crop_yield.csv (Kaggle) in data/raw/  (optional: synthetic data is used otherwise)
python train_models.py
python run.py        # http://127.0.0.1:5000
pytest
```
=======
ML-powered crop decision-support system: recommends crops from soil and weather data, gives crop-specific cultivation guidance, tracks growth-stage conditions with risk alerts, and predicts expected yield. Built with Flask, Scikit-learn.

# 🌾 AgriGuide AI

**Smart Crop Recommendation, Crop Management, Monitoring & Yield Prediction System**

AgriGuide AI is an ML-powered agricultural decision-support system for farmers. Most crop recommenders stop at predicting a crop name. AgriGuide AI covers the whole workflow: **recommend → guide → monitor → alert → predict yield**.

## ✨ Features

- **Crop recommendation**: a Random Forest classifier suggests the best crop, plus alternatives, from N, P, K, temperature, humidity, pH and rainfall.
- **Cultivation guidance**: crop-specific advice on soil, water, nutrients, growth stages, weed/pest management, harvest and yield improvement.
- **Growth-stage monitoring**: log soil moisture, weather, N/P/K values, growth stage and field observations over time.
- **Risk alerts**: rule-based analysis flags unfavourable conditions as Low, Medium or High.
- **Yield prediction**: a separate Random Forest regressor estimates expected yield.
- **Web dashboard**: monitoring history, alerts, guidance and yield estimates, with Chart.js charts.

> **Note:** Cultivation guidance comes from a curated agricultural knowledge base and risk alerts come from transparent rules. Only crop recommendation and yield estimates are ML predictions, and the interface keeps these separate.

## 🧠 Machine Learning

| Task | Model | Input | Output |

| Crop recommendation | Random Forest Classifier | N, P, K, temperature, humidity, pH, rainfall | Recommended crop (22 classes) |
| Yield prediction | Random Forest Regressor | Crop, year, season, state, area, rainfall, fertilizer, pesticide | Estimated yield |

### Measured results

| Model | Result |
| Crop classifier | Accuracy **1.00** on 440 held-out samples (22 crops); one jute sample predicted as rice |
| Yield regressor (Random Forest) | R² **0.926**, MAE **20.25** |
| Yield baseline (Linear Regression) | R² 0.015, MAE 193.22 |

Top features for crop recommendation: rainfall, humidity and potassium (K).

*The crop dataset is clean and well separated, so near-perfect accuracy is expected and may not carry over to noisy field data.*

## 🛠️ Tech Stack

Python · Pandas · NumPy · Scikit-learn · Joblib · Flask · SQLite · HTML · CSS · JavaScript · Chart.js · Jupyter Notebook

## 📊 Datasets

1. **Crop Recommendation Dataset**: N, P, K, temperature, humidity, pH, rainfall → crop label
2. **Indian Crop Yield Dataset**: used for yield prediction and agricultural trends


## 🔮 Future Work

- Live weather API and soil-sensor integration
- Telugu/Hindi multilingual advisory
- Gradient Boosting comparison for yield prediction
- Agronomist validation of the knowledge base and alert thresholds

## 👩‍💻 Team SmartFlow

Jeevani · Kavyasri · Sushma
G. Narayanamma Institute of Technology & Science, Hyderabad


>>>>>>> d164e06e3b5cbd70e36fdf87b672066da39ee481
