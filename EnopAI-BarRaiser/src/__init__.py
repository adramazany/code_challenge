"""
Data Toolkit: A library for processing and analyzing data.
"""

__version__ = "1.0.0"
__all__ = ["Statistics", "DataLoader"]

import logging
import sys
from .analytics import Statistics
from .processor import DataProcessor
from .io import DataLoader

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
