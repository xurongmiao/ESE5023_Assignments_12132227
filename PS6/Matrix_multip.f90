subroutine Matrix_multip(m, n, res)
    implicit none

    real(8),dimension(5, 3) :: M
    real(8),dimension(3, 5) :: N
    real(8),dimension(5, 5) :: Res
    real(8)                 :: tmp
    integer                 :: i, j, w

    do i = 1, 5
        do j = 1, 5
            tmp = 0.
            do w = 1, 3
                tmp = tmp + (m(i, w) * n(w, j))
            enddo
            res(i,j) = tmp
        enddo
    enddo

end subroutine Matrix_multip