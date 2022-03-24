languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}
# print("Python was created by {Python}\n"
#      "Ruby was created by {Ruby}\n"
#      "PHP was created by {PHP}"
#      .format_map(languages))

for key in languages:
    print(key, " was created by ", languages[key])
