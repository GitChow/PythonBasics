from collections import Counter
a = 'Links are created using a specific syntax, the so-called "link pattern". Originally, most wikis[citation needed] used CamelCase to name pages and create links. These are produced by capitalizing words in a phrase and removing the spaces between them (the word "CamelCase" is itself an example). While CamelCase makes linking easy, it also leads to links in a form that deviates from the standard spelling. To link to a page with a single-word title, one must abnormally capitalize one of the letters in the word (e.g. "WiKi" instead of "Wiki"). CamelCase-based wikis are instantly recognizable because they have many links with names such as "TableOfContents" and "BeginnerQuestions." It is possible for a wiki to render the visible anchor of such links "pretty" by reinserting spaces, and possibly also reverting to lower case. However, this reprocessing of the link to improve the readability of the anchor is limited by the loss of capitalization information caused by CamelCase reversal. For example, "RichardWagner" should be rendered as "Richard Wagner", whereas "PopularMusic" should be rendered as "popular music". There is no easy way to determine which capital letters should remain capitalized. As a result, many wikis now have "free linking" using brackets, and some disable CamelCase by default.'

#print(Counter(a).most_common)
# Counter(a).most_common will print all letters and its appearence counter

# format(xxx, '.2f') , to fixed 2 decimal

print(dict((k, format(float(v) / len(a),'.2f')) for k, v in Counter(a).most_common()))

