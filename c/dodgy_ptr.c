#include<stdlib.h>

void my_func (const int *ptr)
{
    free ((void *)ptr);
}

int main (int argc, char **argv)
{

    const int *p = malloc (1024);

    my_func(p);

    *p = 1234;

    return 0;
}
