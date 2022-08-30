from programming_language import ProgrammingLanguage

def main():
    python, ruby, visual_basic = languages() # Return from the languages function
    language = [ruby, python, visual_basic]
    print("The dynamically typed languages are: ")
    for i in language:
        if i.is_dynamic():
            print(i.field)


def languages():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    return python, ruby, visual_basic


main()