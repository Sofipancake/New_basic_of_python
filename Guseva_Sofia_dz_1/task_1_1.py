# coding : utf-8

# Задача-1: Реализовать вывод информации о промежутке
# времени в зависимости от его продолжительности
# duration в секундах.

def convert_time(duration: int) -> str:
    if (duration >= 60):
        minutes = duration // 60
        seconds = duration % 60
        if (duration >= 3600):
            hours = minutes // 60
            minutes = minutes % 60
            if (hours >= 24):
                days = hours // 24
                hours = hours % 24
                return f"{days} d {hours} h {minutes} min {seconds} sec"
            else:
                return f"{hours} h {minutes} min {seconds} sec"
        else:
            return f"{minutes} min {seconds} sec"
    else:
        seconds = duration
        return f"{seconds} sec"

duration = 53
result = convert_time(duration)
print(result)

duration = 153
result = convert_time(duration)
print(result)

duration = 4153
result = convert_time(duration)
print(result)

duration = 400153
result = convert_time(duration)
print(result)
