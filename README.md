# Clinicaltrials.gov Natural Language Processing: 

## About the Project
This repository contains relevant code and data for the Clinicaltrials.gov Natural Language Processing Capstone project by the University of Virginia School of Data Science, sponsored by AllenAI. 

Literature: 

## File Descriptions: 

**mod_chia**

*APIpullcode.ipynb*: Jupyter notebook for applying the chia-based spacy model to the entirety of clinicaltrials.gov through the ctg API interface

*base_config.cfg*: base configuration file for training spacy model

*chia_train.ipynb*: preprocessing for spacy model to create training_data.spacy and dev_data.spacy files

*dev_data.spacy*: validation docbin for spacy model training

*relaxed_scorer*: scores spacy model by overlap of entitiy span

*stratified_sampling*: determines optimal train/dev/test split of chia corpus for training spacy

*strict_scorer*: uses spacy.Scorer() to score spacy model

*strict_scorer_custom*: scored spacy model by exact match to entity span

*training_data.spacy*: training docbin for spacy model training

###How to replicate Model training: 

Download chia's corpus without scope: 
https://virginia.box.com/s/4ezc8cerqqon4l63aa52yvrq0wu35k2k




