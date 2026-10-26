# AgriGuide-AI
Crop recommendation → management guide → monitoring & risk alerts → yield prediction → dashboard → history.

## Run
```
pip install -r requirements.txt
# put crop_recommendation.csv and crop_yield.csv (Kaggle) in data/raw/  (optional: synthetic data is used otherwise)
python train_models.py
python run.py        # http://127.0.0.1:5000
pytest
```
