import wikipedia


def search():
    phrase = str(input("Please enter a search phase: "))
    while phrase != "":
        for entry in wikipedia.search(phrase):
            page = wikipedia.page(entry)
            print(f"Title: {page}")
            print(f"Summary: {page.summary}")
            print(f"URL: {page.url}")
            try:
                print(wikipedia.summary(page))
            except wikipedia.exceptions.DisambiguationError as e:
                print(e.options)
            except wikipedia.exceptions.PageError:
                print(phrase, "is not found on any pages. Please enter another search phrase")
            print()
        phrase = str(input("Please enter a search phase: "))
    print()


search()