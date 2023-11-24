#include <sys/wait.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>

/**
 * count - creates zombies
 * Return:- Always 0
 */

int count(void)
{
	while (1)
	{
		sleep(1);
	}

	return (0);
}

/**
 * main - main entry point
 * Return:- Always 0
 */

int main(void)
{
	int k = 0;

	for (; k < 5; k++)
	{
		if (fork() == 0)
		{
			dprintf(1, "Zombie process created, PID: %d\n", getpid());

			return (0);
		}
	}

	count();

	return (0);
}
