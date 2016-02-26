# ladynerds_site

LadyNerds are an organization comprised of people who graduated from the Hackbright Academy coding bootcamp.  There are roughly 300 of us working in a variety of roles within the tech industry, primarily in San Francisco, but also places like Seattle, Portland, and New York. 

## Table of Contents
- [About the Site](https://github.com/beckastar/ladynerds_site#about-the-site)
- [Tracking Progress](https://github.com/beckastar/ladynerds_site#tracking-progress)
    - [Making an Issue](https://github.com/beckastar/ladynerds_site#making-an-issue)
    - [Tags](https://github.com/beckastar/ladynerds_site#tags)
    - [Suggested Workflow](https://github.com/beckastar/ladynerds_site#suggested-workflow)
- [How To Contribute](https://github.com/beckastar/ladynerds_site#how-to-contribute)
    - [Set Up a Local Repo](https://github.com/beckastar/ladynerds_site#set-up-a-local-repo)
    - [Keep Repos in Sync](https://github.com/beckastar/ladynerds_site#keep-repos-in-sync)
    - [Choose An Issue](https://github.com/beckastar/ladynerds_site#choose-an-issue)
- [Tips and Tricks](https://github.com/beckastar/ladynerds_site#tips-and-tricks)

## About the Site
This CRUD webapp is an ongoing collective project! Any LadyNerd is welcome to contribute. There are instructions for getting started below. Check out the 'issues' tab for things that need to be done.

## Tracking Progress
We're tracking progress using GitHub's Issues. 
Things to remember:
- **Check** the comments of an issue before getting started, to get up-to-date on its progress.
- **Leave** good comments! Starting work on an issue? Claim it! Stopping? Let people know how far you got, and push your branch up.
    
#### Making an Issue
@Lavinia is working on an Issues template, but in the meantime,
**please:**
- Remember each issue should be a doable chunk that one person can accomplish.
- Break down the feature into a checklist using [  ]'s.
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

#### Suggested workflow
**Kelsey** thinks it would be great if we had a dancing kitten on the front page. She makes an issue called "Dancing Kitten". She tags it "good-for-beginner", because it should be pretty simple, and  "help-wanted", because she doesn't have time to do it right now. She also links to a kitten gif, and adds a checklist:
- [ ] Put kitten gif into static/images folder
- [ ] Link to image on main page
- [ ] Adjust CSS to make sure it fits in with the other content

**Shadow** is looking for a fairly simple issue to get started on. They see "Dancing Kitten" and love the idea! They add a comment onto the issue:
> Awesome idea! I'm working on it now :)

Shadow gets everything set up on their machine, then makes a new branch for their work: `kitten-dance`. They work through the checklist, being sure to commit often and ask questions when they get stuck. When they're done, they make sure `kitten-dance ` is up to date with `static`, then push their **whole branch** up to the main repo (they don't merge it yet, because they want a code review first). Then Shadow makes a **pull request** and links it to the issue. Back in the issue, they add another comment and close the issue:
> Finished! I made a pull request for branch 'kitten-dance' and would love a code review

**Sydney** sees an open pull request, so she checks out their code. Everything looks good, she accepts the pull request, and *tada!* Now we have dancing kittens on the front page.

## How to Contribute:
#### Set Up Local Repo
You can either message Becka to be added as a contributor, or you can take the following steps:

**Fork the Repo:** (there's a button in the upper right part of your screen)
- This makes a copy of the repo on your github
- It makes it so you can push up changes without needing to be an official/listed contributor

**Clone Your New Repo Copy:**
```sh
$ git clone https://github.com/[your-username-here]/ladynerds_site.git ladynerds_site
$ cd ladynerds_site
```

#### Keep Repos in Sync:
**If you're not a contributor** to the main repo, you'll have to submit pull-requests from **your** github repo, rather than this one.
Before you can make a pull request, pull and merge any updates from the orginal repo:
* First, [configure your remote](https://help.github.com/articles/configuring-a-remote-for-a-fork/)
* Next, [get changes from the original repo](https://help.github.com/articles/syncing-a-fork/)
    * (substitute "static" for "master" if your updates are in that branch)
    * (changes to this README should be done in master)
* Finally, [update YOUR github repo with your sync'ed and merged local changes](https://help.github.com/articles/pushing-to-a-remote/)
* Now you can submit a pull request!

Keep in mind that if there are changes to both static and master, you will need to go through the fetch, merge, and push steps of this process in both branches

**If you are a contributor:**
- You have write access to the main repo. 
- Make sure to make new branches for your changes!
- Update your branch with the static branch before submitting a pull request, so merging will be easier.

```sh
$ git branch
  master
  static
* my-branch
$ git pull origin static
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

**Checkout Static Branch:**
This is where we're currently working. It's rough, I know.

See what branches you have locally:
```sh
$ git branch
* master
  static
```

*If you only see master, get the static branch from your online repo:
```sh
$ git checkout --track origin/static
```

We're currently working on static, so check that out and make branches from there:
```sh
$ git checkout static
```

Now it should look like this when you 'git branch':
```sh
$ git branch
  master
* static
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
    - Make sure your pull request is comparing your local `issue` branch to the the original 
    repos `static` branch.
- It's very helpful to add the db.sqlite3 to your gitignore file while we're working without data 
- If you're a contributor, please get a code review before accepting your own pull requests :)

This is a screenshot of what you should see, currently (as of Feb 24, 2016), after you login. If it doesn't look like this, 

The site currently has a black header with a black navbar, with neon green font. If you see something else, you're on the wrong branch. 


Have fun!


