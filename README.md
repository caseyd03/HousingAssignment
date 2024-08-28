# HousingAssignment

## Objectives

## Overview

In this assignment, you will using your computer science knowledge to analyze housing data and make decisions.
You'll be first using a sample dataset to practice your data analysis skills, and then be given real data to work with and reflect on.

## Instructions

### Part 1

In `data.json`, a sample housing dataset has been provided. Each object in this data set acts as a person, containing important information like `Income`, `numberOfChildren`, and `disabledStatus`. Here is an example piece of data:

```json
{
    "Income": 17173, 
    "employmentStatus": "Unemployed", 
    "numberOfChildren": 3, 
    "disabledStatus": "None", 
    "Race": "Hispanic/Latino", 
    "Gender": "Female", 
    "veteranStatus": "No"
}
```
Using filters in python, create a copy of the dataset that only contains people with an `Income` of `15000` or less. Store this in a variable called `lowIncome`.

Next, create the variables `greaterThan3Children` and `disabledOrVeteran` and use filters to create copies of the dataset containing only those with less than 3 children and those who qualify as `disabled` or `veteran`, respectively.

Examine the length of these arrays in comparison to the original 100-element dataset. How much smaller are they?

### Part 2

One of the key issues surrounding housing allocation is deciding how the resources are distributed. When considering many factors, and dealing with large amounts of people, it can be hard to look at each situation individually. We can use our computer science skills to make more efficient decisions.

You are now provided with a resource constraint. Out of the `100` people whose information is provided in the dataset, only `20` can be provided housing.

First, reflect and write down what data you consider most important for deciding who gets housing.

Next, using your knowledge on filters and modifying arrays. 

