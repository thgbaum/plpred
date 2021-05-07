'''
arquivo __init__ está servindo para puxar 
os outros arquivos da pasta model
'''

from .plpred_rf import PlpredRF 
from .plpred_gb import PlpredGB
from .base_model import BaseModel
from .plpred_svm import PlpredSVM
from .plpred_nn import PlpredNN