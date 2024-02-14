favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print("%s's favorite language is %s." % (name.title(), language.title()))


print('\nOnly the key:')

for name in favorite_languages.keys():
    print(name.title())

print('\nOnly the value:')
for language in favorite_languages.values():
    print(language.title())
