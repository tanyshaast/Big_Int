%module Big_Integer
%{
/* Includes the header in the wrapper code */
#include "Big_integer.h"
%}
/* Parse the header file to generate wrappers */
%include "Big_integer.h"
