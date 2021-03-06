import datetime

vacation_time_table = {
    '학식': {
        '평일': ['10:30 ~ 14:00(중식)'],
        '주말': ['방학중 휴무'],
    },
    '교식': {
        '평일': [
            '11:20 ~ 14:00(중식)',
            '17:00 ~ 18:10(석식)',
        ],
        '주말': ['11:20 ~ 14:00(중식)'],
    },
    '푸드코트': {
        '평일': ['방학중 휴무'],
        '주말': ['방학중 휴무'],
    },
    '스넥코너': {
        '평일': ['방학중 휴무'],
        '주말': ['방학중 휴무'],
    },
    '더 키친': {
        '평일': ['방학중 휴무'],
        '주말': ['방학중 휴무'],
    }
}

time_table = {
    '학식': {
        '평일': [
            '10:30 ~ 14:00(중식)',
            '17:00 ~ 18:30(석식)',
        ],
        '주말': ['10:30 ~ 14:00(중식)'],
    },
    '교식': {
        '평일': [
            '08:00 ~ 09:00(조식)',
            '11:20 ~ 14:00(중식)',
            '17:00 ~ 18:30(석식)',
        ],
        '주말': ['11:20 ~ 14:00(중식)'],
    },
    '푸드코트': {
        '평일': ['10:30 ~ 18:30'],
        '주말': ['휴무'],
    },
    '스넥코너': {
        '평일': ['11:00 ~ 18:00'],
        '주말': ['휴무'],
    },
    '더 키친': {
        '평일': ['08:30 ~ 19:00'],
        '주말': ['10:00 ~ 14:00'],
    }
}


def get_timetable_string(location, is_tomorrow=None):
    is_tomorrow = 1 if is_tomorrow else 0
    week_day = datetime.date.today().weekday() + is_tomorrow
    date_type = '주말' if week_day in [5, 6] else '평일'
    t = time_table[location]
    ret = ''
    look_up_order = '평일 주말'.split()
    for day in look_up_order:
        if day in t:
            day_time = t[day]
            for time in day_time:
                if date_type == day:
                    decorated_day = day + '🍉'
                else:
                    decorated_day = day + '     '
                ret += '\n{}:{}'.format(decorated_day, time)

    return ret
