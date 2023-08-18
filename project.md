---
layout: class
title: "CSCI 467 Final Project Information"
semester: Fall 2023
time: Tuesdays and Thursdays at 2:00-3:20pm
location: LVL 17
location_link: "https://maps.usc.edu/?id=1928&reference=LVL"
instructor: Robin Jia
order: 1
---
In the final project, you will work in groups of 1-3 students to apply machine learning techniques to a problem of your choice.
Before the final project, there will be a project proposal and midterm report due in the middle of the semester.
These exist to ensure that you will be on track to complete a successful final project.

### Logistics
Please make only one submission per group. Be sure to list all group members on your submission.

I have created
**[this LaTeX template](https://www.overleaf.com/read/mmytwxqhzxsq),**
which you are **required** to use.
Once you open this link, you can copy this to your own project and begin editing (you must be logged in to Overleaf to do this; alternatively you can download the source and edit locally).
Note that for the proposal, you only need to fill in some of the sections.

All groups will be graded on the same criteria, regardless of size.
Each member of a team should contribute both to the technical implementation and to the writing of the reports.

### Project Proposal
The project proposal should be 1.5-2 pages (not including references), and should include the following:
- **Problem statement and task definition**. Your goal is to build a new system. What is your system supposed to do? Describe what is the input and desired output in detail. Also describe why you chose this problem---what real world problem does this try to address? Try to make scope neither too narrow nor too broad. If you need help with this, please come to office hours.
- **Related work**. Search the Internet for similar projects and describe what they do and what challenges they faced.
- **Dataset**. Machine learning methods all rely on having a dataset. Your proposal **must** either describe an existing dataset that you have found that you will use, or include a detailed plan of how you will create an appropriate dataset so that it can be used for experiments in your midterm report.
- **Evaluation plan**. Once you have built a system, how will you evaluate it? First, you need to have an appropriate test dataset. You could choose to take one dataset and randomly split it into train, development, and test sets. You could also use test data from a different source to test whether your system generalizes to new situations. Second, what metric will you use? Standard metrics are accuracy (for classification) or RMSE (for regression), but depending on your problem other metrics may also be appropriate (such as precision/recall/F1 if your problem has label imbalance). You might also wish to consider other factors such as efficiency.
- **Plans for baselines**. A baseline is a simple initial solution to your task. Baselines are important as they give you a starting point that you can hope to improve upon . For some problems, there may be a way to have a non-machine learning baseline (e.g., hard-coding some rules to make predictions). In other cases, such a baseline may be difficult to come up with. In this case, think of a simpler machine learning approach that could serve as a baseline (e.g., logistic regression with a small set of simple features).
- **Plans for main methods**. How do you plan to solve your problem? Talk about specific algorithms you will use---these can be from class or can be other machine learning methods you know about. You should also describe the key challenges of the problem you've chosen, and then talk about how you hope to address them. 

Note that you can adjust the topic of your final project or the specific methods used after the proposal.
If you want to make a significant change, come talk to me or one of the TA's first, 
so we can help determine if the new project plan is feasible.

### Midterm Report
The midterm report should be 3-4 pages long (not including references).
By the time of the midterm report, you should have implemented a basic version of your planned machine learning method, along with at least one baseline approach.
You should describe your initial results in this report, where there is room for improvement, and how you plan to improve your method for the final report.

Your report should have the following sections:
1. **Introduction**: Describe the problem statement and task definition, as in the proposal.
Be sure to address any feedback you received from the proposal.
If you have changed your project, those changes should also be reflected here.
Also include an update on your overall results and progress so far.
2. **Related work**: 
This can be the same as the proposal, but be sure to address any feedback you received.
3. **Dataset and Evaluation**:
By now, you should have a dataset, and should also have a train/dev/test split of the dataset.
(In some cases, you may not have enough data to create a train/dev/test split, in which case you should discuss alternatives such as cross-validation to choose hyperparameters.)
Describe the dataset in detail, such as how many examples are in each split.
If this is a classification dataset, report statistics like how many examples are of each class.
If you created the dataset yourself (e.g., by scraping some websites), describe how you did that.
Finally, describe the evaluation metrics you've chosen and why they are appropriate.
4. **Methods**:
By now you should have tested at least **two** methods.
At least one should be a machine learning method, and the other should be a baseline.
It is also acceptable to have two different machine learning methods.
Describe each method in detail here, including a step-by-step description of how your inputs are mapped to outputs.
Include details such as how you create features, and what the hyperparameters are and how you chose them.
It is okay if the current machine learning methods you've tried are not the final one you want to use.
5. **Experiments**:
Describe the results when you test each of your methods.
Display these results in a table or appropriate chart.
Also include results of experiments you ran on the development set to select hyperparameters.
Comment whether the methods perform differently, which is better, and why you think that is.
6. **Discussion**:
After running your methods, you should do manual error analysis to understand what happened.
Take a random sample of your development examples and study the cases that the model got wrong.
Do you see any patterns?
By looking at the examples, why do you think they were hard for the model?
Based on your error analysis, suggest at least two concrete ways you could improve the model's accuracy.
7. **Conclusion**: Summarize your progress so far and what you will do by the final report.

### Final Report
The final report should be 5-6 pages long (not including references).
You should have a complete description of your final system and comprehensive experiments showing how well it performs compared to previous versions and your baselines.
You should also include detailed error analysis to understand what your system still gets wrong.

Your report should have the following sections:
0. **Abstract**: Write a one-paragraph summary of your task, methods, and findings.
1. **Introduction**: Describe the problem statement and task definition.
Make sure that this is consistent with the final direction that your project goes.
Also briefly describe your final results.
2. **Related work**: 
Now that you know your final methods and project goals, search again for related projects and papers.
Describe what they do, what challenges they faced, and **how your final approach compares and contrasts with these other papers.**
3. **Dataset and Evaluation**:
This can be similar to the midterm report, but be sure to incorporate any feedback you received and make it consistent with the final results of the project.
If you made any changes to your dataset since the midterm report, discuss your reasoning.
4. **Methods**:
Describe all of your methods.
For the final report, you should present one new method or a refinement of your method from the midterm report (something more than just changing hyperparameters),
in addition to the methods from your midterm report.
The new method should be something more advanced than a linear classifier.
You should:
* Describe all of your methods in detail, including a step-by-step description of how your inputs are mapped to outputs.
* Include details such as how you create features, and what the hyperparameters are and how you chose them.
* Finally, describe **why you believe your final method overcomes the limitations of the methods you tested in the midterm report.** 
5. **Experiments**:
Similar to the midterm report, describe the results when you test each of your methods (of course you will have more results compared to the midterm report).
Display these results in a table or appropriate chart.
Also include results of experiments you ran on the development set to select hyperparameters.
Comment whether the methods perform differently, which is better, and why you think that is.
6. **Discussion**:
Do another round of manual error analysis, similar to the midterm report but with your final model.
Again, look for patterns in what types of examples are hard for the model.
Overall, how well do you think your model performs in comparison with what you expected?
Are you surprised by examples your model could/could not process correctly?
7. **Conclusion**: Summarize your findings.
What did you learn (about the task and/or about the machine learning methods) through this project?

Finally, you are **also required to submit your code and data (where applicable)**. 
In your write-up, include a link to a GitHub repository or Google Drive/other cloud storage provider.
It must include the following:
* All code to generate the results in your project
* If you created your own dataset, include the dataset. If you used a ready-made dataset (e.g., from Kaggle), include a link to the dataset.
* A list of commands used to generate all of your results. You do not need to explain the code in detail, but make sure it's clear how all the results in your report were generated.

### Example projects
To give you a rough sense of the expectations for this project (and since this is a new type of assignment for CSCI 467),
I have compiled a list of example final projects from Stanford's machine learning class a few years ago (see [here](https://cs229.stanford.edu/proj2017/) for the full list).
While the exact guidelines will differ, these projects ideas and experiments would all be appropriate for this class as well.
* [Music Genre Classification via Machine Learning](https://cs229.stanford.edu/proj2017/final-reports/5244969.pdf)
* [Terrain Classification for Off-Road Driving](https://cs229.stanford.edu/proj2017/final-reports/5243384.pdf)
* [Real Time Tennis Match Prediction Using Machine Learning](https://cs229.stanford.edu/proj2017/final-reports/5243744.pdf)
* [Learning the Language of Wine](https://cs229.stanford.edu/proj2017/final-reports/5244216.pdf)
* [Speech Command Recognition with Convolutional Neural Network](https://cs229.stanford.edu/proj2017/final-reports/5244201.pdf)
* [An AI Approach to Automatic Natural Music Transcription](https://cs229.stanford.edu/proj2017/final-reports/5244388.pdf)
* [Predicting Insurance Claims in Brazil](https://cs229.stanford.edu/proj2017/final-reports/5244182.pdf)
* [Molecular Structure Prediction Using Infrared Spectra](Molecular Structure Prediction Using Infrared Spectra)
* [Forage: Optimizing Food Use With Machine Learning Generated Recipes](https://cs229.stanford.edu/proj2017/final-reports/5244233.pdf)
* [Balancing Classifier Fairness with Public Safety in Traffic Stops](https://cs229.stanford.edu/proj2017/final-reports/5244311.pdf)

### FAQ
*What if we try something but it doesn't work? (e.g., doesn't improve over the baseline)*
This is fine as long as you were thorough in your process and analyze why your new method did not succeed.
Make sure you try a variety of hyperparameter settings.
Make sure you look at the errors your model makes on the development set data, and report patterns you find.
Do basic sanity checks--for example, can your model fit a small training dataset well?
If not, there may be a bug somewhere, or a bad choice of hyperparameters such as learning rate.

*What libraries can we use?*
For the project, you are free to use any open source libraries for machine learning,
including Sci-kit learn, Pytorch, Tensorflow, and Huggingface libraries.
If you use a complicated method (e.g., some deep neural network), be sure to also include a simpler method as a baseline.

### Project resources
- [USC CARC Discovery Cluster](https://www.carc.usc.edu/user-information/user-guides/hpc-basics/getting-started-discovery) is a computing cluster run by USC. 
I have requested and received quota to run jobs specifically for class final projects.
I have already added all enrolled students to the list of authorized users.
Follow the link more to learn about how to use this resource.
Note that both CPU and GPU-based machines are available---GPUs will be useful for running deep learning models.
- [Google Colab](https://colab.research.google.com/) provides free computational resources, though there are limits (e.g., jobs can only run for 12 hours at a time). See their [FAQ](https://research.google.com/colaboratory/faq.html) for details.
