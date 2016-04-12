## Kaggle: GENENTECH - Help prevent cervical cancer by identifying at-risk populations

### Winning approach for the Genentech Cervical Cancer Screening on Kaggle.

*This repository is intended to show how fetures were engineered and how a single model scoring .9629 ROC can be achieved with a simple IPython notebook.*

## Generating the solution

### Environment

- Hadoop cluster with Hive and Impala

- 128GB RAM

- Python Anaconda

- XGBoost


### Generate the data (final version v9)

**NOTE**: none of the code in this repo is meant to be executed as a single script. Based on my experience a successfull Kaggle environment needs to be condusive to supporting quick experiments throughout the competition. Therefore I did not put any effort during the competition to have highly performing or very well documented code. Due also to the complexity and the length of query time there was no point in making this code executable as one neat production ready script. You should expect to have to execute SQL queries one at time.

1) Load all the data into a Hadoop cluster using **data load SQL.txt**. Then run the SQL code in **feature engineering SQL.txt** on a Hadoop cluster using Impala (or Hive when directed to). In the end the following tables will be generate (among many other tables):

* gj_train_excl_master_v9
* gj_test_master_v9

*OHE data (add a _test for test files)*

* gj_feats_ohe_cptdx_gc
* gj_feats_ohe_dx_gc
* gj_feats_ohe_proc_gc
* gj_feats_ohe_prov_gc
* gj_feats_ohe_cptspec_gc
* gj_feats_ohe_dxspec_gc
* gj_feats_ohe_leak_proc_gc
* gj_feats_ohe_leak_dx_gc
* gj_feats_ohe_proc_proc_gc
* gj_feats_ohe_leak_ct_gc
* gj_feats_ohe_proc_pos_gc
* gj_feats_ohe_dx_pos_gc (up to here to recreate v6)
* gj_feats_ohe_lkprocsd_gc
* gj_feats_ohe_lk_specproc_gc
* gj_feats_ohe_leak_proc_gc2
* gj_feats_ohe_leak_ct_gc2
* gj_feats_ohe_proc_pos_gc2
* gj_feats_ohe_specleak_gc
* gj_feats_ohe_leak_proc_gc3
* gj_feats_ohe_leak_ct_gc3
* gj_feats_ohe_specleak_gc3 (up to here to recreate v9)

**NOTE**: the final winning solutions utilizes models based on several versions of the data, created at different times throughout the competition. v9 is the final version. v6 was also utilized. The SQL code will show how to recreate v6 for the dense features. For the sparse features just include up to the matrix indicated above.

2) Download train, test and all OHE files to your local system as .csv files with headers.


3) Read each OHE file (train and test) and generate a Scipy sparse matrix using scikit learn count vectorizer using the blueprint described in  **OHE_blueprint.py**.


3) Run **Genentech Cervical Cancer Screening - Final.ipynb** to generate a submission.

## Blend augmented predictions

The winning solution is a ensemble of tens of models ran on v9 and previous versions of the data by my teammate Michael. See Kaggle forum or his Git repo for more info about all the models involved in the final ensemble.