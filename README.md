# kill-a-process-powershell

The script will do the following:
1. Read a process name as a command-line argument
2. List all currently running instances of that process on the console.
2a. If there is no currently running instance of the specified process, then print out the message, "No such process is running." to the console, and then terminate the script.
3. Kill all currently running instances of the specified process.
4. List all currently running processes on the console, so we can see the specified process is absent.
