# models/model_factory.py
from .lstm_model import LSTMModel
from .random_forest_model import RandomForestModel
from .gbm_model import GBMModel
from .xgboost_model import XGBoostModel
from .lightgbm_model import LightGBMModel
from .svm_model import SVMModel
from .transformer_model import TransformerModel


class ModelFactory:
    _models = {
        'lstm': LSTMModel,
        'random_forest': RandomForestModel,
        'gbm': GBMModel,
        'xgboost': XGBoostModel,
        'lightgbm': LightGBMModel,
        'svm': SVMModel,
        'transformer': TransformerModel,
    }

    @staticmethod
    def create_model(model_type, config):
        """Create and return a model instance by type name.
        
        Args:
            model_type: One of 'lstm', 'random_forest', 'gbm', 'xgboost',
                        'lightgbm', 'svm', 'transformer'.
            config: Config instance with model hyperparameters.
        
        Returns:
            An instance of the requested model.
        
        Raises:
            ValueError: If model_type is not recognized.
        """
        if model_type not in ModelFactory._models:
            available = ', '.join(sorted(ModelFactory._models.keys()))
            raise ValueError(
                f"Unknown model type '{model_type}'. "
                f"Available models: {available}"
            )
        return ModelFactory._models[model_type](config)

    @staticmethod
    def list_models():
        """Return a list of available model type names."""
        return list(ModelFactory._models.keys())
