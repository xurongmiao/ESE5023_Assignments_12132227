module Declination_angle
implicit none

integer, dimension(12), parameter :: days_per_month = (/31,28,31,30,31,30,31,31,30,31,30,31/)
real, parameter                   :: pi = 3.1415926536 

contains

subroutine declin_angle(month, day, res)
    implicit none
    integer :: d, i, month, day
    real(8) :: tmp1, tmp2, res
    d = 0
    do i = 1, month
        d = d + days_per_month(i)
    enddo
    d = d - (days_per_month(month) - day)

    tmp1 = 360.0 / 365.24
    tmp2 = (tmp1 * (d + 10)) + (360.0 / pi) * 0.0167 * SIN(tmp1 * (d-2) * 2 * pi / 360.0)
    tmp2 = tmp2 * 2 * pi / 360.0
    tmp1 = SIN(-23.44 * 2 * pi / 360.0) * COS(tmp2)
    res  = ASIN(tmp1) * 180.0 / pi

end subroutine declin_angle

end module Declination_angle


! Program Main

! use Declination_angle
! implicit none

! real(8) :: Res

! call declin_angle(12, 31, Res)

! print*, Res

! end program Main