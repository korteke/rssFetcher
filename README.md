# rssFetcher

## Prerequisites

Python > 2.7.x < 3.x   
* Virtualenv   
* Pip --> requirements.txt   
``
feedparser==5.2.1   
jira==1.0.7   
oauthlib==1.1.2   
requests==2.11.1   
requests-oauthlib==0.6.2   
requests-toolbelt==0.7.0   
six==1.10.0   
tlslite==0.4.9   
``

## Install & Testing
``
[vagrant@localhost ~]$ virtualenv rssFetcher
[vagrant@localhost ~]$ source rssFetcher/bin/active
(rssfetcher)[vagrant@localhost fetcher]$ cd rssFetcher
(rssfetcher)[vagrant@localhost fetcher]$ git clone THIS_REPO
(rssfetcher)[vagrant@localhost fetcher]$ cd rssFetcher
(rssfetcher)[vagrant@localhost fetcher]$ pip install -r requirements.txt
(rssfetcher)[vagrant@localhost fetcher]$ python parser.py
``
After that you should see something like this:

`New vulnerablilities`
`Haavoittuvuus 110/2016: Haavoittuvuuksia Ciscon tuotteissa - https://www.viestintavirasto.fi/kyberturvallisuus/haavoittuvuudet/2016/haavoittuvuus-2016-110.html`   
`Creating JIRA ticket`   
`Created JIRA ticket TES-13`   


