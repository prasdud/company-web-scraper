My solution

Sort the companies from biggest to smallest since bigger companies have a higher probability that they are hiring, therefore more jobs.

i will run a google dork search for website and linkedin URLs

i will navigate the website and scrape for a careers or jobs section, first i will check if the jobs section is same as careers so i dont have to waste time looking for both

once found i will scrape the top 3 jobs

im thinking of having a verification function running parallely while the main function is running to verify the data in the pipeline. if the data is invalid or corrupted, the verifier will just delete the data else it will move on

im also thinking of having workers to parallely run the software, 1 worker for 10 companies at a time, it will be faster although worried about rate limiting


although i am now thinking i should focus and sort the list based on service providers like zoho and lever since their HTML formatting will be similar across postings hence easier to scrape



i now see that not all websites would have a regular companyName.com, so i will have to take the company description along with the company name in the google dork