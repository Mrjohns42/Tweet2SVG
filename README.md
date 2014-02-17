#TWEET2SVG

## Download Code and Dependencies
	### Get pip
		sudo apt-get install pip
	### Get tweepy
		sudo pip install tweepy
	### Get tweet2svg source code
		cd

		git clone git@github.com:Mrjohns42/Tweet2SVG.git tweet2svg

		cd tweet2svg

## Create Twitter App
	- Go to:  https://apps.twitter.com/new
	- Log in and fill out new application
	- Copy CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
	  to oAuth.py

## Using tweet2svg
	### Change to tweet2svg directory
		cd

		cd tweet2svg

	### To run the script and collect all tweets
		./tweet2svg

	### To run the script looking for specific hashtags
		./tweet2svg hashtag1 hashtag2

		(arguments should exclude the '#' character)

	### To end the script
		CTRL + C in the terminal where tweet2svg is running

	### The output
		SVG images are stored in the tweet2svg/image folder
		Images will accumulate there as long as the script is running
		Re-running the script will delete the old images and start fresh

