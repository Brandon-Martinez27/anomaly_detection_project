# Curriculum Logs Anomaly Detection
## About the Project
### Goals
- Answer questions from 'executive' by analyzing data from curriculum logs
- Use key findings to include in a single slide for presentation
- Document analysis with enough context to inform anyone reading of the anomalous behavior
### Background
Email from Executive:
>Hello,
>
>I have some questions for you that I need answered before the board meeting Thursday morning. I need to be able to speak to the following questions. I also need a single slide that I can incorporate into my existing presentation (Google Slides) that summarizes the most important points. My questions are listed below; however, if you discover anything else important that I didn’t think to ask, please include that as well. 
> 1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
> 2. Is there a cohort that referred to a lesson significantly more that other cohorts seemed to gloss over? 
> 3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students? 
> 4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses? Any odd user-agents? 
> 5. At some point in the last year, ability for students and alumni to cross-access curriculum (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before? 
> 6. What topics are grads continuing to reference after graduation and into their jobs (for each program)? 
> 7. Which lessons are least accessed? 
> 8. Anything else I should be aware of? 
>
>Thank you,
>Mrs. Executive

### Deliverables
- Jupyter notebook with analysis
- Google slide with key findings

### Acknowledgments
- Codeup Curriculum

## Project Steps
### Acquire
- Read data from a csv into a pandas dataframe
- Added the cohort information into a separate dataframe
### Prepare
- Adjusted the date and time columns to change dtype and set as the index
- Created a new dataframe for rows with missing cohort ids
- Fill the missing values with a 0 for a placeholder
- Adjusted datatypes
- Merge cohort info with data from cohort and original dataframes
- Drop all rows where the table of contents is accessed
- Drop rows where 'staff' member was the user
- Added three features based on time length
### Explore
- Visually or programmatically find answers to key questions (see workbook)
### Conclusions
- Looking further in to the data with no cohort_id, I've discovered that many of these users have multiple ip addresses (ranging from 1 to 29). It seems fishy to have any more than 5 ip addresses. These candidates who have several may be web scrapping the curriculum.
- I split these candidates into two groups
  - weird users (7):
    - users that have matching cohort information within the 'df' dataframe
  - non-users (68):
    - users that have no other information besides, user_id, ip_address, page viewed and the time stamp

## How to Reproduce
### Steps
1. Get the dataset you want to work with
2. Make sure to download the require libraries (see Tools & Requirements)
3. Explore your data!

### Tools & Requirements
python | pandas | numpy | math | sklearn | scipy | matplotlib | seaborn | requests

## Creators
- Brandon Martinez
