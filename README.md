# Notes
1. data/data-npy is the original data downloaded directly from Codalab
2. During cleanup of the .npy files I accidentally wrote into the same files. Problem should have been rolled back but if there are issues check Setup 1 commit or earlier for original.
3. There may still be formatting issues in the data, and there are certainly some typos. If desired, add to remove_lines() in the python script.
4. all-data-new was downloaded on 11.30 and should be preferred for training and eval. Training data seems to be the same between all-data-new and all-data-old, while eval data seems to be the same as eval-data-new. all-data-old and eval-data-new are added for completion and can be ignored.
5. data/readme.pdf is from Codalab and explains the npy data structure: basically list of dicts, keys are questions, answers, etc. and vals can be strings, ints, or list of strings/ints.
6. Set up your own keys.py to run the GPT testing
