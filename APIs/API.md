## API 
An application programming interface is a connection between applications or programs.  

APIs let your product or service communicate with other products and services without having to know how they’re implemented. This can simplify app development, saving time and money.  

APIs let you open up access to your resources while maintaining security and control. How you open access and to whom is up to you. API security is all about good API management, which includes the use of an API gateway. Connecting to APIs, and creating applications that consume the data or functionality exposed by APIs, can be done with a distributed integration platform that connects everything

- Remote APIs
    - Designed to interact through a communications network.  
    - The resources being manipulated by the API are somewhere outside the computer making the request.
    - Because the most widely used communications network is the internet, most APIs are designed based on web standards. 
        - Not all remote APIs are web APIs, but it’s fair to assume that web APIs are remote.

    - Web APIs 
        - Typically use HTTP for request messages and provide a definition of the structure of response messages. 
        - These response messages usually take the form of an XML or JSON file. 
        - Both XML and JSON are preferred formats because they present data in a way that’s easy for other apps to manipulate.

- Simple Object Access Protocol (SOAP) API
    - SOAP is a protocol
    - XML format
    - receives requests through HTTP or SMTP
    - easier for apps running in different environments or written in different languages to share information
- Representational State Transfer (REST) API
    - REST is an architectural style
    - APIs are RESTful as long as they comply with the 6 guiding constraints of a RESTful system:
        - **Client-server architecture**: REST architecture is composed of clients, servers, and resources, and it handles requests through HTTP.
        - **Statelessness**: No client content is stored on the server between requests. Information about the session state is, instead, held with the client.
        - **Cacheability**: Caching can eliminate the need for some client-server interactions.
        - **Layered system**: Client-server interactions can be mediated by additional layers. These layers could offer additional features like load balancing, shared caches, or security.
        - **Code on demand *(optional)***: Servers can extend the functionality of a client by transferring executable code.
        - **Uniform interface**: This constraint is core to the design of RESTful APIs and includes 4 facets: