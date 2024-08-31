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

Examine the length of these arrays in comparison to the original 25-element dataset. How much smaller are they?

### Part 2

One of the key issues surrounding housing allocation is deciding how the resources are distributed. When considering many factors, and dealing with large amounts of people, it can be hard to look at each situation individually. We can use our computer science skills to make more efficient decisions.

You are now provided with a resource constraint. Out of the `25` people whose information is provided in the dataset, only `10` can be provided housing. (For the sake of the assignment, assume that people with children can be accomodated for. We will consider this later.)

First, reflect and write down what data you consider most important for deciding who gets housing.

Next, using your knowledge on filters and modifying arrays, create a copy of the dataset that only contains `10` people. This may take you more than one try as you experiment with different filters. The `10` people contained in this smaller dataset should be considered, by you, to have priority for housing.

Reflect on your filtered dataset. What do you think might have been an unforseen consequence of the filters you chose? What groups are favored/unfavored here?

Next, using your filtered dataset, calculate the total number of people, including children, that are included. This will likely be at least double the `10` person limit. Now considering this factor, how might you edit your filters to stay under the limit? Simply reflect on this, you do not need to code it.

### Part 3

Now, we're going to take a look at real data from the Department of Housing and Urban Development. They don't have public datasets with personal information like the example we used, but they do have data we can work with. Take a look at `hud.py`.

This snapshot of the HUD dataset contains a simple dictionary of the homeless population of San Luis Obispo county separated into age brackets.

You've been assigned a similar task as before: SLO county only has resources to provide temporary housing to `50` people. However you decide to allocate these resources is up to you. **Your job is to create a dictionary just like the one provided, but with only 50 total people.**

It is key for you to consider all factors before coding anything. What other information might you be able to extrapolate from age? It can be tough without additional information, but when dealing with very large numbers, it might not be available. Do your best and use your best judgement.

### Conclusion

After having created your dictionary, reflect on what challenges you now realize programmers might face when tackling real-world problems.

In about 150 words, answer these questions:

What do you think about the additional resposibilities programmers have when problem-solving?
What do you think would make it easier for you, a progammer, to make complex decisions?
How do you view computer science after considering the social impact?



