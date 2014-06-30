import sys
print (sys.version_info.major)
name_1 = input("Name ")

if name_1 == "Dmitry" and sys.version_info.major == 3:
    print("Your name is %s and major version of python is %s" % (name_1, sys.version_info.major))


uid = "sa"
pwd = "secret"
#print pwd + " is not a good password for " + uid      1
#secret is not a good password for sa
#print "%s is not a good password for %s" % (pwd, uid)