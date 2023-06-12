Postmortem: SSL Configuration Fiasco

Issue Summary:
Duration: May 5, 2023, 08:00 - May 5, 2023, 10:30 (PST)
Impact: Users attempting to access the website without the "www" subdomain stumbled upon an unsecure version of the site, introducing a touch of excitement in their otherwise mundane browsing activities. Approximately 30% of users experienced this delightful surprise during the outage period.

Timeline:

May 5, 2023, 08:00 (PST): An adventurous user reported accessing the website without the "www" subdomain and discovered an unsecure connection, adding a dash of insecurity to their digital exploration.
Being a one-person IT department, I sought advice and guidance from my developer friend, Sam, my mentor, Leykun, and my peer group on WhatsApp, who all graciously pointed me in the right direction for resolving the SSL configuration fiasco.
Actions taken: Armed with their valuable advice, I dove into the labyrinth of SSL certificate configuration, traversing the treacherous logs in search of answers like an intrepid explorer.
Misleading investigation paths: Initially, I suspected misconfigured servers and even questioned the firewall's loyalty, but they turned out to be innocent bystanders in this amusing tale.
Utilizing the collective wisdom shared by Sam, Leykun, and my peer group, I focused my investigation on specific areas, narrowing down the potential causes of the SSL configuration issue.
May 5, 2023, 10:30 (PST): The incident reached its grand finale as I, armed with the insights and advice provided, successfully configured the website to redirect all non-secure connections to the secure version, ensuring a harmonious browsing experience for all adventurers.
Root Cause and Resolution:
The root cause of this SSL configuration fiasco was the absence of a redirection rule for non-secure connections. Users bravely venturing to the website without the "www" subdomain were left to wander aimlessly in the unsecure wilderness.

To resolve the issue, the following steps were taken:

Deployed a magnificent redirection rule: Incorporating the advice from Sam, Leykun, and my peer group, I added a redirection rule to the web server configuration, guiding all lost souls from the realm of non-secure connections to the glorious land of security.
Tested the rule's might: With their guidance, I conducted rigorous testing to ensure that every non-secure connection was skillfully redirected to the secure version, leaving no room for ambiguity or confusion.
Employed vigilant log monitoring: Leveraging the insights shared, I implemented a monitoring system to keep watch over the web server logs, ensuring that no mischievous unsecure connections dared to disturb the newfound harmony.
Corrective and Preventative Measures:
To prevent future episodes of this delightful chaos, the following measures have been enacted:

Embrace the art of meticulous SSL configuration: I will diligently review and enhance the SSL certificate setup for all subdomains, including the elusive non-www version.
Automation to the rescue: Utilizing the knowledge shared, I shall weave the magic of automation, empowering the web server with the ability to automatically redirect all non-secure connections to the secure realm, sparing users from any unwarranted surprises.
The quest for eternal vigilance: Incorporating the insights received, I shall establish a monitoring system that stands guard, ever watchful for any signs of SSL configuration mischief or unsecure connections, ensuring prompt rectification and the preservation of peace and security.
Tasks to Address the Issue:

Update the SSL configuration documentation, incorporating the valuable advice received, to include the specific steps for handling non-www domain redirection.
Empower the web server with the skills of automation, leveraging the knowledge shared, allowing it to gracefully redirect all non-secure connections to the secure path.
Conduct regular SSL configuration audits, embracing the insights received, to ensure compliance with best practices and industry standards.
Implement SSL certificate expiration monitoring and alerting, incorporating the suggestions provided, to prevent any unexpected disruptions due to certificates reaching their expiry date.
With these measures in place, the future of SSL configuration shall be secure, delightful, and tinged with a sprinkle of humor, as I recall the valuable advice and guidance received from my developer friend, mentor, and peer group during this amusing adventure.
