def most_frequent_days(year):
    """
        List of most frequent days of the week in the given year
    """
    import datetime
    daysofweek = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    be = datetime.datetime(year,1,1)
    end = datetime.datetime(year,12,31)
    dif = end - be
    date_list = [(end - datetime.timedelta(days=x)).weekday() for x in range(0, dif.days + 1)]
    tot = {}
    for d in date_list:
        if d in tot.keys():
            tot[d] += 1
        else:
            tot[d] = 1
    res_tot = {}
    for d, num in tot.iteritems():
        if num in res_tot.keys():
            res_tot[num].append(daysofweek[d])
        else:
            res_tot[num] = [daysofweek[d]]
    return res_tot[max(res_tot.keys())]
    # return ['Monday'] 

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
