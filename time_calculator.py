def add_time(start, duration, startingDay=" "):

    daysList = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    startingDay = startingDay.lower()
    text =""

    replacedTime1 = start.split(" ")
    replacedTime2 = replacedTime1[0].split(":")
    initialTime = replacedTime2[0]
    initialSession = replacedTime1[1]
    initialDuration = duration.split(":")
    replacedDuration = duration.split(":")

    def amPMConversion():
        if replacedTime1[1] == 'AM':
            convertFlag = False
            amPMConverted = replacedTime1[1].replace("AM", "PM")
        elif replacedTime1[1] == 'PM':
            amPMConverted = replacedTime1[1].replace("PM", "AM")
            convertFlag = True
        return amPMConverted, convertFlag

    amPMConversion = amPMConversion()
    def durationVerification():

        convertFlag = False
        finalDays = ""
        initialTotalHours = int(replacedDuration[0]) + int(replacedDuration[0])

        if int(replacedDuration[1]) > 59:
            replacedDuration[0] = int(replacedDuration[0]) + 1
            replacedDuration[1] = int(replacedDuration[1]) - 60
        else:
            replacedTime2[1] = int(replacedTime2[1]) + int(replacedDuration[1])
            if int(replacedTime2[1]) > 59:
                replacedTime2[0] = int(replacedTime2[0])+ int(replacedDuration[0]) + 1
                replacedTime2[1] = int(replacedTime2[1])-60

                if len(str(replacedTime2[1])) < 2:
                    replacedTime2[1] = str(replacedTime2[1]).zfill(2)
            else:
                replacedTime2[0] = int(replacedTime2[0]) + int(replacedDuration[0])

        if int(replacedTime2[0]) >= 13 and int(replacedTime2[0]) <= 24:
            replacedTime2[0] = int(replacedTime2[0]) - 12
            replacedTime1[1] = amPMConversion[0]
            convertFlag = amPMConversion[1]

        if int(initialDuration[0]) > 24:
            finalTime = (round(int(initialDuration[0])/24, 2))+1
            finalDays = round(finalTime, 0)
            fractionalPart = round(finalTime%1, 2)
            fractionalPartIntoHours = int(round(fractionalPart*24, 1))
            replacedTime2[0] = (int(initialTime) + fractionalPartIntoHours) - 12
            replacedTime1[1] = amPMConversion[0]
            convertFlag = amPMConversion[1]
        else:
            finalDays = 0

        if int(replacedTime2[0]) > 24 and int(initialTotalHours) > 24:
            replacedTime2[0] = int(initialTime) + 1
            finalDays = round(int(initialTotalHours)/24)
            replacedTime1[1] = amPMConversion[0]
            convertFlag = amPMConversion[1]

        elif int(replacedTime2[0]) == 12 and replacedTime1[1] == 'AM':
                replacedTime1[1] = amPMConversion[0]
                convertFlag = amPMConversion[1]

        return replacedTime2[0], replacedTime2[1], replacedTime1[1], convertFlag, finalDays

    convertedTime = durationVerification()
    def calculateDayAndPrintText():

        dayName = ""
        days = round(int(replacedTime2[0])/24)

        if int(initialDuration[0]) > 24 or int(convertedTime[4]) > 0:
            if days <= 0 and int(round(int(convertedTime[4]))) > 0:
                days = int(round(convertedTime[4]))

        if startingDay != " ":
            if days == 0 and (initialDuration[0] != "24" and initialDuration[1] != "00"):
                dayName = ", " + startingDay.capitalize()

            elif days <= 0 or days < 2 or (initialDuration[0] == "24" and initialDuration[1] == "00"):
                dayIndex = daysList.index(startingDay)
                finalPosition = dayIndex+1
                dayName = ", " + daysList[finalPosition].capitalize()

            elif int(replacedTime2[0]) <= 24 and initialDuration[0] <= "24" and convertedTime[4] < 1:
                dayName = ", " +startingDay.capitalize()

            else:
                if (days == 0 and convertedTime[3] == True) or convertedTime[4] > 1:
                    daySearch = (7 - (days % 7)) - 1
                    dayName = ", " + daysList[daySearch].capitalize()

        else:
            dayName = ""

        if (initialDuration[0] == "24" and initialDuration[1] == "00") or (convertedTime[3] == True and days < 2):
            text = dayName + " (next day)"

        elif (days > 1 and int(replacedTime2[0]) > 24) or (days > 1):
            if(days < 2):
                text = dayName
            elif (days > 1):
                text = dayName + " (" + str(days) + " days later)"

        elif int(initialDuration[0]) > 24:
            text = dayName + " (" + str(int(days)) + " days later)"

        elif int(replacedTime2[0]) < 24 and int(initialDuration[0]) <= 24 and convertedTime[3] == False:
            text = dayName

        else:
            text = ""

        return text

    text = calculateDayAndPrintText()

    if int(initialDuration[0]) == 24 and int(initialDuration[1]) == 00:
        new_time = str(initialTime[0])+ ":" +str(replacedTime2[1]).zfill(2)+ " " + initialSession + text

    elif int(convertedTime[0]) >= 12 and int(convertedTime[0]) <= 24 or int(convertedTime[1]) >= 60:
        new_time = str(convertedTime[0])+ ":" +str(convertedTime[1]).zfill(2)+ " " + str(convertedTime[2]) + text

    elif int(initialDuration[0]) > 24:
        new_time = str(convertedTime[0])+ ":" +str(replacedTime2[1]).zfill(2)+ " " +replacedTime1[1] + text

    else:
        new_time = (str(replacedTime2[0])+ ":" +str(replacedTime2[1]).zfill(2)+ " " +replacedTime1[1]) + text

    return new_time
