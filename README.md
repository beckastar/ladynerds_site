# ladynerds_site

LadyNerds are an organization comprised of people who graduated from the Hackbright Academy coding bootcamp.  There are roughly 300 of us working in a variety of roles within the tech industry, primarily in San Francisco, but also places like Seattle, Portland, and New York. 

## Table of Contents
- [About the Site](#about-the-site)
- [Tracking Progress](#tracking-progress)
    - [Making an Issue](#making-an-issue)
    - [Tags](#tags)
    - [Suggested Workflow](#suggested-workflow)
- [How To Contribute](#how-to-contribute)
    - [Set Up a Local Repo](#set-up-a-local-repo)
    - [Keep Repos in Sync](#keep-repos-in-sync)
    - [Choose An Issue](#choose-an-issue)
- [Tips and Tricks](#tips-and-tricks)

## About the Site
This CRUD webapp is an ongoing collective project! Any LadyNerd is welcome to contribute. There are instructions for getting started below. Check out the 'issues' tab for things that need to be done.

## Tracking Progress
We're tracking progress using GitHub's Issues. 
Things to remember:
- **Check** the comments of an issue before getting started, to get up-to-date on its progress.
- **Leave** good comments! Starting work on an issue? Claim it! Stopping? Let people know how far you got, and push your branch up.
    
#### Making an Issue
Please use the appropriate template when making a new issue 
(ISSUES_TEMPLATE_FEATURES.md for new features, changes, and other non-bug issues.
ISSUES_TEMPLATE_BUGS.md for issues about bugs)
- Remember each issue should be a doable chunk that one person can accomplish.
- Break the issue down into a checklist using [  ]'s.
    * A progress bar will magically appear on the issue
    * If someone only completes part of the work, folks have an idea of where to start
    * It's not as intimidating for less-experienced folks to get started
- Use good tags to describe the issue (see below for suggestions)

#### Tags
Tags help other people understand each issue! Here's some suggestions:
- `help-wanted`: This needs someone to help out
- `good-for-beginner`: For small or simple tasks that a fresh grad could easily handle. Please take some extra time and make notes or a checklist, to make it easy for folks to know what to do.
- **Category Tags:** Examples: `OAuth`, `Form`.
- `bug`: Something is broken, and not just because we haven't gotten there yet

#### Suggested workflow:
(Example)
**Kelsey** thinks it would be great if we had a dancing kitten on the front page. She makes an issue called "Dancing Kitten". She tags it "good-for-beginner", because it should be pretty simple, and  "help-wanted", because she doesn't have time to do it right now. She also links to a kitten gif, and adds a checklist:
- [ ] Put kitten gif into static/images folder
- [ ] Link to image on main page
- [ ] Adjust CSS to make sure it fits in with the other content

**Shadow** is looking for a fairly simple issue to get started on. They see "Dancing Kitten" and love the idea! They add a comment onto the issue:
> Awesome idea! I'm working on it now :)

Shadow gets everything set up on their machine, then makes a new branch for their work: `kitten-dance`. They work through the checklist, being sure to commit often and ask questions when they get stuck. When they're done, they make sure `kitten-dance ` is up to date with `mvp`, then push their **whole branch** up to the main repo (they don't merge it yet, because they want a code review first). Then Shadow makes a **pull request** and links it to the issue. Back in the issue, they add another comment and close the issue:
> Finished! I made a pull request for branch 'kitten-dance' and would love a code review

**Sydney** sees an open pull request, so she checks out their code. Everything looks good, she accepts the pull request, and *tada!* Now we have dancing kittens on the front page.

## How to Contribute:
#### Set Up a Local Repo
You can either message Becka to be added as a contributor, or you can take the following steps:

**Fork the Repo:** (there's a button in the upper right part of your screen)
- This makes a copy of the repo on your github
- It makes it so you can push up changes without needing to be an official/listed contributor
- Your forked repo on github will be your remote "origin"
- This is where you push your local work TO, and where you make pull requests FROM

**Clone Your New Repo Copy:**
- This is your local repo, where you make your changes
- You will manage your changes and merge with updates from your upstream here (see next topic below)

```sh
$ git clone https://github.com/[your-username-here]/ladynerds_site.git ladynerds_site
$ cd ladynerds_site
```

**Configure Your Remote Upstream
- Set up your local repo to be able to fetch changes from the main beckastar/ladynerds repo on github
- The beckastar/ladynerds repo on github will be your remote "upstream" 
* Here's how to [configure your remote](https://help.github.com/articles/configuring-a-remote-for-a-fork/)


#### Keep Repos in Sync:
**If you're not an official contributor:**
You'll have to submit pull-requests from **your** github repo, rather than the original one.

Before you can make a pull request you need to:
- Pull and merge any updates from the orginal "upstream" repo:
    - [How to get changes from the original repo](https://help.github.com/articles/syncing-a-fork/)
    - (substitute "mvp" for "master" if your updates are in that branch)
- Push your merged changes up to your remote "origin" repo
    - [How to update YOUR github repo with your sync'ed and merged local changes](https://help.github.com/articles/pushing-to-a-remote/)

Keep in mind that if you've made changes to both mvp and master, you will need to go through the fetch, merge, and push steps of this process in both branches.

Now you can submit a pull request!

**If you are an official contributor:**
- You have write access to the main repo. 
- Make sure to make a new branch for your changes!
- Update and merge your local branch with the mvp branch before submitting a pull request, so merging upstream will be easier.

```sh
$ git branch
  master
  mvp
* my-branch
$ git pull origin mvp
$ git push origin my-branch
```

This merges in any updates that have been made since the last time you did a git pull. This ensures that your pull request will only have **your** changes in it, rather than any changes that have happened since you made your branch. Then you push up your whole branch, so you can submit a pull request for it.

## Run the site locally:

**Activate a virtual environment and install dependencies:**
```sh
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

**Checkout `mvp` branch:**

This is where we're currently working (exception: changes to the README should be done in master)
See what branches you have locally:
```sh
$ git branch
* master
  mvp
```

*If you only see master, get the mvp branch from your online repo:
```sh
$ git checkout --track origin/mvp
```

We're currently working on mvp, so check that out and make branches from there:
```sh
$ git checkout mvp
```

Now it should look like this when you 'git branch':
```sh
$ git branch
  master
* mvp
```

**Run the web server:**

```sh
$ python manage.py runserver
```
And now you can view the site locally at http://localhost:8000/

#### Choose an Issue:
Check out the 'issues' tab (at the top of this repo) to find something you'd like to work on. (Be sure to read [this section on issues](https://github.com/beckastar/ladynerds_site#tracking-progress) before diving in, so you know how it all works.)


## Tips and Tricks:

- Check out the 'issues' for features that we'd like to work on, or are already working on.
    - IMPORTANT: Before you start working on your local repo, make a local branch for the issue
    you are working on.  Do all of your work for that issue on that branch.  This will make pull
    requests less confusing for everyone later on.
- If you do some work, submit a pull request/push up your branch and be sure to comment with whatever work you've done. 
This will make it easier for other folks to help without duplicating code.
    - If you keep working, keep pushing! The pull request will keep updated.
    - Make sure your pull request is comparing your local `issue` branch to the the original repos `mvp` branch.
- If you're a contributor, please get a code review before accepting your own pull requests :)

The site currently has a black header with a black navbar, with neon green font. If you see something else, you're on the wrong branch. 

The documentation for switching to Postgres can be seen at this URL:  https://docs.google.com/document/d/1bBNODYnMo0-DIkD0hXp7gFRexDhmvqZvySEWi8hVE3w/edit

Have fun!


