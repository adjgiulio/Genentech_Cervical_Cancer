#Kaggle: GENENTECH - Help prevent cervical cancer by identifying at-risk populations

![Alt text](https://kaggle2.blob.core.windows.net/competitions/kaggle/4494/media/bigccribbon.png)

Description
--------------

Cervical cancer is the third most common cancer in women worldwide, affecting over 500,000 women and resulting in approximately 275,000 deaths every year. After reading these statistics, you may be surprised to hear that cervical cancer is potentially preventable and curable.

Cervical cancer can be prevented through early administration of the HPV vaccine and regular pap smear screenings, which indicate the presence of precancerous cells. It is also sometimes curable by the removal of the early-stage cancerous tissue that is identified through pap smears. Screening and early treatment can lead to potential cures in about 95% of women at risk for cervical cancer.

Most women in the US have access to cervical cancer screening, yet 4,000 women die every year from cervical cancer in the US and it is estimated that 30% of US women do not receive regular pap screenings. We know little about who these women are and why they are not getting screened. Prior research suggests that lower screening rates are associated with low income, low education, lack of interaction with the healthcare system, and lack of health insurance. But research also shows that even in women with access to healthcare fail to get this preventive test, indicating that barriers like lack of education and not being comfortable with the procedure are influencing their behavior (Patient Survey). 

There are many patient advocacy programs on the importance of pap smears in cervical cancer prevention. However, these widespread programs may not be reaching or effectively speaking to the most vulnerable populations. If one could better identify these women, education campaigns could target them with content that speaks directly to their unique risk factors. Identifying predictors of not receiving pap smears will provide important information to stakeholders in cervical cancer prevention who run awareness programs.

With this Masters competition, Genentech is asking you to join their mission to help prevent cervical cancer. Given a dataset of de-identified health records, your challenge is to predict which women will not be screened for cervical cancer on the recommended schedule. Identifying at-risk populations will make education and other intervention efforts more effective, ideally ultimately reducing the number of women who die from this disease.


Evaluation
--------------

Submissions are judged on area under the *ROC curve*.

Data
-----------

In this competition, you are to predict whether a patient receives regular cervical cancer screening (pap smear), given the medical records of over 3 million women in the United States.

A patient is defined as a screener if the patient has had a pap smear in the last 5 years. This patient must be between the age of 25 and 65, and has not been diagnosed of cervical cancer or had hysterectomies. 

Please note that because of the data source, this data provided in the competition may have some sampling bias, therefore may not reflect the prevalence of cervical cancer screening of the general population.

This competition has 11 relational data tables.