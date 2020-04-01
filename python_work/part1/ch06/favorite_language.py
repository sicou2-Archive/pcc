favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

print('NEXT')

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print('NEXT')

for name in favorite_languages.keys():
    print(name.title())

print('THIS IS THE SAME THING')

for name in favorite_languages:
    print(name.title())


print('NEXT')

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print("NEXT")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("NEXT")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")

print("NEXT")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("NEXT")
print("Unique languages")
for language in set(favorite_languages.values()):
    print(language.title())

print("NEXT")
print("SET")
languages = {'python', 'ruby', 'c', 'python'}
print(languages)