# There are two kinds of http messages, requests and responses. HTTP operates on the client-server architecture
# and facilitates the exchange of data between said client and server.
# A request is an operation a client wants to perform on the server, and the response is the servers response

# The anatomy of an HTTP message:
# 1. Start line which consists of the method and target url for requests, and the status code for responses.
# 2. The request/response headers
# 3. Optional body for passing data

# HTTP methods define the desired action the client wants to perform on the server are. Examples are:
# GET, POST, PUT, HEAD, DELETE, etc.

# Whenever you click a link youre telling your browser to send a GET request to the server that domain exists
# on.
# When you login to a site, youre sending a POST request to access it.

# Status codes specify the response from the server. We have status codes such as:
# 1xx: Informational codes which report on how client requests are processed.
# 2xx: Success codes indicate the action requested has been successfully accepted for processing
# 3xx: Redirection codes indicate further action must be taken to complete the request
# 4xx: Client error codes indicate errors on the client side
# 5xx: Server error codes indicate errors on the server side

