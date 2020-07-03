def solution(a, b):
    month_day =  [31,29,31,30,31,30,31,31,30,31,30,31]
    day =  ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    total_day = sum(month_day[:a-1])+ b if a > 1 else b
    return day[total_day%7]