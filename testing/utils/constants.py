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
GPT4 = "gpt-4"

# Request Rates
RATES = {ADA_EMBED: {"tokens": 60000, "requests": 500},
         GPT3_TURBO: {"tokens": 1000000, "requests": 3000},
         GPT4: {"tokens": 10000, "requests": 500},}