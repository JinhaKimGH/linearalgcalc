from linearalgcalc import myfunctions
import math


def test_re():
    assert myfunctions.Complex(5, -5).re() == 5


def test_im():
    assert myfunctions.Complex(5, -5).im() == -5


def test_addition():
    assert myfunctions.Complex(5, -5).addition(myfunctions.Complex(10, 10)).real == 15
    assert myfunctions.Complex(5, -5).addition(myfunctions.Complex(10, 10)).imaginary == 5


def test_subtraction():
    assert myfunctions.Complex(5, -5).subtraction(myfunctions.Complex(10, 10)).real == -5
    assert myfunctions.Complex(5, -5).subtraction(myfunctions.Complex(10, 10)).imaginary == -15


def test_complex_multiplication():
    assert myfunctions.Complex(1, -2).multiplication(myfunctions.Complex(1, 1)).real == 3
    assert myfunctions.Complex(1, -2).multiplication(myfunctions.Complex(1, 1)).imaginary == -1


def test_complex_conjugate():
    assert myfunctions.Complex(5, -5).conjugate().real == 5
    assert myfunctions.Complex(5, -5).conjugate().imaginary == 5


def test_complex_modulus():
    assert myfunctions.Complex(3, 4).modulus() == 5


def test_complex_exponent():
    assert round(myfunctions.Complex(1, math.sqrt(3)).exponent(2).real) == -2
    assert round(myfunctions.Complex(1, math.sqrt(3)).exponent(2).imaginary) == round(2 * math.sqrt(3))


def test_complex_roots():
    listy = myfunctions.Complex(4, -4 * math.sqrt(3)).roots(3)
    answer = (2 * math.cos(math.pi / 9), -2 * math.sin(math.pi / 9))
    assert round(listy[0].real) == round(answer[0])
    assert round(listy[0].imaginary) == round(answer[1])


def test_vector_addition():
    assert myfunctions.Vector([1, 2, 3]).addition(myfunctions.Vector([4, 5, 6])).numbers[0] == 5
    assert myfunctions.Vector([1, 2, 3]).addition(myfunctions.Vector([4, 5, 6])).numbers[1] == 7
    assert myfunctions.Vector([1, 2, 3]).addition(myfunctions.Vector([4, 5, 6])).numbers[2] == 9


def test_vector_subtraction():
    assert myfunctions.Vector([1, 2, 3]).subtraction(myfunctions.Vector([4, 5, 6])).numbers[0] == -3
    assert myfunctions.Vector([1, 2, 3]).subtraction(myfunctions.Vector([4, 5, 6])).numbers[1] == -3
    assert myfunctions.Vector([1, 2, 3]).subtraction(myfunctions.Vector([4, 5, 6])).numbers[2] == -3


def test_vector_scalar_multiplication():
    assert myfunctions.Vector([1, 2, 3]).scalar_multiplication(3).numbers[0] == 3
    assert myfunctions.Vector([1, 2, 3]).scalar_multiplication(3).numbers[1] == 6
    assert myfunctions.Vector([1, 2, 3]).scalar_multiplication(3).numbers[2] == 9


def test_vector_norm():
    assert myfunctions.Vector([3, 4, 0, 0, 0]).norm() == 5


def test_vector_dot_product():
    assert myfunctions.Vector([1, 2, 3]).dot_product(myfunctions.Vector([1, 2, 3])) == 14


def test_angle_between_vectors():
    assert round(myfunctions.Vector([1, 2, 3]).angle_between(myfunctions.Vector([1, 2, 3]))) == 0


def test_vector_cross_product():
    assert myfunctions.Vector([1, 2, 3]).cross_product(myfunctions.Vector([1, 2, 3])).numbers[0] == 0
    assert myfunctions.Vector([1, 2, 3]).cross_product(myfunctions.Vector([1, 2, 3])).numbers[1] == 0
    assert myfunctions.Vector([1, 2, 3]).cross_product(myfunctions.Vector([1, 2, 3])).numbers[2] == 0


def test_vector_projection():
    assert myfunctions.Vector([1, 0, 0, 0, 0]).projection(myfunctions.Vector([2, 0, 0, 0, 0])).numbers[0] == 1
    assert myfunctions.Vector([1, 0, 0, 0, 0]).projection(myfunctions.Vector([2, 0, 0, 0, 0])).numbers[1] == 0
    assert myfunctions.Vector([1, 0, 0, 0, 0]).projection(myfunctions.Vector([2, 0, 0, 0, 0])).numbers[2] == 0


def test_unit_vector():
    assert round(myfunctions.Vector([3, 4]).unit_vector().numbers[0], 1) == 3 / 5
    assert round(myfunctions.Vector([3, 4]).unit_vector().numbers[1], 1) == 4 / 5


def test_volume_parallelepiped():
    assert myfunctions.Vector([1, 2, 3]).parallelepiped_volume(myfunctions.Vector([3, 0, 6]),
                                                               myfunctions.Vector([7, 1, 9])) == 33


def test_isParallel():
    assert myfunctions.Vector([1, 2, 3]).isParallel(myfunctions.Vector([2, 4, 6])) == True
    assert myfunctions.Vector([1, 2, 3]).isParallel(myfunctions.Vector([3, 4, 6])) == False


def test_complexvector_addition():
    c1 = myfunctions.Complex(1, 2)
    c2 = myfunctions.Complex(3, 4)
    complexVector1 = myfunctions.ComplexVector([c1, c2])
    complexVector2 = myfunctions.ComplexVector([c2, c1])

    assert complexVector1.addition(complexVector2).numbers[0].real == 4
    assert complexVector1.addition(complexVector2).numbers[0].imaginary == 6


def test_complexvector_subtraction():
    c1 = myfunctions.Complex(1, 2)
    c2 = myfunctions.Complex(3, 4)
    complexVector1 = myfunctions.ComplexVector([c1, c2])
    complexVector2 = myfunctions.ComplexVector([c2, c1])

    assert complexVector2.subtraction(complexVector1).numbers[0].real == 2
    assert complexVector2.subtraction(complexVector1).numbers[0].imaginary == 2


def test_complexvector_scalar_multiplication():
    c1 = myfunctions.Complex(1, 2)
    c2 = myfunctions.Complex(3, 4)
    complexVector1 = myfunctions.ComplexVector([c1, c2])
    assert complexVector1.scalar_multiplication(5).numbers[0].real == 5
    assert complexVector1.scalar_multiplication(5).numbers[0].imaginary == 10
    assert complexVector1.scalar_multiplication(5).numbers[1].real == 15
    assert complexVector1.scalar_multiplication(5).numbers[1].imaginary == 20


def test_complexvector_norm():
    c1 = myfunctions.Complex(1, 2)
    c2 = myfunctions.Complex(3, 4)
    complexVector1 = myfunctions.ComplexVector([c1, c2])
    assert complexVector1.norm() == math.sqrt(30)


def test_inner_product():
    c1 = myfunctions.Complex(1, 2)
    c2 = myfunctions.Complex(3, 4)
    complexVector1 = myfunctions.ComplexVector([c1, c2])
    complexVector2 = myfunctions.ComplexVector([c2, c1])
    result = complexVector1.inner_product(complexVector2)
    assert result.real == 22
    assert result.imaginary == 0


def test_matrix_addition():
    assert myfunctions.matrix_addition([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[2, 2, 2], [2, 2, 2], [2, 2, 2]]) == [
        [3, 3, 3], [3, 3, 3], [3, 3, 3]]


def test_matrix_scalar_multiplication():
    assert myfunctions.matrix_scalar_multiplication([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 3) == [[3, 3, 3], [3, 3, 3],
                                                                                              [3, 3, 3]]


def test_matrix_transpose():
    assert myfunctions.matrix_transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]


def test_matrix_multiplication():
    assert myfunctions.matrix_multiplication([[1, 2, 3], [4, 5, 6]], [[10, 11], [20, 21], [30, 31]]) == [[140, 146], [
        320, 335]]
    assert myfunctions.matrix_multiplication([[1, 2, 3], [-1, -1, 1]], [[1], [1], [2]]) == [[9], [0]]


def test_matrix_determinant():
    assert myfunctions.matrix_determinant([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 0
