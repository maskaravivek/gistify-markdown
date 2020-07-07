## Introduction

In the last post on GANs we saw how to generate synthetic data on Synthea dataset. Here's a link to the post for a refresher: 

https://www.maskaravivek.com/post/gan-synthetic-data-generation/

Similar to the last post, we would be working with the Synthea dataset which is publicly available. 

https://synthetichealth.github.io/synthea/

In this post, we will be working on the `patients.csv` file and will only be using continious and categorical fields. We will remove the other fields like name, email ID etc which contains a lot of unique values and will thus will be difficult to learn. 

## Data Preprocessing

Firstly, download the publicly available synthea dataset and unzip it. 



https://gist.github.com/5595405b34c384ded0f9bbc4bb6b1efd

## Install Dependencies

In this post, we will be using the default implementation of CTGAN which is available here. 

https://github.com/sdv-dev/CTGAN

To use CTGAN do a pip install. Also, we will be installing the `table_evaluator` library([link](https://pypi.org/project/table-evaluator/)) which will help us in comparing the results with the original data. 



https://gist.github.com/e2fff48dd2987b20684bd0b5926a751c

### Remove unnecessary columns and encode all data

Next, we read the data into a dataframe and drop the unnecessary columns. 



https://gist.github.com/a6c8d8a6ec7440d4fa1faf8b87207ad2

    Index(['MARITAL', 'RACE', 'ETHNICITY', 'GENDER', 'BIRTHPLACE', 'CITY', 'STATE',
           'COUNTY', 'ZIP', 'HEALTHCARE_EXPENSES', 'HEALTHCARE_COVERAGE'],
          dtype='object')


Next, we define a list with column names for categorical variables. This list will be passed to the model so that the model can decide how to process these fields. 



https://gist.github.com/82aa9e3d7bbeb2210d2509b8a2cb197b

## Training the model

Next, we simply define an instance of `CTGANSynthesizer` and call the `fit` method with the dataframe and the list of categorical variables. 

We train the model for 300 epochs only as the discriminator and generator loss becomes quite low after these many epochs. 



https://gist.github.com/9a24a63580d2a2f269200209fd484c91

## Evaluation

Next, we simply call model's `sample` function to generate samples based on the learned model. In this example we generate 1000 samples. 



https://gist.github.com/56045e1d1c7e279a883f38e005d84855


https://gist.github.com/49b715b52e2bec269833b12ca088b50e

Now let's try to do a feature by feature comparision between the generated data and the actual data. We will use python's `table_evaluator` library to compare the features. 

We call the `visual_evaluation` method to compare the actual data(`data`) and the generated data(`samples`).



https://gist.github.com/cbe6bba1f245b1749b24398afc33d1c7

    (1171, 11) (1000, 11)


    
![png](images/CTGAN_Synthetic_data_generation_13_1.png)
    
![png](images/CTGAN_Synthetic_data_generation_13_2.png)
    
![png](images/CTGAN_Synthetic_data_generation_13_4.png)
  
![png](images/CTGAN_Synthetic_data_generation_13_5.png)
    
![png](images/CTGAN_Synthetic_data_generation_13_6.png)
    
## Conclusion

As its apparent from the visualizations, the similarity between the original data and the synthetic data is quite high. The results give a lot of confidence as we took a random dataset and applied the default implementation without any tweaks or any data preprocessing. 

The model can be used in various scenarios where data augmentation is required. Its worthwhile to highlight a few caveats:
- In this dataset we just had categorical and continuous variables and the results were quite good. 
- It would be useful to try it on datasets with date time values
- Also this model won't be able to handle relational datasets by default. For eg. there's no way of specifiying primary key foreign key constraints. 
- Moreover, it cannot handle contraints by default. For eg. a particular state should belong to a single country but there's no way of specifying this constraint. The generated dataset can contain new combinations of (state, country) which is not present in the original dataset. 

There's a framework to mitigate some of the above issues. Checkout [SDV](https://sdv.dev/SDV/) if you are interested. I will try to write a post about it in future.

## TL;DR

Here's the link to the Google colab notebook with the complete source code. 

https://colab.research.google.com/drive/1nwbvkg32sOUC69zATCfXOygFUBeo0dsx?usp=sharing


## References

[1] Lei Xu, Maria Skoularidou, Alfredo Cuesta-Infante, Kalyan Veeramachaneni. Modeling Tabular data using Conditional GAN. NeurIPS, 2019