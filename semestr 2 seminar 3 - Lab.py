def nonlinear_equation(radioactivity, time, N, precision ,interval1, interval2): # возращает decay_time
    decay_time = poplam(interval1, interval2, precision, radioactivity, time, N)
    return decay_time

def sum_residals1_nonlinear_equation(radioactivity, time, N): #возращает sum_residals1
    sum_residals1 = 0.0
    for i in range(N):
       sum_residals1 = sum_residals1 + (radioactivity[i] - math.e ** (-(time[i] / nonlinear_equation(radioactivity, time, N, precision ,interval1, interval2)))) ** 2
    return abs(sum_residals1)

def Znachenie_functsii(decay_time, radioactivity, time, N): #передает значения функции
    znachenie_functsii = 0.0
    for i in range(N):
       znachenie_functsii = znachenie_functsii + time[i] * (math.e ** (-(time[i] / decay_time))) * (radioactivity[i] - math.e ** (-(time[i] / decay_time)))
    return znachenie_functsii

def poplam(interval1, interval2, precision, radioactivity, time, N): #метод деления пополам
    y1 = Znachenie_functsii(interval1, radioactivity, time, N)
    y2 = Znachenie_functsii(interval2, radioactivity, time, N)
    if y1 * y2 <= 0:
        while abs(interval2 - interval1) > precision:
            m = (interval1 + interval2) / 2
            ym = Znachenie_functsii(m, radioactivity, time, N)
            if ym * y1 <= 0:
                interval2 = m
            else:
                interval1 = m
        return (interval1 + interval2) / 2
    else:
        print("net kornei")
        quit()

def linear_equation(radioactivity, time, N): # возращает decay_rate
    decay_rate = 0.0
    verxnyaya_chast_uravneniya = 0.0
    niznyaya_chast_uravneniya = 0.0
    for i in range(N):
         verxnyaya_chast_uravneniya = verxnyaya_chast_uravneniya + (time[i] ** 2)
         niznyaya_chast_uravneniya = niznyaya_chast_uravneniya + (time[i] * (1 - radioactivity[i]))

    decay_rate = verxnyaya_chast_uravneniya / niznyaya_chast_uravneniya
    return decay_rate

def sum_residals2_linear_equation(radioactivity, time, N): #возращает sum_residals2
    sum_residals2 = 0.0
    for i in range(N):
        sum_residals2 = sum_residals2 + (radioactivity[i] -(1 - (time[i] / linear_equation(radioactivity, time, N))))
    return abs(sum_residals2)
sum_residals1 = sum_residals1_nonlinear_equation(radioactivity, time, N)
sum_residals2 = sum_residals2_linear_equation(radioactivity, time, N)
decay_rate = linear_equation(radioactivity, time, N)
decay_time = nonlinear_equation(radioactivity, time, N, precision ,interval1, interval2)