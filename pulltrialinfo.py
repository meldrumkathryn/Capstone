# import necessary packages
import os
import xmltodict
import pprint
import pandas as pd


# main function

def pull_trial(filename):
    '''
    main function to pull information from each file 
    filename: xml file name
    return: list of file information [nct id, condition, intervenction, age range, gender, healthy participants, criteria]
    '''
    # copy pathname of static copy of data here
    AllPublicXML='/Users/meldrumapple/Desktop/Capstone/AllPublicXML'
    
    #parse into folder where file is 
    folder=filename[0:7]+'xxxx'
    os.chdir(AllPublicXML+'/'+str(folder)) # Change this forward slash to backslash if on pc
    
    #open file and convert to dictionary
    with open(filename, 'r', encoding='utf-8') as doc:
        file = doc.read()
    dct=xmltodict.parse(file)
    
    #Extract trial info
    
    #pull NCT-id
    try:
        num=dct['clinical_study']['id_info']['nct_id'] 
    except:
        num=pd.NA
    
    #pull condition
    try: 
        condition= dct['clinical_study']['condition']
    except: 
        condition=pd.NA
    
    # pull intervention data- this can be formatted as list of dictionary or just dictionary
    try: 
        intv=[dct['clinical_study']['intervention']['intervention_name'],dct['clinical_study']['intervention']['intervention_type']]
    except:
        try:
            intv=[dct['clinical_study']['intervention'][0]['intervention_name'],dct['clinical_study']['intervention'][0]['intervention_type']]
        except:
            intv=pd.NA #sometimes trial has no intervention category at all
    
    #pull age range
    try:
        ages=[dct['clinical_study']['eligibility']['minimum_age'],dct['clinical_study']['eligibility']['maximum_age']]
    except: 
        ages=pd.NA
        
    #pull gender
    try:
        gender=dct['clinical_study']['eligibility']['gender']
    except:
        gender=pd.NA
        
    #pull healthy
    try: 
        healthy=dct['clinical_study']['eligibility']['healthy_volunteers']
    except:
        healthy=pd.NA
    
    #Extract criteria and clean up
    try: 
        criteria= dct['clinical_study']['eligibility']['criteria']['textblock']
        try: 
            criteria=criteria.split('Exclusion Criteria:')
            criteria[0]=criteria[0].replace('Inclusion Criteria:','')
        except: 
            None
    except:
        criteria=pd.NA
    df.loc[len(df.index)] = [num, condition, intv, ages, gender, healthy, criteria]
    return None



#initialize empty df
df=pd.DataFrame(columns=['nct_id', 'condition', 'intervention','ages','gender','healthy','criteria']) 



#pull from NCTIds 0 through 5600000 and count number of failures
fails=0
for i in range(0, 5600000):
    j='00000000'+str(i)           #add a bunch of zeros onto front of numbers
    j=j[-8:]                      #select only the last 8 digits
    try:
        pull_trial('NCT'+str(j)+'.xml')
    except:
        fails+=1