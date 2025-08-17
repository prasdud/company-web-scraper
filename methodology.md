My Solution

Sort the companies from biggest to smallest since bigger companies have a higher probability that they are hiring, therefore more jobs.

I will run a Google dork search for website and LinkedIn URLs.

I will navigate the website and scrape for a careers or jobs section. First, I will check if the jobs section is the same as careers so I don't have to waste time looking for both.
Once found, I will scrape the top 3 jobs.

I'm thinking of having a verification function running in parallel while the main function is running to verify the data in the pipeline. If the data is invalid or corrupted, the verifier will just delete the data; otherwise, it will move on.

I'm also thinking of having workers to run the software in parallel, 1 worker for 10 companies at a time. It will be faster, although I'm worried about rate limiting.

Although I am now thinking I should focus and sort the list based on service providers like Zoho and Lever since their HTML formatting will be similar across postings, hence easier to scrape.

I now see that not all websites would have a regular companyName.com, so I will have to take the company description along with the company name in the Google dork.

It has been almost 1 hour since starting. It's not as easy as it looks but very interesting.
Some companies return the correct dork result without the long description; however, some require the description, otherwise they return the wrong website. I will have to summarize the description or extract 2-3 keywords, maybe using AI.

ISSUE
For tomra.com, the /careers page exists but my scraper is not picking it up. Upon further inspection, I realized that when running curl with the /careers link, it throws a 403, which means it's not my mistake but Cloudflare is blocking the scraper.
So right now I can't access that page, but GPT had a solution that I don't need to access the page; I just need to know it exists - very smart.

END OF DAY 1
Running the script, I get 80 job postings. I will need to have more aggressive and in-depth fallback for the job scraper.
Good news - it gets the website, LinkedIn, careers page.
Needs to get more job post listings and jobs.

FINAL EDIT
i was only able to get ~100 job postings which according to me is for the following reasons
    - cloudflare blocks a few job sites to prevent crawling, nothing i can do there
    - come job sites are JS heavy and embed postins in JSON, it would theoretically be possible to extract job posting but very time consuming and not guaranteed to work on every JS heavy site
    - most modern job sites use react / vue to load content via JS after page loads
    - a lot of companies were not hiring, the smaller ones which were had completely different job posting frontend code which would involve manually adding  in edge cases for that exact company - which would be a waste of time
    - if we increased to max job for a company to 5 or more, we could hit 200 postings or more
    - a few job postings pages are still active even when not currently hiring

THANK YOU
i was able to learn a lot from this and will definitely continue this project in my free time