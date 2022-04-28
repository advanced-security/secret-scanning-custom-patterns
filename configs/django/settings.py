# Django keys

SECRET_KEY = "DJango_Secret_Key1"
SECRET_KEY = "DJango_Secret_Key2"
SECRET_KEY = "DJango_Secret_Key3"

# False positives

SECRET_KEY = os.environ.get("test")
SECRET_KEY = os.environ["test"]

secret_key = "Django_ThisIsAFalsePositive"
