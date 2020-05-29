# Michael Fanous Cs87 discussion 5
# Been liking Star Wars so lets pretend we are in the millenium falcon and want to convert from Lightyears to Miles
#define values
def starwarsconversion(lightyears):
    miles = lightyears * 5878559666946
    return miles
# insert commas to make large outputs more readable to user
def placeholder(miles):
    return("{:,}".format(miles))

def main():
    print("Welcome to Star Wars conversions! Lets convert light years to miles!")
    #what user enters
    lightyears = int(input("Please enter an integer in Light years that you want to be converted: "))
    miles=starwarsconversion(lightyears)
    #output of function
    print(lightyears,"light year(s) is equal to ",placeholder(miles),"miles. May the force be with you, Jedi!!" )

main()
    

