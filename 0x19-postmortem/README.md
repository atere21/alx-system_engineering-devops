

# A Post Moterm on server failure
## Issue Summary:
Duration of the outage: 2 hours, from 10:00 AM to 12:00 PM WAT.

Impact: The Nginx server was down, resulting in slow loading times for the company's e-commerce website. Approximately 85% of users were affected, and some reported error messages when trying to access the site.

Timeline:
• 10:00 AM: The issue was detected by a customer who reported slow loading times and error messages when trying to access the website. • 10:05 AM: An engineer noticed that the Nginx server was unresponsive and attempted to restart it. • 10:10 AM: The engineer received an error message stating that the server could not be restarted. • 10:15 AM: The engineer escalated the issue to the infrastructure team, who began investigating the issue. • 10:30 AM: The infrastructure team noticed that the server's CPU usage was abnormally high and began investigating further. • 11:00 AM: The team found that the server was running an outdated version of Nginx that was vulnerable to a known exploit. • 11:15 AM: The team updated Nginx to the latest version and restarted the server. • 11:30 AM: The server was confirmed to be responsive and the e-commerce website was fully functional. • 12:00 PM: The outage was declared over.

## Root cause and resolution:
The root cause of the issue was an outdated version of Nginx that was vulnerable to a known exploit. This allowed an attacker to overload the server and bring it down. The issue was fixed by updating Nginx to the latest version and restarting the server. This prevented the exploit from being used to bring down the server again. Corrective and preventative measures:

To prevent similar issues in the future, the infrastructure team will implement the following measures:
• Regularly check for updates to server software and apply them in a timely manner. • Implement a monitoring system that alerts the team when CPU usage on a server is abnormally high. • Conduct regular security audits to identify potential vulnerabilities and address them before they can be exploited. • Provide training to all engineers and staff on security best practices to minimize the risk of human error causing a security breach.![535FD85B-C9B5-4648-9107-F8F92068E1AF](https://github.com/atere21/alx-system_engineering-devops/assets/106532533/0690c644-a319-484f-9415-e8297085c884)


### TODO:
• Patch all servers running outdated software. • Set up monitoring alerts for high CPU usage on all servers. • Conduct a security audit of all servers and implement any necessary changes. • Schedule regular security training sessions for all engineers and staff.
