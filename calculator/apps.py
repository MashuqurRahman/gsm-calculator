
import os
from django.apps import AppConfig
from django.conf import settings
import pickle




class CalculatorConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'calculator'
    # model_path = os.path.join(settings.DIGIT_RECOGNIZER_MODEL, 'abcde.h5')
    model_path = os.path.join(settings.GSM_CALCULATOR_MODEL, 'gsm_model.sav')
    loaded_model = pickle.load(open(model_path, 'rb'))

    encoder_path = os.path.join(settings.MODEL_PATH, 'MachineDiameterXGauge_encoder.pkl')
    
    encoder_model = pickle.load(open(encoder_path, 'rb')) 
    # pkl_file.close()

