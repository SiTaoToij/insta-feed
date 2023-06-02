# insta-feed

With this code you can constatly get the information of any new post from any Instagram page you want (using Discord, Feedbro and Instaloader).


How to prepare things:

Feedbro: Install the "Feedbro" extension in your browser -> Open a Instagram page and select the Feedbro extension -> Select "Find Feeds in Current Tab" and then "Subscribe"

Discord: Create a new bot and add it to your server -> Richt click over your channel name and select "Edit Channel" -> Select "Integration" then "New webhook" -> Select the new webhook and click "Copy webhook URL"

Back to Feedbro: Select the Feedbro extension and click "Open Feed Reader" -> Select "Rules" then "Add New Rule" -> Select "Add Action" then change from "Desktop notification" to "Discord HTPP POST URL" and paste the webhook URL right in front of it.

A few notes:
  -You can use Discord and Feedbro to better select you content (ex: You can add a page to a different folder in Feedbro and then send it     to a new channel on Discord)
  -I'm not sure if it's possible to download multiple media from the post (More than 1 photo/video)

This code was created because I couldn't find anyone saying how to use Discord with Feedbro, the only place that I found was this chinese post https://hackmd.io/@haruhi3745/rkgz8f76F (It's really good btw), and using Feedbro, Instaloader and Discord was the most realiable in my case.
