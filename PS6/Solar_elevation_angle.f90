program  Solar_elevation_angle

    use Solar_hour_angle
    use Declination_angle

    implicit none

    integer:: mon, day, hrs, min, del_TZ
    real(8):: dec_angle, sol_hur_angle, Lon, Lat, temp, SEA
    real, parameter                   :: pih = 3.1415926536

    mon = 12
    day = 31
    hrs = 10
    min = 32
    Lon = 114.062996
    Lat = 22.542883
    del_TZ = 8

    ! call declin_angle(12, 31, dec_angle)
    ! call solarhour_angle(11, 24, 15, 30, -8, Lon, sol_hur_angle)

    call declin_angle(mon, day, dec_angle)
    call solarhour_angle(mon, day, hrs, min, del_TZ, Lon, sol_hur_angle)

    temp = sin(Lat * pih / 180.0) * sin(dec_angle * pih / 180.0)
    temp = temp + cos(Lat * pih / 180.0) * cos(dec_angle * pih / 180.0) * cos(sol_hur_angle * pih / 180.0)

    SEA = ASIN(temp) * 180.0  / pih
    print*, 'SEA for Shenzhen (22.542883N, 114.062996E) at 10:32 (Beijing time; UTC+8) on 2021-12-31:', SEA
end program  Solar_elevation_angle