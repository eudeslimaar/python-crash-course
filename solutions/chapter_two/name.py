name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "Ada"
last_name = "Lovelace"

full_name = f"{first_name} {last_name}"
print("Full name: "+full_name)

print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = ' python '
favorite_language = favorite_language.rstrip()
print(favorite_language)
favorite_language = favorite_language.lstrip()
print(favorite_language)
favorite_language = favorite_language.strip()
print(favorite_language)

nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)
