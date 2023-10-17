from django.test import TestCase

# Create your tests here.
def edit(request, title):
    content = util.get_entry(title)
    if request.method == "POST":
        if content:
            content = request.POST.get("content")
            title = request.POST.get("title")
            util.save_entry(title, content)
            return render(request, "encyclopedia\entry.html", {
            "entry_title": title,
            "content": content
            })
        return render(request, "encyclopedia\edit.html", {
        "entry_title": title,
        "content": content
        })