x = int(input("enter an error code, i will tell you its meaning"))
def errorcode(x):
    match x:
        case 400:
            print("Bad Request")
        case 401:
            print("Unauthorized")
        case 405:
            print("Method Not Allowed")
         case 406:
             print("Not Acceptable")


 #test it
 #errorcode(400)
 #errorcode(405)



errorcode(x)
quit()

