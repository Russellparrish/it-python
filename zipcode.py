from banner import banner
banner("ZIPCODE SORTER","by Russell")

print("welcome to Newaygo County zipcode sorter")

    zipcode = int(input("please enter your zipcode."))
    if zipcode == 49327:
        print("the zipcode 49327 is for Grant.")
    elif zipcode == 49337:
        print("the zipcode 49337 is for newaygo.")
    if zipcode == 49412:
        print("the zipcode 49412 is for fremont.")
    elif zipcode == 49309:


    else:
        print("The {zipcode} is not in newaygo county!")
    if input("would you lke enter another zipcode (Y/N)") == "Y":
        continue
    else:
            break






