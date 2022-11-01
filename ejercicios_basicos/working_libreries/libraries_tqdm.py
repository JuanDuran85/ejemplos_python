"""
Working with tqdm library

Instantly make your loops show a smart progress meter - just wrap any iterable with tqdm(iterable), and you're done!

"""

from tqdm import tqdm
from time import sleep

#----------------------------------------------------------------
# Creating a Progress Bar in with tqdm library
#----------------------------------------------------------------

for _ in tqdm(range(25)):
    sleep(1)



#----------------------------------------------------------------
#----------------------------------------------------------------