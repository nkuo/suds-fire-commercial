# suds-fire-commercial

This project is to further Michael's work on Fire Risk Modeling for the Pittsburgh fire department.

To run:
Put all data files in "data/" from Google_Drive/Data
Install anaconda, then install everything via conda or pip within conda.
Remember to create a virtual env within conda via:

```bash
conda create -n name_of_my_env python
source activate name_of_my_env            #when activating a virtual env
conda install pandas                      #installing stuff

#from my experience xgboost is only available via pip so..
conda install pip
pip install xgboost                       #while inside the virtual env
