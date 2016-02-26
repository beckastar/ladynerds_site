# ladynerds_site

LadyNerds are an organization comprised of people who graduated from the Hackbright Academy coding bootcamp.  There are roughly 300 of us working in a variety of roles within the tech industry, primarily in San Francisco, but also places like Seattle, Portland, and New York. 

This CRUD webapp is a collective project that will have the following features as part of the MVP:

- Put all of our info that is currently in Google Docs in one central place 
- Google Cal integration:   https://developers.google.com/google-apps/calendar/quickstart/python#prerequisites
- Good UI

We've chosen to use the old terminal color scheme of green on a black background. The green color hex value: #00ff00

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

Stubs have a view, url, and a link from the navbar, but lack content and logic. 

## How to Contribute:

### Set Up Local Repo

You can either message Becka to be added as a contributor, or you can take the following steps:

**Fork the Repo:** (there's a button in the upper right part of your screen)
- This makes a copy of the repo on your github
- It makes it so you can push up changes without needing to be an official/listed contributor

**Clone Your New Repo Copy:**
```sh
$ git clone https://github.com/[your-username-here]/ladynerds_site.git ladynerds_site
$ cd ladynerds_site
```

**Checkout Static Branch:**
See what branches you have locally:
```sh
$ git branch
* master
  static
```
We're currently working on static, so check that out and make branches from there:
```sh
$ git checkout static
```

*If you only see master, get the static branch from your online repo:
```sh
$ git checkout --track origin/static
```

Now it should look like this when you 'git branch':
```sh
$ git branch
  master
* static
```
## Run the site locally:

Acvtivate a virtual environment and install dependencies, like Django:
```sh
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

After you've installed the dependencies:

```sh
$ python manage.py runserver
```
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
- It's very helpful to add the db.sqlite3 to your gitignore file while we're working without data 
- If you're a contributor, please get a code review before accepting your own pull requests :)

This is a screenshot of what you should see, currently (as of Feb 24, 2016), after you login. If it doesn't look like this, 

The site currently has a black header with a black navbar, with neon green font. If you see something else, you're on the wrong branch. 


Have fun!


