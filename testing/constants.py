from pathlib import Path

# File locations
ROOTDIR = str(Path().parent.absolute().parent.absolute())
NPY_DATA_PATH = ROOTDIR + "/data/data-npy"
CLEAN_DATA_PATH = ROOTDIR + "/data/data-npy-clean"
TXT_DATA_PATH = ROOTDIR + "/data/data-txt"
TSV_DATA_PATH = ROOTDIR + "/data/data-tsv"
WORKING_DIR = CLEAN_DATA_PATH + "/all-data-new"
TEST_LOGS = ROOTDIR + "/testing/test_logs"
MODELS = ROOTDIR + "/testing/models"
EMBEDDINGS = ROOTDIR + "/testing/embeddings"
SUBMISSION = ROOTDIR + "/submission"

# Models
GPT3_TURBO = "gpt-3.5-turbo"
ADA_EMBED = "text-embedding-ada-002"

# Request Rates
ADA_RATE = 2500