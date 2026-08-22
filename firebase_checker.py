import os
import firebase_admin
from firebase_admin import credentials, firestore

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


KEY_PATH = os.path.join(BASE_DIR, "serviceaccountkey.json")

if not firebase_admin._apps:
    cred = credentials.Certificate(KEY_PATH)
    firebase_admin.initialize_app(cred)

db = firestore.client()


def check_domain(domain):

    doc = db.collection("url_database").document(domain).get()

    if doc.exists:
        data = doc.to_dict()

        print("\n Found in Firebase!")
        print("Domain:", domain)
        print("Risk Level:", data.get("risk_level", "Not specified"))
        print("Reason:", data.get("reason", "Not specified"))

    else:
        print("\n Domain not found in Firebase")
        print("Domain:", domain)



if __name__ == "__main__":
    check_domain("fake-login.com")
