def dog_run():
    distance = 100
    firstFriendSpeed = 1
    secondFriendSpeed = 2
    dogSpeed = 5

    friend = "first"
    count = 0

    while distance > 10:
        if friend == "first":
            time_to_meet = distance / (firstFriendSpeed + dogSpeed)
            distance -= time_to_meet * secondFriendSpeed
            friend = "second"
        else:
            time_to_meet = distance / (secondFriendSpeed + dogSpeed)
            distance -= time_to_meet * firstFriendSpeed
            friend = "first"
        count += 1

    return count

result = dog_run()
print("Количество пробежек собаки:", result)
