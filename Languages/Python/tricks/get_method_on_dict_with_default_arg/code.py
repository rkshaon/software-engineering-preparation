# The get() method on dicts
# and its "default" argument

name_for_userid = {
    382: "Rezaul",
    590: "Karim",
    951: "Shaon",
}


def greeting(userid: int = None):
    return "Hi %s!" % name_for_userid.get(userid, "there")


print(greeting(382))        # "Hi Alice!"
print(greeting(333333))     # "Hi there!"
print(greeting())           # "Hi there!"
