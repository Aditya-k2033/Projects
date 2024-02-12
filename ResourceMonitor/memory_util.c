#include <stdio.h>
#include <stdlib.h>

// Function to allocate memory with tracking
void *allocate_with_tracking(size_t size, const char *file, int line)
{
    void *ptr = malloc(size);
    if (ptr)
    {
        printf("Allocated %zu bytes in %s, line %d\n", size, file, line);
    }
    else
    {
        printf("Failed to allocate %zu bytes in %s, line %d\n", size, file, line);
    }
    return ptr;
}

// Function to deallocate memory with tracking
void deallocate_with_tracking(void *ptr, const char *file, int line)
{
    free(ptr);
    printf("Deallocated memory in %s, line %d\n", file, line);
}

// Macros to wrap memory allocation functions with tracking
#define TRACKED_MALLOC(size) allocate_with_tracking(size, __FILE__, __LINE__)
#define TRACKED_FREE(ptr) deallocate_with_tracking(ptr, __FILE__, __LINE__)

int main()
{
    int *dynamicArray = (int *)TRACKED_MALLOC(5 * sizeof(int));

    if (dynamicArray)
    {
        for (int i = 0; i < 5; i++)
        {
            dynamicArray[i] = i * 10;
        }

        // Perform operations with the allocated memory

        TRACKED_FREE(dynamicArray); // Free the allocated memory
    }

    return 0;
}
