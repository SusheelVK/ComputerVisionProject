from .gpds import GPDSDataset
from .mcyt import MCYTDataset
from .cedar import CedarDataset
from .brazilian import BrazilianDataset, BrazilianDatasetWithoutSimpleForgeries
from .BHSig260H import BHSig260HindiDataset
from .BHSig260B import BHSig260BengaliDataset

available_datasets = {'gpds': GPDSDataset,
                      'mcyt': MCYTDataset,
                      'cedar': CedarDataset,
                      'brazilian': BrazilianDataset,
                      'BHSig260H': BHSig260HindiDataset,
                      'BHSig260B': BHSig260BengaliDataset,
                      'brazilian-nosimple': BrazilianDatasetWithoutSimpleForgeries}
