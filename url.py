# The anatomy of a url: <scheme>://<login>:<password>@<host>:<port>/<path>?<request.parameters>#<anchor>

# Scheme: protocol used for exchanging data with a resource, such as http/https

# Login and Password: prefixes that transmit auth data for some protocols if necessary

# Host: Domain name or IP address site is located. Domain is the name of a site given by the DNS. IP
# is it's address in a server on the network.

# Port: For connection within the specified host. The default port for HTTP connections is port:80 or port:8080
# For HTTPS it's port:443

# Path: The exact address for a file or page within a domain.

# Request.parameters: Parameters transmitted to the server. Depending on params, site may slightly change its
# display. For example, filtering.

# Anchor: Allows you to connect to a specific part of a web page or document.


# Absolute URL's are the whole URL, but you can also use relative URL's which are just
# <path>?<request.params>#<anchor>

# relative paths only work if youre already currently visitin the domain they belong to.

# Retrieve a resource through an absolute URL, then browse it use using relative URL.