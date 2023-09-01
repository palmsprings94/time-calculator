def add_time(given, inp, day=None):

    ihour = inp.split(":")
    imin = ihour[1]
    ihour = ihour[0]

    ghour = given.split(":")
    gmin = ghour[1]
    ghour = ghour[0]
    gmin = gmin.split(" ")
    midday = gmin[1]
    gmin = gmin[0]


    gmin = int(gmin)
    imin = int(imin)
    if imin > 59:
        return "exceed max minutes"
    anmin = gmin + imin
    adhour = int()
    while anmin >= 60:
        anmin = anmin - 60
        adhour = adhour + 1

    ghour = int(ghour)
    ihour = int(ihour) + adhour
    cy = 0
    if ghour == 12:
        ghour = 0
    while ihour >= 12:
        ihour = ihour - 12
        cy = cy + 1
    anhour = ghour + ihour
    while anhour >= 12:
        anhour = anhour - 12
        cy = cy + 1
    if anhour == 0:
        anhour = 12

    y = 0
    carlito = 0
    while cy > 0:
        if midday == "PM":
            midday = "AM"
            y = y + 1
            carlito = carlito + 1
        elif midday == "AM":
            midday = "PM"
        cy = cy - 1

    if carlito == 1:
        carl = "(next day)"
    elif carlito > 1:
        carl = f"({carlito} days later)"
    else:
        carl = ""

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day is None:
        result = f"{anhour}:{anmin:02d} {midday} {carl}"
    elif day in days:
        x = days.index(day)
        z = x + y
        while z > 6:
            z = z - 7
        result = f"{anhour}:{anmin:02d} {midday}, {days[z]} {carl}"

    return print(result)
