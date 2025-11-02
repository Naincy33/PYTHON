#include<stdio.h>
#include<math.h>

void quadraticEquation(int a, int b, int c){
  
      float D = (b*b)-(4*a*c);
      float root1, root2;
      if (D>0){
        root1 = (-b + sqrt(D)) / (2 * a);
        root2 = (-b - sqrt(D)) / (2 * a);
        printf("Real and distinct roots:\n");
        printf("Root 1 = %.2f\n", root1);
        printf("Root 2 = %.2f\n", root2);
     
      }
      else if (D<0){
        float realPart = -b / (2.0 * a);
        float imagPart = sqrt(-D) / (2.0 * a);
        printf("Imaginary roots:\n");
        printf("Root 1 = %.2f + %.2fi\n", realPart, imagPart);
        printf("Root 2 = %.2f - %.2fi\n", realPart, imagPart);
      }
      else{
        root1 = root2 = -b / (2.0 * a);
        printf("Real and equal roots:\n");
        printf("Root = %.2f\n", root1);

       
      }

    }

int main(){
    int a, b, c;
    printf("Enter a, b, c respectively (space-separated): ");
    scanf("%d %d %d", &a, &b, &c);
    quadraticEquation(a,b,c);

    return 0;

}