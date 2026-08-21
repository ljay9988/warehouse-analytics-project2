# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Project Warehouse analytics
project warehouse analytics analyses the DataCo Supply Chain dataset focusing on shipping performance, delivery reliability, product/category patterns, and geographic delivery outcomes.

## Dataset Content
This project uses the DataCo supply chain datset, a large real-world supply chain data set containing
- Order information
- shipping details
- delivery status
- product information
- customer location
The datset was large and after running the ETL pipeline the file reached over 100MB which caused github to reject the push. To resolve this the cleaned dataset was added to '.gitignore', the file was removed from git tracking using 'git rm --cached', and the cleaned datset is generated locally in VSCode.

## Business Requirements
1. analyse delivery performance across all orders
- identify how many deliveries are late vs on time
- understand factors contributing to late deliveries
- measure the difference between scheduled and actual shipping days
2. Evaluate the impact of shipping mode on delivery outcomes
- compare late delivery risk across different shipping modes
- determine which shipping methods are most reliable
- highlight modes that consistently underperform
3. assess geographic delivery performance
- compare delivery reliability across countries and regions
- identify locations with higher late delivery risk
- explore whether distance affects delivery outcomes
4. prepare a clean, structured datset for future modelling and dashboarding
- ensure the ETL pipeline produces a reproducible cleaned dataset
- enable future predictive modelling (e.g preedicting late deliveries)
- support future dashboard development for operational monitoring


## Hypothesis
1. shipping mode affects the likelyhood of late delivery.
- group orders by 'shipping_mode
- calculate the percentage of late deliveries
- compare modes using bar charts and summary statistics
2. The difference between scheduled and actual shipping delays is a strong indicator of late delivery
- create a new feature (column) shipping_delay = days_for_shipping_real - days_for_shipment_scheduled
- compare shipping delay values between late vs on-time deliveries
- use boxplots or correlation analysis
3. Certain product categories have higher late delivery rates than others.  
- Group orders by category_name
- Calculate late delivery rate per category
- Visualise using grouped bar charts
4. Customer country influences delivery reliability.  
- Group orders by customer_country
- Calculate late delivery percentage per country
- Visualise using bar charts or geographic plots
5. Longer shipping distances increase the chance of late delivery.
- Approximate distance using latitude/longitude
- Compare distance ranges against late_delivery_risk
- Use scatter plots or boxplots

Project Plan
Outline the high-level steps taken for the analysis.
How was the data managed throughout the collection, processing, analysis and interpretation steps?
Why did you choose the research methodologies you used?
The rationale to map the business requirements to the Data Visualisations
List your business requirements and a rationale for mapping them to the Data Visualisations
Analysis techniques used
List the data analysis methods used and explain limitations or alternative approaches.
How did you structure the data analysis techniques? Justify your response.
Did the data limit you, and did you use an alternative approach to meet these challenges?
How did you use generative AI tools to help with ideation, design thinking and code optimisation?
Ethical considerations (optional)
Feel free to delete this section if this is a data visualisation only (unit 1 or 2) project submission.
Were there any data privacy, bias or fairness issues with the data?
How did you overcome any legal or societal issues?
Dashboard Design (optional)
Feel free to delete this section if this is a data visualisation only (unit 1 or 2) project submission.
List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
Later, during project development, you may revisit your dashboard plan to update a feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later you used another plot type).
How were data insights communicated to technical and non-technical audiences?
Explain how the dashboard was designed to communicate complex data insights to different audiences.
Unfixed Bugs
Please list any unfixed bugs and explain why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation are not valid reasons to leave bugs unfixed.
Did you recognise gaps in your knowledge, and how did you address them?
If applicable, include evidence of feedback received (from peers or instructors) and how it improved your approach or understanding.
Development Roadmap
What challenges did you face, and what strategies were used to overcome these challenges?
What new skills or tools do you plan to learn next based on your project experience?
Deployment (optional)
If this is a Unit 3 Streamlit, Power BI or Tableau Public project, then you can include a link here and explain how you hosted the dashboard.
Heroku (optional)
This section is necessary only if you are deploying a Streamlit app to Heroku as part of your submission for units 2 and 3.
The App live link is: https://YOUR_APP_NAME.herokuapp.com/
Set the .python-version Python version to a Heroku-22 stack currently supported version.
The project was deployed to Heroku using the following steps.
Log in to Heroku and create an App
From the Deploy tab, select GitHub as the deployment method.
Select your repository name and click Search. Once it is found, click Connect.
Select the branch you want to deploy, then click Deploy Branch.
The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App at the top of the page to access your App.
If the slug size is too large, then add large files not required for the app to the .slugignore file.
Main Data Analysis Libraries
Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.
Credits
In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials; however, it is important to be very specific about these sources to avoid plagiarism.
You can break the credits section into Content and Media, depending on what you include in your project.
Content
The text for the Home page was taken from the Wikipedia Article A
Instructions on how to implement form validation were taken from a Specific YouTube Tutorial
The icons in the footer were taken from Font Awesome
Media
The photos used on the home and sign-up page are from This Open-Source site
The images used for the gallery page were taken from this other open-source site
Acknowledgements (optional)
Thank the people who supported this project.
