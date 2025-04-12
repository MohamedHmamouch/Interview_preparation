# Test Data Science

## Before starting

- Fork the project in your namespace and **make it private**.
- Go To `Repository settings` then `User and group access` then `Add members` (Top right).
- Add the following emails `bibiana.martinez@dataimpact.io`, `louis.denoyelle@dataimpact.io`, `maha.amami@dataimpact.io`, `raphael.person@dataimpact.io`, `samer.azar@dataimpact.io`, `sina.akhavan@dataimpact.io`

Some really important tips:

- Comments and automated tests are a BIG plus.
- To find examples of inputs and outputs, look at the unit tests.
- You might need pytest (and you can use any other packages).
- There are two main sections (Python & Data Science).
- Your answers for the Python section should be in the provided source files (in the `Python` folder).
- The Deep learning 2 is only dedicated to those applying for a CDI position.
- **Answering questions with a ðŸ”´ are considered mandatory for CDI.**
- You are allowed to use the internet, however, you should fully understand the code you've written.
- If you have any questions, don't hesitate to send an email to `bibiana.martinez@dataimpact.io`, `louis.denoyelle@dataimpact.io`, `maha.amami@dataimpact.io`, `raphael.person@dataimpact.io`, `samer.azar@dataimpact.io`, `sina.akhavan@dataimpact.io`

# Python

Even though unit tests are already provided for some questions, bonus points are given for adding more **(5 points)**

## Simple Python **(30 points)**

In this section we expect efficient code, meaning the time complexity should be at most linear O(n).

### ðŸ”´ Exercise 1 **(10 points)**

Complete the function `remove_null` that takes as input a string of comma separated substrings (of the form **"2076,3B,19C,138D,NULL,NULL"**) and remove the NULLs (they are not necessarily located at the end).

### ðŸ”´ Exercise 2 **(10 points)**

Complete the function `reverse_substrings` that takes as input a string, in the same format as in Exercise 1, and reverses the order of its substrings.

### ðŸ”´ Exercise 3 **(10 points)**

##### Find the Missing Number
Given a list of n-1 integers, all of which are in the range of 1 to n, find the missing number. The list has no duplicated values. Complete the function `find_missing_number` with the most **efficient** way to find the missing integer.

## Advanced Python **(40 points)**

### Exercise 1 **(10 points)**

Write the generator `random_gen` that generates random numbers (use random module) between 10 and 20 and stops once it has generated the number 15.

### Exercise 2 **(10 points)**

Rewrite `decorator_to_str` to force the functions `add` and `get_info` to return string values.

### Exercise 3 **(10 points)**

Rewrite `ignore_exception` so that it ignores the exception in its argument and returns None if this exception is raised.

### Exercise 4 **(10 points)**

Write the tests for the class `CacheDecorator` without modifying it.
Don't hesitate to add comment and explain your choice of tests.

Hint: note that some of your tests should not pass as this class is a bit buggy.

## Pandas **(20 points)**

### ðŸ”´ Exercise 1 **(10 points)**

+    **The files are located in Python/pandas/data**

1) Import raw data from the files `17-10-2018.3880.gz` and `18-10-2018.3880.gz` into dataframes `df1_1` and `df1_2`, these files contain the following columns:

+ **categorieenseigne -- Category assigned to product by retailer**
+ **prixproduit -- Product price in the shop**
+ **identifiantproduit -- Product's id in the shops**
+ **ean -- Product's EAN** - Useless in the test
+ **disponible -- Product's availability** - Useless in the test

2) For each row of the column `categorieenseigne` replace "Promotions" by "promo".

3) Import the file `back_office.csv.gz` into dataframe `df2` , this file contains the following columns:

+ **pe_ref_in_enseigne -- Products id in the shops**
+ **pe_id -- Data Impact's products id**
+ **p_id_cat -- Category assigned to product by Data Impact**

4) Merge the data of the dataframes `df1_1` and `df1_2` with `df2` into `df_merged_1` and `df_merged_2`

### Exercise 2 **(10 points)**

- Get the average price by Data Impact product from the two dataframes `df_merged_1` and `df_merged_2`. (write the `average_prices` function)

The function should ouput a dict: data impact product --> price

- For each dataframe (`df_merged_1`, `df_merged_2`), get the list of unique Data Impact products per category

The function should output two dicts:
- dict1 : category --> list of data impact product for df_merged_1
- dict2 : category --> list of data impact product for df_merged_2

## API **(15 points)**

### Exercise 1 **(10 points)**

For this exercise you will be using the functions `remove_null` and `reverse_substring` developed on the Simple Python section.

In `api.py`, write a web service that listens on port `12345` and has a POST route `clean_string`.

This route should take a `raw_string` parameter and return a clean version of it as a response.

+ **raw_string**: string in the same format as expected for functions `remove_null` and `reverse_substring`
+ **response**: string, result of having applied both `remove_null` and `reverse_substring` to the input

Hint: you can use the flask library (or any library that suits you) to build the web service.

### Exercise 2 **(5 points)**

Write the `Dockerfile` so your web service can run in a Docker container and still work properly

The commands to build the image and run the container should be in `run.sh`

# Data Science

For this section you will receive an email with a form to fill with all the answers.
Some of the answers will need to be answered in a colab notebook.
You will find all the details in the mail sent.