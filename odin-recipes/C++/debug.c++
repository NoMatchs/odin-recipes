#include <iostream>

using namespace std;

// int main()
// {
//     FILE *fp = fopen("test.txt", "r");
//     if (fp == NULL)
//     {
//         puts("Fail to open file!");
//         exit(0);
//     }

//     fseek(fp, 16, SEEK_SET);
//     char c = fgetc(fp);
//     printf("char：%c", c);
//     fclose(fp);
// }

const int N = 10;

typedef struct
{
    int number;
    char name[30];
    char major[30];
} Student_info;

int main()
{

    FILE *fp = fopen("students.info", "w");
    if (fp == NULL)
    {
        printf("fail to open file!");
        exit(0);
    }

    // Student_info student[N];

    // for (int i = 0; i < N; i++)
    // {
    //     student[i].number = i;
    //     student[i].name[0] = '?';
    //     student[i].name[0] = '?';
    // }

    // fwrite(student, sizeof(Student_info), N, fp);
    // fclose(fp);

    fseek(fp, 5 * sizeof(Student_info), SEEK_SET);
    Student_info stu;

    fread(&stu, sizeof(Student_info), 1, fp);
    printf("Students number:%d\n", stu.number);

    fclose(fp);

    return 0;
}