"""
Core module for advanced Python features.

This module provides:
- Decorators (retry, cache, timer)
- Generators (data pipeline, batching, fibonacci)
- Context managers (safe file handling)
- Metaclasses (class registry system)
"""

# Import decorators
from .decorators import retry, Cache, timer

# Import generators
from .generators import DataPipeline, batch_generator, fibonacci_generator

# Import context managers
from .context_managers import SafeFileHandler

# Import metaclasses
from .metaclasses import RegistryMeta

# Public API
__all__ = [
    "retry",
    "Cache",
    "timer",
    "DataPipeline",
    "batch_generator",
    "fibonacci_generator",
    "SafeFileHandler",
    "RegistryMeta",
]