#!/usr/bin/env python3

mad_lib = {}

for key in ['noun', 'verb', 'adjective', 'adverb']:
    mad_lib[key] = input("Enter a {}: ".format(key))


story = "You did {} your {} {} {} spaghetti, What's that suppose to mean?!"

print(story.format(mad_lib['verb'],
                   mad_lib['adjective'],
                   mad_lib['noun'],
                   mad_lib['adverb'])
      )
