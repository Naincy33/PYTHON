s = "but soft what light yonder window breaks"
s+= " in"

words= s.split()

decorated= [(len(word), word) for word in words]
print(decorated)

decorated.sort(reverse=True)
print("\n list after sorting: ")
print(decorated)

sorted_words= [word for length, word in decorated]
print(sorted_words)