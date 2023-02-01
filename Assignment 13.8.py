#Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL",
#"C", "Reactjs", "Javascript", "Python"]
def sort(thislist):
  
    thislist.sort(key = str)
    return thislist
  

thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]
print(sort(thislist))
