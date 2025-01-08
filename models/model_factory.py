# models/model_factory.py
from .lstm_model import LSTMModel
from .random_forest_model import RandomForestModel
from .gbm_model import GBMModel
from .xgboost_model import XGBoostModel
from .lightgbm_model import LightGBMModel


class ModelFactory:
    @staticmethod
    def create_model(model_type, config):
        models = {
            'lstm': LSTMModel,
            'random_forest': RandomForestModel,
            'gbm': GBMModel,
            'xgboost': XGBoostModel,
            'lightgbm': LightGBMModel
        }
        return models[model_type](config)












