print "let's get started"
spy_name = raw_input("enter your name :")
spy_salutation = raw_input("enter your salution :")
#concatination of name and salutation
if len(spy_name)>0:
    spy_age=0
    spy_rating=0.0
    spy_is_online=False
    spy_age=int(raw_input("enter your age :"))
    spy_name = spy_salutation + " " +spy_name+str(spy_rating)
    print"alright" + spy_name +"I'd like to know more about you"
    print "Welcome " + spy_name +" glad to have you back with us"
else:
 print 'Invalid name Please try again'
