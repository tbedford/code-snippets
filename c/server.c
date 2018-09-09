// Server side C/C++ program to demonstrate Socket programming
#include <unistd.h>
#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>

#define PORT 8080
#define BUF_SZ 1024


int main(int argc, char const *argv[])
{
    int server_fd, new_socket, valread; // socket is actually an integer
    char *hello = "Hello from server";

    // set up address
    struct sockaddr_in address; // IPv4 socket address type, cast to before use in socket function
    int addrlen = sizeof(address);
    memset(&address, 0, addrlen);         // clear struct for compatibility and pad sockaddr_in to size of sockaddr
    address.sin_family = AF_INET;         // Address format internet, should match that used in socket creation
    address.sin_addr.s_addr = INADDR_ANY; // Bind ANY IP address or network interface via specified port
    address.sin_port = htons(PORT);       // Convert port number from host byte order to short network byte order

    // Creating socket file descriptor - this uses TCP here (stream-based connection)
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
    {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    // Set socket options
    int opt = 1;
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT,
                   &opt, sizeof(opt)))
    {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }

    // Bind the socket to specified address (which is *not* the address that packets will be sent to)
    if (bind(server_fd, (struct sockaddr *)&address,
             sizeof(address)) < 0)
    {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    // Listen
    if (listen(server_fd, 3) < 0)
    {
        perror("listen");
        exit(EXIT_FAILURE);
    }

    // Accept
    if ((new_socket = accept(server_fd, (struct sockaddr *)&address,
                             (socklen_t *)&addrlen)) < 0)
    {
        perror("accept");
        exit(EXIT_FAILURE);
    }

    // Blocking Read socket
    char buffer[BUF_SZ] = {0};
    valread = read(new_socket, buffer, BUF_SZ);
    printf("%s\n", buffer);

    // Send on socket
    send(new_socket, hello, strlen(hello), 0);
    printf("Hello message sent\n");
    return 0;
}
