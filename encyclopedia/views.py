from django.shortcuts import render
from . import util
from markdown2 import Markdown
from random import randint


def md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content:
        return markdowner.convert(content)
    else:
        return None


def index(request):
    # entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": search
    })


def entry(request, title):
    html_entry = md_to_html(title)
    if html_entry:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_entry
        })
    else:
        return render(request, "encyclopedia/error.html")


def search(request):
    form = request.GET.get('q')
    html_entry = md_to_html(form)
    if form is not None:
        entry = util.get_entry(form)

        if entry:
            return render(request, "encyclopedia/entry.html", {
                "title": form,
                "content": html_entry
            })
        else:
            entries = util.list_entries()
            matched = []

            for entry in entries:
                if form.lower() in entry.lower():
                    matched.append(entry)

            if len(matched) == 0:
                return render(request, "encyclopedia/error.html")
            else:
                return render(request, "encyclopedia/search.html", {
                    "title": form,
                    "matched": matched})
    else:
        entries = util.list_entries()
        return render(request, "encyclopedia/index.html", {
            "entries": entries
        })


def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        if util.get_entry(title) is None:
            util.save_entry(title, content)
            html_entry = md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_entry
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "message": "This entry already exists"
            })
    else:
        return render(request, "encyclopedia/create.html")


def edit(request, title):
    if request.method == "POST":
        content = request.POST["content"]
        title = request.POST["entry_title"]
        if content == "":
            return render(request, "encyclopedia/error.html", {
                "message": "Content cannot be empty"
            })
        else:
            util.save_entry(title, content)
            content = md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": content
            })
    else:
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "entry_title": title,
            "content": content
        })

def random(request):
    entries = util.list_entries()

    random_entry = entries[randint(0, len(entries) - 1)]
    html_entry = md_to_html(random_entry)

    return render(request, "encyclopedia/entry.html", {
        "title": random_entry,
        "content": html_entry
    })
