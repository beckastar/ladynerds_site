# ladynerds_site

Ladynerds are an organization comprised of women who graduated from the Hackbright Academy coding bootcamp.  There are roughly 300 of us working in a variety of roles within the tech industry, primarily in San Francisco, but in other locations as well. 

This CRUD webapp is a collective project that will have the following features as part of the MVP:

- Display all users and skills 
- Google Cal integration:   https://developers.google.com/google-apps/calendar/quickstart/python#prerequisites
- Good UI


We've chosen to use the old terminal color scheme of green on a black background.  

The green color hex value: #00ff00
The terminal font is in google fonts: https://www.google.com/fonts/specimen/VT323

Nice to haves:
- Slack integration 

Currently has:
- Login /logout 
- About page url 
- Profile page
- working navbar 

## How to Contribute:

Fork the repo (there's a button in the upper right part of your screen)
- This makes a copy of the repo on your github
- It makes it so you can push up changes without needing to be an official/listed contributor

Clone repo:
```sh
$ git clone https://github.com/[your-username-here]/ladynerds_site.git ladynerds_site
$ cd ladynerds_site
```

We're currently working off of the 'static' branch, so check that out:
```sh
$ git checkout static
```
* (changes to this README should be done in master)

If that doesn't work (because you only have a master branch, locally), try:
```sh
$ git checkout --track origin/static
```
Acvtivate a virtual environment and install dependencies:
```sh
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

Before you can sync any changes with the orginal repo, [Configure your remote]
(https://help.github.com/articles/configuring-a-remote-for-a-fork/)

[Get changes from the original repo (but substitute "static" for "master")]
(https://help.github.com/articles/syncing-a-fork/)

And have fun! 
- Check out the 'issues' for features that we'd like to work on, or are already working on.
- If you do some work, submit a pull request and be sure to comment with whatever work you've done. This will make it easier for other folks to help without duplicating code
    - If you keep working, keep pushing! The pull request will keep updated.
- If you're a contributor, please get a code review before accepting your own pull requests :)

