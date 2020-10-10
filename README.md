# Automated Model and Algorithm Deployment from Github to Algorithmia

This example repository uses an automated workflow via our Algorithmia Github Action, for continuous deployment of an XGBoost model and its inference script that runs as [an algorithm at Algorithmia](https://algorithmia.com/algorithms/asli/xgboost_automated). It's based off of our [Github Actions template ML repository](https://github.com/algorithmiaio/githubactions-modeldeployment-template/) which contains the necessary components of this integration as a starter kit. 

After creating an algorithm on Algorithmia as the scalable inference endpoint for your ML model, you can incorporate this automated deployment workflow in your own ML repository, if:

- Your algorithm's repository host is Algorithmia. Check out [this demo repo for an algorithm with Github as the repository host](https://github.com/algorithmiaio/githubactions-modeldeployment-demo-githubalgo.git)
- And you are either 
  - using a Jupyter notebook to train and evaluate your ML model and to create your inference script & dependencies
  - checking your saved model file into your repository

This workflow helps you deploy your model to Algorithmia and update your inference API to use the new model, whenever you do a Git push to your `master` branch. You can of course configure your own triggering event depending on your organization's deployment workflow.

Depending on your model development preference:
  - If you're developing your ML model on a Jupyter notebook, you can configure the workflow with the notebook path and tell it where to save the model file. In this case, the workflow will run the notebook on the CI worker machine's from-scratch environment. 
  - If you have an already saved model checked-in to your repository, you can configure the workflow with the existing model file path.
  
In both scenarios, the workflow will get the model file and upload it to the configured data collection on Algorithmia. 

To get your inference endpoint use this newly uploaded model, the workflow will make the connection between your inference algorithm and the uploaded model file, with the key-value pairs in  `model_manifest.json` file.
In addition to that, the manifest file will contain certain metadata such as:
- Which Github repository and which ref was this model file uploaded from?
- What was the MD5 hash of your model file when it was first created?
- What is the Github commit SHA and the commit message resulting in this automated upload?
- When did this upload happen?

By using this manifest, your inference script will know which model to load and use. It can also calculate the loaded model file's MD5 hash with the original MD5 hash that was calculated at the time of the upload, and make sure that the model file hasn't been changed.  

Cool, right? To see how all these are implemented in the algorithm for this repository's XGBoost sentiment analysis model, check out our [automated XGBoost example algorithm on Algorithmia](https://algorithmia.com/algorithms/asli/xgboost_automated).
