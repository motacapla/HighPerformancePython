//
// 2018/06/17
// lib_tkd.c
// ** This library has been developed by tikeda **
//
//To compile:
//$ gcc -cpp -fPIC -shared libadd.c -lm -o libadd.so -O3
//

#include <stdio.h>

void add_matrix(double **matrix, int row, int col, int n) {
  int i, j, k;
  for(i=0; i<n; i++){
    for(j=0; j<row; j++){
      for(k=0; k<col; k++){
	matrix[j][k] = matrix[j][k] + 1;
      }
    }
  }
}
