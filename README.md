# PMT

Welcome to the home page of the Predictive Mutation Testing(i.e., PMT).
In the paper we propose predictive mutation testing, the first approach to predicting mutation testing results without mutant execution. In particular, the proposed approach constructs a classification model based on a series of features related to mutants and tests, and uses the classification model to predict whether a mutant is killed or survived without executing it.

## Structure of the Homepage

The homepage is constructed by four main parts. Here are the brief introduction to each part.


### Experiment Java Source Code

This part of the folder contains the java code used to generate arff files, which are the input of weka machine learning.
The java code that we used to do machine learning is also included in weka_test_zy_version.rar.

### Project List

This folder contain several txt files which indicates the projects we used for each experiment. All of the projects of the lists can be downloaded at github. 

### Project Arffs

All of the arff files used in the PMT paper can be found in this folder. You can replicate the experiment result use the arffs and the source code provided in this homepage.

### Tools

Tools that we use to collect assert values and static metric are included in this folder. We also put a readme.txt under each directory of the tool to make the useage of the tool clearer.
