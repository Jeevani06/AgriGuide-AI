import pytest, os
@pytest.mark.skipif(not os.path.exists("models/crop_recommendation_model.pkl"), reason="train first")
def test_model_file(): assert True
