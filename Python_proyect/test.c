#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main()
{
    /*
     * Creamos una Variable que guarde 50 Caracteres en memoria
     * strcpy copia el texto a la variable creada
     * system ejecuta el texto como comando del systema 
     */
    char command[50];
    strcpy(command, "sfc /scannow");
    system(command);
    return 0;
}