from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib
import pandas as pd
import numpy as np

#files
ohe_file_train = 'myfilename_train.csv'
ohe_file_test = 'myfilename_test.csv'

#import train and test
train = pd.read_csv(ohe_file_train)
test = pd.read_csv(ohe_file_test)

#define a vectorizer
tf_vectorizer = CountVectorizer(min_df=50, max_df=0.9,
                                stop_words='english',
                                token_pattern=u'[0-9A-Za-z_]{1,}',
                                ngram_range=(1,1))

#fill NA
train.fillna('',inplace=True)
test.fillna('',inplace=True)

#train and trasform
X = tf_vectorizer.fit_transform(train[data])
Xte = tf_vectorizer.transform(test[data])

#save to pkl files
joblib.dump(X,'myfile_tr_sparse.pkl')
joblib.dump(Xte,'myfile_te_sparse.pkl')
