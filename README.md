Welcome to LinearAlgCalc!

This repository is mainly used to display the sourcecode utilized for my library.

This library is built to simplify linear algebra calculations.

To import the necessary functions and classes type 'from linearalgcalc import myfunctions'

This library can be installed through pip with the command 'pip install linearalgcalc==0.1.0'

Classes
 - Vector: A vector with real numbers
 - Complex Number
 - Complex vectors: Vectors with complex numbers
 
 
 Functions
 - Complex
    - re: returns the real part of a complex number
 
    - im: returns the imaginary part of a complex number
 
    - addition: adds two complex numbers
    
    - subtraction: subtracts two complex numbers
    
    - multiplication: multiplies two complex numbers
    
    - conjugate: returns the complex conjugate 
    
    - modulus: calculates the modulus
    
    - polar_form: returns the polar form as a string
    
    - exponent: returns the complex number to the exponent of n
    
    - roots: calculates the nth roots of a complex number
    
    
 - Vector
    - addition: Calculates and returns the sum of two vectors
    
    - subtraction: Calculates and returns the difference of two vectors
  
    - scalar_multiplication: Calculates and returns the product of a vector with a scalar
    
    - norm: Calculates the norm of a vector
    
    - dot_product: Calculates the dot product of two vectors
    
    - angle_between: Calculates the angle between two vectors
    
    - cross_product: Calculates the cross product of two vectors in R3
    
    - projection: Calculates the projection of a vector onto another
    
    - unit_vector: Returns the unit vector equivalent of the vector
    
    - parallelepiped_volume: Calculates and returns the volume of a parallelepiped constructed by three vectors

    - isParallel: Returns a boolean value that is dependent on whether the two vectors are parallel or not
    
 - ComplexVector
    - addition: Calculates and returns the sum of two complex vectors
    
    - subtraction: Calculates and returns the difference of two complex vectors
  
    - scalar_multiplication: Calculates and returns the product of a complex vector with a scalar
    
    - norm: Calculates the norm of a complex vector
    
    - inner_product: Calculates and returns the inner product of a complex vector
