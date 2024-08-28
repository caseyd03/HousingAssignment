# HousingAssignment

## Objectives

## Overview

In this assignment, you will using your computer science knowledge to analyze housing data and make decisions.
You'll be first using a sample dataset to practice your data analysis skills, and then be given real data to work with and reflect on.

## Instructions

### Part 1

In `data.json`, a sample housing dataset has been provided. Each object in this data set acts as a person, containing important information like `Income`, `numberOfChildren`, and `disabledStatus`. Here is an example piece of data:

`{
    "Income": 17173, 
    "employmentStatus": "Unemployed", 
    "numberOfChildren": 3, 
    "disabledStatus": "None", 
    "Race": "Hispanic/Latino", 
    "Gender": "Female", 
    "veteranStatus": "No"
}`

Using filters in python, create a copy of the dataset that only contains people with an `Income` of `15000` or less. Store this in a variable called `lowIncome`.

Next, create the variables `greaterThan3Children` and `disabledOrVeteran` and use filters to create copies of the dataset containing only those with less than 3 children and those who qualify as `disabled` or `veteran`, respectively.

Examine the length of these arrays in comparison to the original 25-element dataset. How much smaller is it now? Do you think these filters are helpful for 

