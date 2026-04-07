text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
words = text.split()
for word in words:
    if word[-1] in [',', '.']:
        print(word[:-1] + 'ing' + word[-1], end=' ')
    else:
        print(word + 'ing', end=' ')
