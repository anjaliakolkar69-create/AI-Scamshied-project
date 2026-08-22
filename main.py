from url_detector1 import extract_urls, analyze_url


print("======================================")
print("          AI SCAMSHIELD")
print("     URL & PHISHING DETECTOR")
print("======================================")



message = input("\nEnter the SMS/message: ")



urls = extract_urls(message)


s
if not urls:

    print("\n No URL found in the message.")


else:

    print("\n URL(s) detected:")


    for url in urls:

        risk, score, reasons = analyze_url(url)

        print("\n--------------------------------------")

        print("URL:", url)

        print("Risk Level:", risk)

        print("Risk Score:", score)

        print("\nReasons:")

        if reasons:

            for reason in reasons:
                print("•", reason)

        else:

            print("• No suspicious pattern detected")


       
        if risk == "HIGH":

            print("\n⚠️ WARNING!")
            print("This link may be dangerous.")
            print("Do NOT open this link.")


        elif risk == "MEDIUM":

            print("\n⚠️ CAUTION!")
            print("This link looks suspicious.")
            print("Be careful before opening it.")


        else:

            print("\n✅ LOW RISK")
            print("No major suspicious pattern detected.")


        print("--------------------------------------")
