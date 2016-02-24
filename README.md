# ladynerds_site

Ladynerds are an organization comprised of people who graduated from the Hackbright Academy coding bootcamp.  There are roughly 300 of us working in a variety of roles within the tech industry, primarily in San Francisco, but in other locations as well. 

This CRUD webapp is a collective project that will have the following features as part of the MVP:

- Put all of our info that is currently in Google Docs in one central place 
- Google Cal integration:   https://developers.google.com/google-apps/calendar/quickstart/python#prerequisites
- Good UI
- Eliminate the need for google docs by

We've chosen to use the old terminal color scheme of green on a black background.  

The green color hex value: #00ff00

The terminal font which we're using for the logo and navbar is in google fonts: https://www.google.com/fonts/specimen/VT323

Nice to haves:
- Slack integration 

Currently has:
- Login /logout 
- About page url with data  
- Profile form 
- working navbar 
- Resources page stub
- LN Twitter feed stub 
- Code of Conduct stub 

Stubs have a view, url, and a link from the navbar, but lack content. 

## How to Contribute:

Install Django with pip, and activate your virtual environment.  The Django official tutorial is a great way to learn Django, but for this simple webapp, is probably not necessary for contributing. 

You can either message Becka to be added as a contributor, or you can take the following steps:

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

If that doesn't work (because you only have a master branch, locally), try:
```sh
$ git checkout --track origin/static
```

## How to Run the site locally:

Acvtivate a virtual environment and install dependencies:
```sh
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

After you've installed Django:

$ python manage.py runserver

And now you can view the site locally at http://localhost:8000/


## How to keep your repos in sync :

Before you can make a pull request, pull and merge any updates from the orginal repo:
* First, [configure your remote](https://help.github.com/articles/configuring-a-remote-for-a-fork/)
* Next, [Get changes from the original repo](https://help.github.com/articles/syncing-a-fork/)
	* (substitute "static" for "master" if your updates are in that branch)
	* (changes to this README should be done in master)
* Finally, [update YOUR github repo with your sync'ed and merged local changes](https://help.github.com/articles/pushing-to-a-remote/)
* Now you can submit a pull request!

Keep in mind that if there are changes to both static and master, you will need to go through the fetch, merge, and push steps of this process in both branches

## General Stuff to keep in mind:

- Check out the 'issues' for features that we'd like to work on, or are already working on.
    - IMPORTANT: Before you start working on your local repo, make a local branch for the issue
    you are working on.  Do all of your work for that issue on that branch.  This will make pull
    requests less confusing for everyone later on.
- If you do some work, submit a pull request and be sure to comment with whatever work you've done. 
This will make it easier for other folks to help without duplicating code.
    - If you keep working, keep pushing! The pull request will keep updated.
    - Make sure your pull request is comparing your local issue branch to the the original 
    repos 'static' branch.
- If you're a contributor, please track the feature you're working on.  Ask Becka for access to the Spreadsheet in Google Docs that tracks all the issues. 
- If you're a contributor, please get a code review before accepting your own pull requests :)

This is a screenshot of what you should see, currently (as of Feb 24, 2016), after you login:





Have fun!


