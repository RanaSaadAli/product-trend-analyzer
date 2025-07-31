
import numpy as np
import pandas as pd


def polarity_avg(dataset):
    """This function converts Polarity column into a numpy array and calculate avg of that array"""
    polarity_array = dataset["Polarity"].to_numpy()
    avg = round(np.mean(polarity_array),2)
    return avg
#-------------------------------------------------------------------------------------------------------------------------
def threshold_comparison(avg):
    """This functions sets a threshold value and compare avg of polarity column against that threshold"""
    threshold = 0
    if avg > 0.5:
        result = "This product have higher positive reviews"
    elif avg < -0.5:
        result = "This product have higher negative reviews"
    elif 0 < avg < 0.5:
        result = "People have slighlty positive reviews"
    elif -0.5 < avg < 0:
        result = "People have slightly negative reviews"
    else:
        result = "People reviews are neutral about this product"
    return result
#-------------------------------------------------------------------------------------------------------------------------
def subjective_percentage(subjective_reviews,subject_array):
    """This function calculates percentage of subjective reviews"""
    percentage_of_subjective_reviews = round(len(subjective_reviews)/len(subject_array)*100,2)
    return f"Percentage of opinion based reviews is: {percentage_of_subjective_reviews}"
#-------------------------------------------------------------------------------------------------------------------------    
def subjective_avg(subjective_reviews):
    """This function calculates average of subjective reviews"""
    avg_of_sub_rev = round(np.mean(subjective_reviews), 2)
    return f"Average of opinion based reviews is: {float(avg_of_sub_rev)}"
#-------------------------------------------------------------------------------------------------------------------------
def total_sub_rev(subjective_reviews):
    """This function total number of subjective reviews in dataset"""
    total_sub_rev = len(subjective_reviews)
    return f"Total opinion based reviews are: {total_sub_rev}"
#-------------------------------------------------------------------------------------------------------------------------
def total_ob_rev(objective_reviews):
    """This function count total number of objective reviews in dataset"""
    total_ob_rev = len(objective_reviews)
    return f"Total factual based reviews are: {total_ob_rev}"
#-------------------------------------------------------------------------------------------------------------------------
#create hype analysis function
def hype_analysis(dataset):

    #Calculate avg of Polarity
    avg = polarity_avg(dataset)
    
    #compare the polarity avg score against a threshold
    comparison_result = threshold_comparison(avg)

    #convert subject column into np array
    subject_array = dataset["Subjectivity"].to_numpy()

    #separate subject reviews and objectives and store them in lists
    subjective = subject_array > 0.5
    objective = subject_array <= 0.5

    subjective_reviews = subject_array[subjective]
    objective_reviews = subject_array[objective]

    #Calculate percentage of subjective reviews
    sub_per = subjective_percentage(subjective_reviews,subject_array)

    # Calculate average of subjective reviews
    avg_sub_rev = subjective_avg(subjective_reviews)
    
    #count total subjective reviews
    total_of_sub_rev = total_sub_rev(subjective_reviews)
    
    #count total objective reviews
    total_of_ob_rev = total_ob_rev(objective_reviews)
    
    #return results
    return comparison_result, sub_per, avg_sub_rev ,total_of_ob_rev , total_of_sub_rev





