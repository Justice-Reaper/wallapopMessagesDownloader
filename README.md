# wallapopMessagesDownloader
A Python script to download and save Wallapop inbox messages using the Wallapop API. Authenticates with a bearer token, fetches paginated conversations, and writes sorted text messages with timestamps and item details to a text file

## Obtain Bearer Token
To get the bearer token, we need to log in to Wallapop, open the developer tools, and filter by accessToken

![accessToken](/img/image_1.png)

## Help Panel

```
# python wallapopMessagesDownloader.py -h
usage: wallapopMessagesDownloader.py [-h] -t TOKEN

Download Wallapop messages

options:
  -h, --help         show this help message and exit
  -t, --token TOKEN  Bearer authentication token
```

# Usage

```
# python wallapopMessagesDownloader.py -t eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0NDU0NjQzODIiLCJkZXZpY2UiOiIzNWRkZGVhZi04Nzg5LTRlMmItYWQ5NS1hY2EyOWYyMjgzYzQiLCJpYXQiOjE3NTEzOTc4OTAsImV4cCI6MTc1MTQ4NDI5MH0.yPRvZjoQxTITb9Z2xgjkaUxrKxwdrItiTfo3eY63wRo-DseTpJHAEqpMb7TcvFzcai7tT3p-OgMLYrJWINV1xG71IRqdKyOF9LEM-cWVVro3sQulHMf5tqf9r-T0MLj2Jv9yTUJDyjoDAeu1NECqhTb68VDwQXFZ8LLRHqldhXhVHo0hU10yqJBsQGB-X_PBKpn_r9aUDqmf9VxOPMFYr7ArcFlsbMaZD-KOQ-vXjyv5GGIGBCgmGU2Yr-xXUAoObuOFIpQ-khQJ83LkcU7mMKa-e2pPid5wgBPoesx1wHlbsFGrMFLqSiW7lZRcB_oWA569KtG7_BMcMR8Tyl36NQ 
Messages saved to 'wallapop_messages.txt'
```

# Output

```
Conversation about: iPhone 6S 64GB - Gold and White (with Liberr)
--------------------------------------------------
[2025-06-24 02:41:04] Liberr: Hi, does the camera work well?
[2025-06-24 12:58:49] You: Yes, everything works fine.
[2025-06-24 12:59:15] You: The screen has a cracked glass, but the touch works perfectly.
[2025-06-24 13:46:56] You: It has 64GB, a new battery, and works perfectly.
[2025-06-24 13:47:05] You: Let me know if you have any questions, cheers!
[2025-06-24 13:50:45] Liberr: Alright, thanks a lot.
[2025-06-24 13:50:53] Liberr: One more thing, what's the price?
[2025-06-24 13:50:55] Liberr: ?
[2025-06-24 14:14:05] You: 20€
[2025-06-24 14:14:25] You: I had it at 25, lowered it to 20 because there's another interested buyer.
[2025-06-24 14:14:40] You: 👍🏼
[2025-06-24 14:44:30] Liberr: Alright, thanks a lot.

==================================================

Conversation about: iPhone 6S 64GB - Gold and White (with Andrei sergiu)
--------------------------------------------------
[2025-06-21 17:00:43] You: 20?
[2025-06-21 20:33:54] Andrei sergiu: OK
[2025-06-21 22:59:11] You: Ready, you can buy it.
[2025-06-21 22:59:20] You: *Can
[2025-06-21 23:00:14] Andrei sergiu: OK
[2025-06-22 20:46:35] You: Are you going to buy it in the end? Someone else is asking about it.
[2025-06-22 20:46:52] Andrei sergiu: Hi
[2025-06-22 20:47:03] Andrei sergiu: I'm waiting for a response.
[2025-06-22 20:47:34] Andrei sergiu: Once I get confirmation, I'll buy it.
[2025-06-22 21:25:37] You: Okay, thanks.
```
