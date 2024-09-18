def percentage(part, whole):
  Percentage = 100 * float(part)/float(whole)
  return float(Percentage)

def script():
    points_earned = input("How many points were earned? ")
    total_points = input("How many points possible? ")


    score = percentage(points_earned, total_points)


    if score <= 50:
        print("Score: F")
    elif score >= 51 and score <= 60:
        print('Score: D')
    elif score >= 61 and score <= 75:
        print('Score: C')
    elif score >= 76 and score <= 88:
        print("Score: B")
    elif score >= 89 and score <= 100:
        print("Score: A")
    else:
        print("invalid score")



    reset = input("Restart Program y/n: ")
    if reset == "y":
        print("restarting...")
        script()
    else:
        print("goodbye :)")

script()