mydict={
    "fast" : "in aquick manner",
    "saket" :"a good coder",
    "marks" : [1,34,56],
    "anotherdict" : {
        "nilesh" : "my brother"
    }
}
print(list(mydict.keys())) #prints the keys of dictionery
print(list(mydict.values())) #printing the values of dictionery
print(list(mydict.items())) #printing the tuple of te dictionery
print(mydict)
updatedict={
    "sanidhya" : "freind of mine"
}
mydict.update(updatedict) #update the dictionery with key value pairs from update mydict
print(mydict)
print(mydict.get("saket2")) #returns none as saket2 is not present in the dictionery
print(mydict["saket2"]) #throws an error as saket2 is not present in the dictionery