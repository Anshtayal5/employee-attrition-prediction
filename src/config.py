from pathlib import Path

# =============================================================================
# Project Paths
# =============================================================================

# Root directory of the project
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# =============================================================================
# Data Directories
# =============================================================================

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# =============================================================================
# Other Project Directories
# =============================================================================

MODELS_DIR = PROJECT_ROOT / "models"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
ASSETS_DIR = PROJECT_ROOT / "assets"

# =============================================================================
# Dataset Paths
# =============================================================================

DATASET_PATH = RAW_DATA_DIR / "WA_Fn-UseC_-HR-Employee-Attrition.csv"