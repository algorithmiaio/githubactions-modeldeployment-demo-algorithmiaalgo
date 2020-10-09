# Automated Model and Algorithm Deployment from Github to Algorithmia

This is an example repository demonstrating an automated workflow between Github and Algorithmia where:
- You have an algorithm on Algorithmia as the scalable inference endpoint for your ML model. 
- Your algorithm's repository host is Algorithmia. Check [out this demo repo for an algorithm with Github as the repository host](https://github.com/algorithmiaio/githubactions-modeldeployment-demo-githubalgo.git)
- You are either 
  - using a Jupyter notebook to train and evaluate your ML model and to create your inference script & dependencies
  - checking your saved model file into your repository

And to automatize your model deployment to Algorithmia, you are using an awesome Github Actions workflow!

This example workflow helps you deploy your model to Algorithmia and update your inference API to use the new model, whenever you do a Git push to your `master` branch. 

Depending on your model development preference:
  - If you're developing your ML model on a Jupyter notebook, you can configure the workflow with the notebook path and tell it where to save the model file. In this case, the workflow will run the notebook on the CI worker machine's from-scratch environment. Through our utility script, your notebook will get the path for where to save the ML model object. 
  - If you have an already saved model checked-in to your repository, you can configure the workflow with the existing model file path.
  
In both scenarios, the workflow will get the model file and upload it to the configured data collection on Algorithmia. 

To get your inference endpoint use this newly uploaded model, the workflow will make the connection between your inference algorithm and the uploaded model file. 

In addition to that, a manifest file will inform you with model metadata such as:
- Which Github repository was this model file uploaded from?
- What was the MD5 hash of your model file when it was first created?
- What is the Github commit SHA and the commit message resulting in this automated upload?
- When did this upload happen?

By using this manifest, your inference script will know which model to load and use. It can also calculate the loaded model file's MD5 hash with the original MD5 hash that was calculated at the time of the upload, and make sure that the model file hasn't been changed.  

Cool, right? To see the inference algorithm for this repository's XGBoost sentiment analysis model, check out the [automated XGBoost example algorithm on Algorithmia](https://algorithmia.com/algorithms/asli/xgboost_automated).
