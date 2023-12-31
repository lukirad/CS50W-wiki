# CS50W - Project1 - Wiki

Project 1 for CS50’s Web Programming with Python and JavaScript: design a Wikipedia-like online encyclopedia using Python's web framework Django, HTML and CSS.

## Youtube Video
A short video outlining the required specifications of the project: TBA

## Specification
- **Entry Page**: Visiting `/wiki/TITLE`, where `TITLE` is the title of an encyclopedia entry, renders a page that display the contents of that encyclopedia entry.
    - The view gets the content of the encyclopedia entry by calling the appropriate `util` function.
    - If an entry is requested that does not exist, the user is presented with an error page indicating that their requested page was not found.
    - If the entry does exist, the user is presented with a page that displays the content of the entry. The title of the page includes the name of the entry.
- **Index Page**: Updated `index.html` such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.
- **Search**: User is allowed to type a query into the search box in the sidebar to search for an encyclopedia entry.
    - If the query matches the name of an encyclopedia entry, the user is redirected to that entry’s page.
    - If the query does not match the name of an encyclopedia entry, the user is instead taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were `ytho`, then `Python` appears in the search results.
    - Clicking on any of the entry names on the search results page takes the user to that entry’s page.
- **New Page**: Clicking “Create New Page” in the sidebar takes the user to a page where they can create a new encyclopedia entry.
    - Users are able to enter a title for the page and, in a [`textarea`](https://www.w3schools.com/tags/tag_textarea.asp), are able to enter the Markdown content for the page.
    - Users are able to click a button to save their new page.
    - When the page is saved, if an encyclopedia entry already exists with the provided title, the user is presented with an error message.
    - Otherwise, the encyclopedia entry is saved to disk, and the user is taken to the new entry’s page.
- **Edit Page**: On each entry page, the user is able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a `textarea`.
    - The `textarea` is pre-populated with the existing Markdown content of the page. (i.e., the existing content is the initial `value` of the `textarea`).
    - The user is able to click a button to save the changes made to the entry.
    - Once the entry is saved, the user is redirected back to that entry’s page.
- **Random Page**: Clicking “Random Page” in the sidebar takes user to a random encyclopedia entry.
- **Markdown to HTML Conversion**: On each entry’s page, any Markdown content in the entry file is converted to HTML before being displayed to the user. To perform this conversion the [`python-markdown2`](https://github.com/trentm/python-markdown2) package was used, installable via `pip3 install markdown2`.

## Setup
Requires Python3 and the package installer for Python (pip) to run:

* Install requirements (Django4 and Markdown2): `pip install -r requirements.txt`
* After cloning the repository, refer to the project folder and run the app locally: `python3 manage.py runserver`
* Visit the site: `http://localhost:8000` and you are ready to go!

## Topics
Built with [`Python`](https://www.python.org/downloads/), [`Django`](https://www.djangoproject.com/), [`Markdown`](https://pypi.org/project/Markdown/), [`Bootstrap 4.4`](https://getbootstrap.com/docs/4.4/getting-started/introduction/) and HTML/CSS.
