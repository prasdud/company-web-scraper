My solution

Sort the companies from biggest to smallest since bigger companies have a higher probability that they are hiring, therefore more jobs.

i will run a google dork search for website and linkedin URLs

i will navigate the website and scrape for a careers or jobs section, first i will check if the jobs section is same as careers so i dont have to waste time looking for both

once found i will scrape the top 3 jobs

im thinking of having a verification function running parallely while the main function is running to verify the data in the pipeline. if the data is invalid or corrupted, the verifier will just delete the data else it will move on

im also thinking of having workers to parallely run the software, 1 worker for 10 companies at a time, it will be faster although worried about rate limiting


although i am now thinking i should focus and sort the list based on service providers like zoho and lever since their HTML formatting will be similar across postings hence easier to scrape



i now see that not all websites would have a regular companyName.com, so i will have to take the company description along with the company name in the google dork


It has been almost 1 hour since starting, its not as easy as it looks but very interesting

some companies return the correct dork result without the long description, however some require the description else they return the wrong website. i will have to summarize the description or extract 2 -3 keywords maybe using AI



ISSUE
for tomra.com the /careers page exists but my scraper is not picking it up, upon further inspection i realized that when running curl with the /careers link it throws a 403. which means its not my mistake but cloudflare is blocking the scraper.

so right now i cant access that page but GPT had a solution that i dont need to access the page i just need to know it exists - very smart


END OF DAY 1
running the script i get 80 job postings. i will need to have more aggresive and indepth fallback for the job scraper
good news - it gets the website linkedin careers page 
needs to get more job post listings and jobs