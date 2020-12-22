MarijuanaAnalyzer: an Intelligent Visualization and Analysis Web App
TEAM 47
11/20/2020

1. DESCRIPTION:
----------------------------------------------------------------------------------
MarijuanaAnalyzer is a intelligent web app integrated with interactive
data visualization as well as a predictor backed by multiple machine
learning models. We provide a comprehensive overview of marijuana
through dynamic data visualization. Also, the user can predict the
impact of marijuana on mental health and abuses of other drugs based on
customized demographic information. The ultimate goal is to provide insights
into policy makers’ decision making. Also, we hope to offer a more informative
education for our web app users.

PACKAGES/FILES:

Web app repository (https://github.gatech.edu/ylu635/marijuana):
	css: css files associated with index.html and ml.html.
	data: data used in data visualization.
	js: Javascript code for data visualization as well as machine learning predictors
	lib: D3 library
	index.html: html file for main page.
	ml.html: html file for machine learning predictor page.
	predictors: python code for training and generating machine learning models

AWS lambda repository (https://github.gatech.edu/ftian39/marijuana_effects_team_47_lambda):
	code: code for AWS lambda used in predictors
	devEnv.json: a file for local test
	template.yaml: AWS cloudforamtion 
----------------------------------------------------------------------------------


2. INSTALLATION:
----------------------------------------------------------------------------------
unzip submitted team047final.zip

(or "git clone https://github.gatech.edu/ylu635/marijuana.git" for web app only)
----------------------------------------------------------------------------------

3. EXECUTION:
----------------------------------------------------------------------------------
LOCAL EXECUTION: 
1) change directory: "cd <path to the <marijuana> project folder under team47final/CODE folder>"
2) local execution: "python -m http.server 8000"

HOSTED STATIC WEB PAGE:
go to url "https://lukeyanggb.github.io/"
----------------------------------------------------------------------------------


4. APPENDIX
----------------------------------------------------------------------------------
TEAM MEMBERS:
Muzi Bi, Yang Lu, Fangxia Tian, Jing Ren, Jian Wang, Yutong Wu

LANGUAGES:
Python, Javascript, HTML, CSS

LIBRARIES
D3.js, scikit-learn, Pandas, Seaborn, Numpy, Scipy, Matplotlib, Joblib

FRAMEWORK:
Bootstrap

CLOUD RESOURCES:
AWS API Gateway, AWS Lambda, AWS S3

MAIN DATASET:
https://www.datafiles.samhsa.gov/study-series/national-survey-drug-use-and-health-nsduh-nid13517
----------------------------------------------------------------------------------
