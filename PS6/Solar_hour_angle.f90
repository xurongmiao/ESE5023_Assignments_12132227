module Solar_hour_angle
    implicit none
    integer, dimension(12), parameter :: days_per_month = (/31,28,31,30,31,30,31,31,30,31,30,31/)
    real, parameter                   :: pi = 3.1415926536 

    contains
    subroutine solarhour_angle(month, day, hour, minute, del_TZ, Lon, Result)
        implicit none
        integer:: month, day, hour, minute, del_TZ, d, i
        real(8):: Lon, gamma, EoT, Offset, Result, hours

        d = 0
        do i = 1, month
            d = d + days_per_month(i)
        enddo
        d = d - (days_per_month(month) - day) - 1
        
        hours = (minute / 60.0) + hour 
        gamma  = (2 * pi / 365.0) * (d - 1 + (hours - 12.0) / 24.0)
        
        EoT   = 0.
        EoT   = 229.18 * (0.000075 + (0.001868 * cos(gamma)) - (0.032077 * sin(gamma)) )
        EoT   = EoT - 229.18 * ( (0.014615 * cos(2 * gamma)) + (0.040849 * sin(2 * gamma)) )

        Offset = EoT + 4 * (Lon - (15 * del_TZ) )
        hours = hours + (Offset / 60.0)
        Result = 15.0 * (hours - 12.0)
    end subroutine solarhour_angle
    
end module Solar_hour_angle



! Program Main

! use Solar_hour_angle
! implicit none

! real(8) :: Res, L
! L = -118.24
! call solarhour_angle(11, 24, 15, 30, -8, L, Res)
! print*, Res
! end program Main