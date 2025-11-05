### Pre-Processing
Target to be predicted quarterly 

Features are all monthly - create lags. Create a GDP lag, use an interpolation scheme (this is not data leakage as discussed). Experiment with how many lags are optimal. 

Remove all data entries that are not from the start of the month 

Any other feature engineering ideas to improve information models have to train on?

Create a train-test split with no overlap. Only use this test set once, at the very end with the final tuned model. 

Use TimeSeriesSplit train-test split and cross validation  

Apply StandardScaler to each individual dataset (eg within the Pipeline). 

### Next Steps 
Research a model you want to investigate within sci-kit learn. I think its best we focus on non-linear models as no one had much success with linear models last time. Can also look to use new pre-processing methods eg for dimensionality reduction. 

Implement this model to predict quarterly values.

Compare to the other models. 

Use R^2 as primary performance metric? This seems to align with what we all done.

Any other ideas you have give a try, it seems they really want us to experiment.
