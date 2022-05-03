import IPython.core.display_functions
from chembl_webresource_client.new_client import new_client
import pandas as pd

molecule = new_client.molecule
approved_drugs = molecule.filter(first_approval_isnull=False).filter(max_phase=4)
ad_df = pd.DataFrame(approved_drugs)
IPython.core.display_functions.display(ad_df)