# WAP to create a dictionary of hindi words with values as their english transalation. Provide user with options to look it up.
myDict={
    "pankha":"fan",
    "juta":"shoes",
    "hath":"hand",
    "nakh":"nose",
    "bistar":"bed",
}
a=input("write a hindi word\n")
#print("the meaning of your word is:",myDict[a])
print("the meaning of your word is:",myDict.get(a))