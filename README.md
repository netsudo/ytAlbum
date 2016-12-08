<header>ytDL</header>

If you've ever used a free youtube mp3 downloader, you'd know it's frustrating when you want an album, but it gives you the entire mp3. It's not practical, we all want to know what song we're listening to.

ytDL is an album downloader for Youtube. Typically albums uploaded to Youtube have descriptions with the timestamps and titles in the description. By parsing the timestamps and titles, you're able to download the m4a and cut it into m4a's for the individual songs using FFMPEG on the back-end.

If the uploader didn't include a timestamped description, then a manual option has been added so you can cut it up yourself. Just add the titles and the timestamps and you can download any song from the album, or all of them.

ytDL is made with Flask, currently it's still in production. The files are being served with a POST request to work on a local machine. If it were to go into production send_from_directory would be removed, and the files would be served with NGINX instead.

As far as functionality goes, everything is working smoothly thus far. A fork will come soon with a more modern theme. There's also some minor fixes that still have to be made. For instance, input checking for the manual options and Flask alerts for errors, but this project was just made to test out Flask and play around, so moving on from this one soon.
